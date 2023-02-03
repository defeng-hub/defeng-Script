import json
import re

import requests


def getUserInfo(sec_uid, douyinheaders):
    useinfo = "https://www.iesdouyin.com/web/api/v2/user/info/?sec_uid={}".format(sec_uid)

    resp = requests.get(useinfo, headers=douyinheaders)

    userinfo = json.loads(resp.text)
    name = userinfo['user_info']['nickname']

    print("用户名:", name)
    pass


def getUserName(sec_uid, douyinheaders):
    useinfo = "https://www.iesdouyin.com/web/api/v2/user/info/?sec_uid={}".format(sec_uid)

    try:
        resp = requests.get(useinfo, headers=douyinheaders)
        userinfo = json.loads(resp.text)
        name = userinfo['user_info']['nickname']
        return name
    except:
        return ""


def getSec_uid(url):
    try:
        lsheaders = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                          "Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/107.0.0.0 "
        }
        url = re.findall('(https?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]+)', url)[0]
        resp = requests.get(url=url, headers=lsheaders, allow_redirects=False)
        location = resp.headers['location']
        temp = location.split('&')
        sec_uid = temp[4].split('=')[1]
        return sec_uid
    except:
        return ""
