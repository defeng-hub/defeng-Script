import time
import webbrowser
from douyin_user_info import getUserName, getSec_uid
from douyin_videos import getUserFirstVideo, getUserFirstVideoAndName, playAudio
from init import douyinheaders, monitorUrlList, monitorUser
from conf import wait_time, open_browser


# 初始化监听对象
def initMonitor():
    log()
    # 初始化
    for i in range(len(monitorUrlList)):
        url = monitorUrlList[i]
        if url is not None and url != "":
            secuid = getSec_uid(url)
            vid, name = getUserFirstVideoAndName(secuid, douyinheaders)
            if name != "" and secuid != "":
                monitorUser[url] = [name, secuid, vid]
            else:
                print("{}：".format(url), "地址无法使用, 已跳过。")

    for k in monitorUser:
        print(k + "：", monitorUser[k][0])
    print("=====初始化完成, 监听数量：{}条=====".format(len(monitorUser)))


def runMonitor():
    while True:
        print("=====持续监测中....=====")
        for url in monitorUser:
            obj = monitorUser[url]
            name, secuid, yvid = obj[0], obj[1], obj[2]
            time.sleep(1)
            hvid = getUserFirstVideo(secuid, douyinheaders)
            if hvid == "":
                print("<此条信息如果连续出现多次，那么该更换 conf.py文件中的douyin_ck参数>")
                continue

            if yvid != hvid:
                if open_browser == 1:
                    webbrowser.open(url)

                # 更新为后来的vid
                monitorUser[url][2] = hvid
                print("{}：更新了视频 {}".format(name, url))
                playAudio("./mp3/quick.mp3")
            else:
                continue
        time.sleep(wait_time)


def log():
    print("========开始初始化....=========")

    if open_browser == 1:
        print("是否开启浏览器：是")
    else:
        print("是否开启浏览器：否")
    print("每一轮的间隔时间(秒)：{}".format(wait_time))


if __name__ == '__main__':
    # https://m.douyin.com/share/user/MS4wLjABAAAAZKLBIA9UKpovpOyowaKJWJDYu_vMjmVrQmmaZfKCJ1Y
    initMonitor()
    runMonitor()
