#!/bin/bash
read -p 'After: ' after
read -p 'Channel ID: ' channelid
read -sp 'Token: ' token
echo .
dotnet DiscordChatExporter/DiscordChatExporter.Cli.dll export -t "$token" -c "$channelid" -f json --after "$after"