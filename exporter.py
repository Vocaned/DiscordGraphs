import subprocess
import sys
import os
import json
from config import token
from utils import compressdata, decompressdata

EXPORTERPATH = 'DiscordChatExporter/DiscordChatExporter.Cli.dll'

def downloadMessages(token, id, compress, after=None):
    assert channelid.isdigit()
    file = os.path.join('data', f'{channelid}.json')
    print('Downloading messages.. This will take a while!')
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

    if compress:
        print('Compressing data')
        with open(file) as f:
            data = json.load(f)
        os.remove(file)
        compressdata(data, channelid)
        print('Channel exported')

def main(channelid: str):
    assert channelid.isdigit()

    if not os.path.exists('data'):
        os.makedirs('data')

    if not os.path.exists(os.path.join('data', f'{channelid}.zip')):
        downloadMessages(token, channelid, True)
    else:
        print('Existing data found. Initializing...')
        # FIXME: THIS WILL KILL RAM USAGE
        olddata = decompressdata(channelid)

        # Get last message timestamp
        after = olddata['messages'][-1]['timestamp']

        downloadMessages(token, channelid, False, after)

        print('Updating data')
        with open(os.path.join('data', f'{channelid}.json')) as f:
            newdata = json.load(f)
        os.remove(os.path.join('data', f'{channelid}.json'))

        # Append new messages to old ones
        # FIXME: HACK: skipping first message since it's duplicate, it shouldn't be downloaded at all
        olddata['messages'] += newdata['messages'][1:]

        olddata['messageCount'] += newdata['messageCount'] - 1 # -1 fixme ^

        # Update guild/channel info in case those have updated
        olddata['guild'] = newdata['guild']
        olddata['channel'] = newdata['channel']

        print('Compressing data')
        compressdata(olddata, channelid)

        print(f'Channel exported')

if __name__ == "__main__":
    channelid = input('Channel ID: ')
    main(channelid)