import time
import webbrowser
from douyin_user_info import getUserName, getSec_uid
from douyin_videos import getUserFirstVideo, getUserFirstVideoAndName, playAudio
from init import douyinheaders, monitorUrlList, monitorUser


# 初始化监听对象
def initMonitor():
    # 初始化
    for i in range(len(monitorUrlList)):
        url = monitorUrlList[i]
        if url is not None and url != "":
            secuid = getSec_uid(url)
            vid, name = getUserFirstVideoAndName(secuid, douyinheaders)
            if name != "" and secuid != "":
                monitorUser[url] = [name, secuid, vid]

    print("=====初始化开始=====")
    for k in monitorUser:
        print(k, monitorUser[k])
    print("=====初始化完成=====")


def runMonitor():
    while True:
        print("=====持续监测中....=====")
        for url in monitorUser:
            obj = monitorUser[url]
            name, secuid, yvid = obj[0], obj[1], obj[2]
            time.sleep(1)
            hvid = getUserFirstVideo(secuid, douyinheaders)
            if yvid != hvid:
                # 打开浏览器
                webbrowser.open(url)
                print("更新了视频", name, url)
                playAudio("./mp3/quick.mp3")
            else:
                continue
        time.sleep(20)


if __name__ == '__main__':
    # https://m.douyin.com/share/user/MS4wLjABAAAAZKLBIA9UKpovpOyowaKJWJDYu_vMjmVrQmmaZfKCJ1Y
    initMonitor()
    runMonitor()
