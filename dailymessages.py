import typing
import json
import datetime
import matplotlib.pyplot as plt

from utils import daterange, Line
from plot import lineplot

def dailymessages(jsonfile: str) -> typing.Tuple[str, dict, dict]:
    """Returns discord channel name, a list of all user IDs who have sent a message and a dictionary including the number of messages every day from the start of the log to the end"""
    with open(jsonfile, 'r') as f:
        data = json.loads(f.read())

    msgs = []
    users = []
    daily = {}

    # Init daily message count dictionary with all days between first and last message
    start_dt = datetime.date.fromisoformat(data["messages"][0]["timestamp"].split("T")[0])
    end_dt = datetime.date.fromisoformat(data["messages"][-1]["timestamp"].split("T")[0])
    for dt in daterange(start_dt, end_dt):
        daily[dt.strftime("%Y-%m-%d")] = 0

    for i in range(len(data["messages"])):
        msg = data["messages"][i]["content"]
        date = data["messages"][i]["timestamp"].split("T")[0]
        user = data["messages"][i]["author"]["id"]
        msgs.append(msg)

        if not user in users:
            users.append(user)

        daily[date] += 1

    return (data['channel']['name'], users, daily)

if __name__ == "__main__":
    print('Parsing data...')
    name, users, data = dailymessages(input('DiscordChatExporter JSON file path: '))

    print(f"[#{name}] Total messages: {len(data)}")
    print(f"[#{name}] Unique chatters: {len(users)}")
    lineplot(Line(list(data.keys()), list(data.values()), color="red", label=f"Daily messages in #{name}"))