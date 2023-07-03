import requests
import json
import tomllib
import random
import time
from datetime import date, datetime, timedelta, timezone

with open('config.toml', 'rb') as f:
    config = tomllib.load(f)

client = requests.Session()
if config['account']['bot']:
    client.headers = {'Authorization': 'Bot ' + config['account']['token']}
else:
    client.headers = {
        'Authority': 'discord.com',
        'Accept': '*/*',
        'Accept-Language': 'en-US',
        'Authorization': config['account']['token'],
        'Referer': 'https://discord.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Linux',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-discord-locale': 'en-US',
        'x-discord-timezone': 'Europe/London',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIxMDU3OCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
    }

def getSnowflake(time: date) -> int:
    timestamp = int(datetime(year=time.year, month=time.month, day=time.day, tzinfo=timezone.utc).timestamp()) * 1000
    return timestamp-1420070400000 << 22

def search(guild: int, channel: int, before: int | None = None, after: int | None = None) -> int:
    queries: list[str] = []
    if channel:
        queries.append(f'channel_id={channel}')
    if before:
        queries.append(f'max_id={before}')
    if after:
        queries.append(f'min_id={after}')

    res = client.get(f'https://discord.com/api/v9/guilds/{guild}/messages/search?{"&".join(queries)}').json()
    print(f'Count: {res["total_results"]}')
    return res["total_results"]

def getDailyMessages(day: date) -> int:
    min_snowlake = getSnowflake(day)
    max_snowflake = getSnowflake(day + timedelta(days=1))
    print(f'Getting all daily messages for {day}')

    return search(config['data']['guild_id'], config['data']['channel_id'], max_snowflake, min_snowlake)

if __name__ == '__main__':
    start_date: date = config['data']['range'][0]
    end_date: date = config['data']['range'][1]
    dates = [start_date + timedelta(days=x) for x in range(0, (end_date-start_date).days)]

    # TODO: get this data programmatically
    results: dict = {
        'metadata': {
            'guild_id': '0',
            'channel_id': '0',
            'guild': '.',
            'channel': '#.'
        },
        'data': []
    }

    try:
        for date in dates:
            results['data'].append({'date': date.strftime('%Y-%m-%d'), 'count': getDailyMessages(date)})
            time.sleep(random.randint(2, 3))
    finally:
        with open(f'data/{config["data"]["channel_id"]}.json', 'w', encoding='utf-8') as f:
            json.dump(results, f)
