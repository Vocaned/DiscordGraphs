import datetime
import os
import json
import io
import zipfile

def daterange(date1: datetime, date2: datetime) -> datetime.timedelta:
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + datetime.timedelta(n)

def decompressdata(name: str) -> str:
    """Decompresses a zip and returns a json object"""
    path = os.path.join('data', name)

    with zipfile.ZipFile(f'{path}.zip') as file:
        return json.loads(file.read(f'{name}.json'))

def compressdata(j, name: str):
    """Compresses json data into a zip and writes it into a file"""
    path = os.path.join('data', name)

    with zipfile.ZipFile(f'{path}.zip', 'w', compression=zipfile.ZIP_DEFLATED) as file:
        file.writestr(f'{name}.json', json.dumps(j, indent=None))