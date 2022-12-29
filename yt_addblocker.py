import pyautogui
import time


def findAndClick():
    while True:
        videoAdCords = pyautogui.locateCenterOnScreen("./images/play.png", confidence=0.99, region=(1208, 0, 1585, 1079))
        bannerCords = pyautogui.locateCenterOnScreen("./images/bannerad.png", confidence=0.99, region=(931, 0, 1100, 1079))
        blackBannerCords = pyautogui.locateCenterOnScreen("./images/black banner.png", confidence=0.99, region=(931, 0, 1100, 1079))
        print(videoAdCords)
        print(bannerCords)
        print(blackBannerCords)

        if videoAdCords or bannerCords or blackBannerCords is not None:
            break

    if videoAdCords is not None:
        pyautogui.click(videoAdCords)
    elif bannerCords is not None:
        pyautogui.click(bannerCords)
    elif blackBannerCords is not None:
        pyautogui.click(blackBannerCords)

    time.sleep(1)
    findAndClick()


findAndClick()