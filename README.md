# DiscordGraphs

Python scripts that generate graphs based on data downloaded from Discord using [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter)


1. Clone repo
2. Download [DiscordChatExporter.CLI](https://github.com/Tyrrrz/DiscordChatExporter/releases) and extract it in a folder inside the repo called `DiscordChatExporter`
3. Make a `config.py` file, inside it add `token = "[token here]"`
4. Run `exporter.py` to download a channel
5. Run a script

Available scripts:

* dailymessages.py - Graph how many messages are sent every day
* comparedailymessages.py - Graph that compares different channels based on their number of daily messages
* mostusedemotes.py - Top 25 most used emotes in a channel
* mostactivechatter.py - Top 25 most active chatters in a channel