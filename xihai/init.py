from conf import douyin_ck, user_list

douyinheaders = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": douyin_ck,
    "Host": "m.douyin.com",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/107.0.0.0 "
}

monitorUser = {
    "https://v.douyin.com/BrE92Kp/": ["风月鉴", "MS4wLjABAAAAtxsohPRa6MhnS5moiCWcRJ53NQrSOAXAwtIxXOlZQdE"],
}

monitorUrlList = user_list
