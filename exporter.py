import subprocess
import sys
import os
import json
from config import token

EXPORTERPATH = 'DiscordChatExporter/DiscordChatExporter.Cli.dll'

# TODO: DearPyGui gui.py

def downloadMessages(token, id, file, after=None):
    print('Downloading messages.. This will take a while')
    args = ['-f', 'json',
            '-t', token,
            '-c', id,
            '-o', file]
    if after:
        args.append('--after')
        args.append(after)
    output = subprocess.check_output(['dotnet', EXPORTERPATH, 'export', *args])
    if not os.path.exists(file):
        print('Could not download messages')
        print(output.decode('utf-8'))
        exit(1)
    print('Channel exported')

def main(channelid):
    file = f'data/{channelid}.json'
    if not os.path.exists(file):
        downloadMessages(token, channelid, file)
    else:
        print('Initializing...')
        # FIXME: THIS WILL KILL RAM USAGE
        with open(file) as f:
            olddata = json.load(f)

        # Get last message timestamp
        after = olddata['messages'][-1]['timestamp']

        downloadMessages(token, channelid, file, after)

        print('Updating messages')
        with open(file) as f:
            newdata = json.load(f)

        # Append new messages to old ones
        # FIXME: HACK: skipping first message since it's duplicate, it shouldn't be downloaded at all
        olddata['messages'] += newdata['messages'][1:]

        olddata['messageCount'] += newdata['messageCount'] - 1 # -1 fixme ^

        # Update guild/channel info in case those have updated
        olddata['guild'] = newdata['guild']
        olddata['channel'] = newdata['channel']

        # Write merged file
        with open(file, 'w') as f:
            json.dump(olddata, f, indent=2)

if __name__ == "__main__":
    channelid = input('Channel ID: ')
    assert channelid.isdigit()
    main(channelid)