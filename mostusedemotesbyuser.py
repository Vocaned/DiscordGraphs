import json
import re
import typing
from datetime import datetime
from utils import checkChannelID
from plotcreator import horizontalbar

def mostusedemotesbyuser(jsonfile: str, userid: str) -> typing.Tuple[str, str, dict]:
    """Returns discord channel name, user name and a list of top 25 most used emotes"""
    with open(jsonfile) as f:
        data = json.loads(f.read())

    username = None
    emotes = {}
    for i in range(len(data["messages"])):
        user = data["messages"][i]["author"]["id"]
        msg = data["messages"][i]["content"]
        if user != userid:
            continue

        username = f'{data["messages"][i]["author"]["name"]}#{data["messages"][i]["author"]["discriminator"]}'

        found = re.findall(':\\w+?:', msg)
        for emote in found:
            if emote in emotes:
                emotes[emote] += 1
            else:
                emotes[emote] = 1

    emotes = {key: value for key , value in sorted(emotes.items(), key=lambda kv: kv[1])[-25:]}

    return (data['channel']['name'], username, emotes)

if __name__ == "__main__":
    channelid = input('Channel ID: ')
    userid = input('User ID: ')
    jsonfile = checkChannelID(channelid)
    print('Parsing data...')
    name, username, data = mostusedemotesbyuser(jsonfile, userid)
    horizontalbar(list(data.keys()), list(data.values()), 'Number of times used', 'Emote', f'Most used emotes in #{name} by {username} (as of {datetime.today().strftime("%Y-%m-%d")})')