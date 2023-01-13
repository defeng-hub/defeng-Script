import json
import urllib.parse
import requests

loginUrl = "https://haojiahuo.top/auth/login"
qiandao = "https://haojiahuo.top/user/checkin"


cookielogin = "lang=zh-cn; crisp-client%2Fsession%2F377cb669-2bb3-4a4d-a3e3-964f322c07a9%2Fdb32067f-2f06-3975-b93e-9701ab19ac93=session_ebd7b25d-4ea4-46d0-aa5b-def1367f7980; mtauth=a1933c924433621c3446d39bff490237; pop=yes; ip=e9ac1c3b76f4cbe6396ae591284a24ea; expire_in=1674203106; crisp-client%2Fsession%2F377cb669-2bb3-4a4d-a3e3-964f322c07a9=session_f0ef17e9-a30b-49eb-a64c-96c11c934548; crisp-client%2Fsession%2F377cb669-2bb3-4a4d-a3e3-964f322c07a9%2F64c6c130-1a33-3694-b167-3165b9f56962=session_f0ef17e9-a30b-49eb-a64c-96c11c934548qq"
loginheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36 Edg/106.0.1370.37',
    'Referer': "https://haojiahuo.top/auth/login",
    "Accept": "application/json, text/javascript, */*; ",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://haojiahuo.top",
    "X-Requested-With": "XMLHttpRequest",
    "Host": "haojiahuo.top",
    "Cookie": cookielogin
}

res1 = requests.post(loginUrl, headers=loginheaders,
                     data="email=12"+str((103+452))+"4566%40"+cookielogin[-2:]+".com&passwd=OldSeven&remember_me=on&code=")


cookies = """lang=zh-cn; crisp-client%2Fsession%2F377cb669-2bb3-4a4d-a3e3-964f322c07a9%2Fdb32067f-2f06-3975-b93e-9701ab19ac93=session_ebd7b25d-4ea4-46d0-aa5b-def1367f7980; uid=28801; email=125554566%40qq.com; key=c3865272f070bc5dd26f54e811362394d972fa48ea906; ip=2ee0f9f0acc4432b7d2baeadd51aa2a0; expire_in=1674189081; PHPSESSID=k1c0s10hq6e6m4padmjc9g2o24; mtauth=a1933c924433621c3446d39bff490237; pop=yes; crisp-client%2Fsession%2F377cb669-2bb3-4a4d-a3e3-964f322c07a9=session_a14177fb-e890-4b9f-8379-f8ff4816c1b4; crisp-client%2Fsession%2F377cb669-2bb3-4a4d-a3e3-964f322c07a9%2F64c6c130-1a33-3694-b167-3165b9f56962=session_a14177fb-e890-4b9f-8379-f8ff4816c1b4"""

qiandaoheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36 Edg/106.0.1370.37',
    'Referer': "https://haojiahuo.top/user",
    "Accept": "application/json, text/javascript, */*; ",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://haojiahuo.top",
    "X-Requested-With": "XMLHttpRequest",
    "Host": "haojiahuo.top",
}

res = requests.post(qiandao, headers=qiandaoheaders, cookies=res1.cookies)

resText = bytes(res.text, encoding="utf8").decode("unicode_escape")
print(resText)
