import base64
import json


def encoded():
    with open('station_telecodes.json', 'r', encoding='utf-8') as f:
        station_telecodes = json.load(f)
    encoded = base64.b64encode(json.dumps(station_telecodes, separators=(',', ':')).encode('utf-8')).decode('utf-8')

    with open('encoded_station_telecode.py', 'w', encoding='utf-8') as f:
        f.write(f"encoded_json = '{encoded}'\n")


if __name__ == "__main__":
    encoded()
