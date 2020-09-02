import json
from datetime import timedelta, date
import numpy as np
import matplotlib.pyplot as plt

xtickdensity = 15
ytickdensity = 500


with open('channel.json') as f:
    furrydata = json.loads(f.read())

print("Parsing data...")

msgs = []
dailyfurry = {}
usersfurry = []

# Init daily message count dictionary with all days between first and last message
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)
start_dt = date.fromisoformat(furrydata["messages"][0]["timestamp"].split("T")[0])
end_dt = date.fromisoformat(furrydata["messages"][-1]["timestamp"].split("T")[0])
for dt in daterange(start_dt, end_dt):
    dailyfurry[dt.strftime("%Y-%m-%d")] = 0

for i in range(len(furrydata["messages"])):
    msg = furrydata["messages"][i]["content"]
    date = furrydata["messages"][i]["timestamp"].split("T")[0]
    user = furrydata["messages"][i]["author"]["id"]
    msgs.append(msg)

    if not user in usersfurry:
        usersfurry.append(user)

    dailyfurry[date] += 1

print()
print(f'[#furry-channel] Total messages: {len(msgs)}')
print(f'[#furry-channel] Unique chatters: {len(usersfurry)}')

fig, ax = plt.subplots()

#line1, = ax.plot(list(dailygeneral.keys()), list(dailygeneral.values()), color="blue", label='Daily unique messages in #general')
line2, = ax.plot(list(dailyfurry.keys()), list(dailyfurry.values()), color="red", label='Daily messages in #furry-channel')

plt.xticks(list(dailyfurry.keys())[::xtickdensity]) #show every n days in ticks
plt.yticks(range(0, max(dailyfurry.values())+ytickdensity, ytickdensity))

plt.grid(b=True, which='major', color='#888888', linestyle='-', alpha=0.5)

ax.legend()
plt.show()