import json
import typing
from datetime import datetime
from utils import decompressdata
from plotcreator import horizontalbar

def mostactivechatter(channelid: str) -> typing.Tuple[str, dict]:
    """Returns discord channel name and a list of top 25 most active chatters"""
    data = decompressdata(channelid)

    users = {}
    userdict = {}
    for i in range(len(data["messages"])):
        user = data["messages"][i]["author"]["id"]

        # HACK: Always rewrite the user dictionary in case their name has changed; probably causes *minor* performance issues
        userdict[user] = f'{data["messages"][i]["author"]["name"]}#{data["messages"][i]["author"]["discriminator"]}'

        if user not in users:
            users[user] = 1
        else:
            users[user] += 1

    full = {userdict[key]: value for key, value in sorted(users.items(), key=lambda kv: kv[1])[-25:]}

    return (data['channel']['name'], full)

if __name__ == "__main__":
    channelid = input('Channel ID: ')
    assert channelid.isdigit()
    print('Parsing data...')
    name, data = mostactivechatter(channelid)
    horizontalbar(list(data.keys()), list(data.values()), 'Number of messages', 'User', f'Most active chatters in #{name} (as of {datetime.today().strftime("%Y-%m-%d")})')