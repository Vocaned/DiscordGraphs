from dailymessages import dailymessages
from plotcreator import multiplot

if __name__ == "__main__":
    color = 0
    colors = ("red", "blue", "green", "yellow", "orange", "pink", "lime", "gray")
    datas = []
    inputs = []
    inp = None


    while inp != '':
        inp = input('DiscordChatExporter JSON file path. Empty to stop: ')
        if inp:
            inputs.append(inp)

    print('Parsing data...')

    for file in inputs:
        name, users, data = dailymessages(file)
        print(f"[#{name}] Total messages: {len(data)}")
        print(f"[#{name}] Unique chatters: {len(users)}")
        datas.append((list(data.keys()), list(data.values()), colors[color%len(colors)], f'Daily unique messages in #{name}'))
        color += 1

    multiplot(datas)