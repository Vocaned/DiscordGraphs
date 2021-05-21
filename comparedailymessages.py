from dailymessages import dailymessages
from utils import checkChannelID
from plotcreator import multiplot

if __name__ == "__main__":
    color = 0
    colors = ("blue", "red", "green", "yellow", "orange", "pink", "lime", "gray")
    datas = []
    inputs = []
    inp = None

    while inp != '':
        inp = input('Channel ID: (empty to stop) ')
        if not inp:
            continue
        inputs.append(checkChannelID(inp))

    print('Parsing data...')

    for file in inputs:
        name, users, data = dailymessages(file)
        num = 0
        for key in data.keys():
            num += int(data[key])
        print(f"[#{name}] Total messages: {num}")
        print(f"[#{name}] Unique chatters: {len(users)}")
        datas.append((list(data.keys()), list(data.values()), colors[color%len(colors)], f'Daily messages in #{name}'))
        color += 1

    multiplot(datas)