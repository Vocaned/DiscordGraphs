import typing
import json
import datetime

from utils import daterange, decompressdata
from plotcreator import lineplot

def dailymessages(channelid: str) -> typing.Tuple[str, dict, dict]:
    """Returns discord channel name, a list of all user IDs who have sent a message and a dictionary including the number of messages every day from the start of the log to the end"""
    data = decompressdata(channelid)

    users = []
    daily = {}

    # Init daily message count dictionary with all days between first and last message
    start_dt = datetime.date.fromisoformat(data["messages"][0]["timestamp"].split("T")[0])
    end_dt = datetime.date.fromisoformat(data["messages"][-1]["timestamp"].split("T")[0])
    for dt in daterange(start_dt, end_dt):
        daily[dt.strftime("%Y-%m-%d")] = 0

    for i in range(len(data["messages"])):
        date = data["messages"][i]["timestamp"].split("T")[0]
        user = data["messages"][i]["author"]["id"]

        if not user in users:
            users.append(user)

        daily[date] += 1

    return (data['channel']['name'], users, daily)

if __name__ == "__main__":
    channelid = input('Channel ID: ')
    assert channelid.isdigit()
    print('Parsing data...')
    name, users, data = dailymessages(channelid)

    num = 0
    for key in data.keys():
        num += int(data[key])
    print(f"[#{name}] Total messages: {num}")
    print(f"[#{name}] Unique chatters: {len(users)}")
    lineplot(list(data.keys()), list(data.values()), color="blue", label=f"Daily messages in #{name}")