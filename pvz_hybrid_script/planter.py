from time import sleep

import pyautogui

start_x, start_y = 0, 0
# 均以左上角为顶点
FIRST_CANNON_OFFSET_SIX_CHANNELS = [200,150]
CANNON_WIDTH_SIX_CHANNELS = 160
CANNON_HEIGHT_SIX_CHANNELS = 85

def get_cannon_position(channel, index):
    pass

# 六张场地 目前获得的基础数据如下：炮长160，行高85
# 200,150为基准点放炮
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

def cannon_shot():
    pass
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
    while True:
        print(get_mouse_position())
        sleep(1)
    # for i in range(100):
    #     press_key('space')
    #     sleep(1)
