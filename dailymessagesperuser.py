import typing
import json
import datetime

from utils import daterange, decompressdata
from plotcreator import lineplot

def dailymessagesperuser(channelid: str, userid: str) -> typing.Tuple[str, str, dict]:
    """Returns discord channel name, user name and a dictionary including the number of messages every day from the start of the log to the end"""
    data = decompressdata(channelid)

    username = None
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

        date = data["messages"][i]["timestamp"].split("T")[0]
        username = f'{data["messages"][i]["author"]["name"]}#{data["messages"][i]["author"]["discriminator"]}'
        daily[date] += 1

    # Remove empty messages from before the first message by user was sent
    for dt in daterange(start_dt, end_dt):
        if not daily[dt.strftime("%Y-%m-%d")]:
            del daily[dt.strftime("%Y-%m-%d")]
        else:
            break

    return (data['channel']['name'], username, daily)

if __name__ == "__main__":
    channelid = input('Channel ID: ')
    userid = input('User ID: ')
    assert channelid.isdigit()
    assert userid.isdigit()
    print('Parsing data...')
    name, username, data = dailymessagesperuser(channelid, userid)

    num = 0
    for key in data.keys():
        num += int(data[key])
    print(f"[#{name}] Total messages by {username}: {num}")
    print(f"[#{name}] Average messages by {username} per day: {round(num/len(data), 2)}")
    lineplot(list(data.keys()), list(data.values()), color="blue", label=f"Daily messages in #{name} by {username}")