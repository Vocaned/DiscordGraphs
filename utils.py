import datetime
import os
import exporter

def checkChannelID(id):
    assert id.isdigit()
    if not os.path.exists(f'data/{id}.json'):
        exporter.main(id)
    return f'data/{id}.json'

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + datetime.timedelta(n)