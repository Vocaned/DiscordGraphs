import typing
import json
import datetime

from utils import daterange, Line, checkChannelID
from plotcreator import lineplot

def dailymessagesperperson(jsonfile: str, userid: str) -> typing.Tuple[str, str, dict]:
    """Returns discord channel name, user name and a dictionary including the number of messages every day from the start of the log to the end"""
    with open(jsonfile, 'r') as f:
        data = json.loads(f.read())

    username = None

    msgs = []
    daily = {}

    # Init daily message count dictionary with all days between first and last message
    start_dt = datetime.date.fromisoformat(data["messages"][0]["timestamp"].split("T")[0])
    end_dt = datetime.date.fromisoformat(data["messages"][-1]["timestamp"].split("T")[0])
    for dt in daterange(start_dt, end_dt):
        daily[dt.strftime("%Y-%m-%d")] = 0

    for i in range(len(data["messages"])):
        user = data["messages"][i]["author"]["id"]
        if user != userid:
            continue
        msg = data["messages"][i]["content"]
        date = data["messages"][i]["timestamp"].split("T")[0]
        msgs.append(msg)
        
        username = f'{data["messages"][i]["author"]["name"]}#{data["messages"][i]["author"]["discriminator"]}'

        daily[date] += 1

    for dt in daterange(start_dt, end_dt):
        if not daily[dt.strftime("%Y-%m-%d")]:
            del daily[dt.strftime("%Y-%m-%d")]
        else:
            break

    return (data['channel']['name'], username, daily)

if __name__ == "__main__":
    channelid = input('Channel ID: ')
    userid = input('User ID: ')
    jsonfile = checkChannelID(channelid)
    print('Parsing data...')
    name, username, data = dailymessagesperperson(jsonfile, userid)

    num = 0
    for key in data.keys():
        num += int(data[key])
    print(f"[#{name}] Total messages: {num}")
    lineplot(list(data.keys()), list(data.values()), color="blue", label=f"Daily messages in #{name} by {username}")