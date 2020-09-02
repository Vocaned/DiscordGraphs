import json
import re
import typing
from plotcreator import horizontalbar


def mostusedemotes(jsonfile: str) -> typing.Tuple[str, dict]:
    """Returns discord channel name and a list of top 25 most used emotes"""
    with open(jsonfile) as f:
        data = json.loads(f.read())

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
    jsonfile = input('DiscordChatExporter JSON file path: ')
    print('Parsing data...')
    name, data = mostusedemotes(jsonfile)

    horizontalbar(list(data.keys()), list(data.values()), 'Number of times used', 'Emote', 'Most used emotes in channel')