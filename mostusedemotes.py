import json
import re
import typing
from datetime import datetime
from utils import decompressdata
from plotcreator import horizontalbar

def mostusedemotes(channelid: str) -> typing.Tuple[str, dict]:
    """Returns discord channel name and a list of top 25 most used emotes"""
    data = decompressdata(channelid)

    emotes = {}
    for i in range(len(data["messages"])):
        msg = data["messages"][i]["content"]

        found = re.findall(':\\w+?:', msg)
        for emote in found:
            if emote in emotes:
                emotes[emote] += 1
            else:
                emotes[emote] = 1

    emotes = {key: value for key , value in sorted(emotes.items(), key=lambda kv: kv[1])[-25:]}

    return (data['channel']['name'], emotes)

if __name__ == "__main__":
    channelid = input('Channel ID: ')
    assert channelid.isdigit()
    print('Parsing data...')
    name, data = mostusedemotes(channelid)
    horizontalbar(list(data.keys()), list(data.values()), 'Number of times used', 'Emote', f'Most used emotes in #{name} (as of {datetime.today().strftime("%Y-%m-%d")})')