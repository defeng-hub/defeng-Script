import requests
from playsound import playsound


# from xihai.init import douyinheaders, sec_uid


def getUserFirstVideo(sec_uid, douyinheaders):
    try:
        url = "https://m.douyin.com/web/api/v2/aweme/post/?reflow_source=reflow_page&sec_uid={}&count=21".format(
            sec_uid)
        res1 = requests.get(url=url, headers=douyinheaders)
        # print(res1.json())
        # 最新视频的id
        aweme_id = res1.json()["aweme_list"][0]["aweme_id"]
        return aweme_id
    except:
        return ""


def getUserFirstVideoAndName(sec_uid, douyinheaders):
    try:
        url = "https://m.douyin.com/web/api/v2/aweme/post/?reflow_source=reflow_page&sec_uid={}&count=21".format(
            sec_uid)
        res1 = requests.get(url=url, headers=douyinheaders)

        # 最新视频的id
        aweme_id = res1.json()["aweme_list"][0]["aweme_id"]
        author = res1.json()["aweme_list"][0]["author"]["nickname"]
        return aweme_id, author
    except:
        return "", ""


def playAudio(path):
    playsound(path)
    pass
