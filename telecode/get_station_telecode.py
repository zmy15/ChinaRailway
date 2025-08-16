import requests
import json
import time

url = "https://kyfw.12306.cn/index/otn/index12306/queryAllCacheSaleTime"
headers = {
    "Cookie": "JSESSIONID=9C9E34F1FAD965B26639509A78C26978; BIGipServerpool_index=787481098.43286.0000; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=66060810.50210.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}
res = {}


def main():
    """
    获取12306车站电报码
    """
    content_json = requests.get(url=url, headers=headers).json()
    time.sleep(3)  # 防止被检测（不要低于3）
    datas = content_json["data"]
    for data in datas:
        station_name = data["station_name"]
        station_telecode = data["station_telecode"]
        res.setdefault(station_name, station_telecode)
    with open("station_telecodes.json", "w") as f:
        json.dump(res, f, indent=4, ensure_ascii=False, encodings="utf-8")


if __name__ == "__main__":
    main()
