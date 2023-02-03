import json
import re

import requests

headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/107.0.0.0 "
}

share = '长按复制此条消息，打开抖音搜索，查看TA的更多作品。https://v.douyin.com/Br5gAmG/'

url = re.findall('(https?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]+)', share)[0]
resp = requests.get(url=url, headers=headers, allow_redirects=False)
location = resp.headers['location']
temp = location.split('&')
sec_uid = temp[4].split('=')[1]
print(sec_uid)


lsurl = location.split("?")[0]
sec_uid = lsurl.split("/")[-1]


