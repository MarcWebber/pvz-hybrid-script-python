from time import sleep

import pyautogui


def get_window():
    # 获取游戏句柄
    # qqlocation = pyautogui.locateOnScreen('qq.png')
    # print(qqlocation)
    pvz_hybrid_location = pyautogui.locateOnScreen("pvz_hybrid.png", confidence=0.9)
    x_start = pvz_hybrid_location[0]
    y_start = pvz_hybrid_location[1]
    print(x_start, y_start)
    # 获取pvz
    # while True:
    #     height, width  = pyautogui.size()
    #     print(height, width)
    #     sleep(1)


def press_key(key):
    pyautogui.press('space')


def get_mouse_position():
    return pyautogui.position()


def get_ground_info():
    # 获取场地信息，这里建议整合c++代码，直接获取游戏内存信息
    pass


def plant():
    pass


if __name__ == "__main__":
    # print(get_mouse_position())
    get_window()
    for i in range(100):
        press_key('space')
        sleep(1)
