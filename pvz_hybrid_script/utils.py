# 定义六行场地所有格子的坐标
import time

from pvz_hybrid_script.planter import FIRST_CANNON_OFFSET_SIX_CHANNELS
from pvz_hybrid_script.constants import AREA
import pyautogui
pyautogui.PAUSE = 0.00


def init_grids_six():
    pass


# 定义五行场地所有格子的坐标
def init_grids_five():
    pass


# 设置六行场地玉米加农炮的发射点
def init_cannons_six():
    for line in range(6):
        pass
        # for colum in range(9):
        #     x = con
        #     print(x, y)
    pass


def cannon_shot(cannon_x, cannon_y, target_x, target_y):
    # 释放鼠标
    cannon_x, cannon_y = cannons[(cannon_y - 1) * 9 + cannon_x - 1]

    pyautogui.click(cannon_x, cannon_y)
    pyautogui.click(target_x, target_y)


def init_cannons_five():
    x_offset = 105
    y_offset = 165
    cannon_positions = []
    for line in range(5):
        for column in range(9):
            y = y_offset + line * AREA['HEIGHT_FIVE_LINES']
            x = x_offset + column * AREA['WIDTH']
            cannon_positions.append((x, y))
    return cannon_positions


if __name__ == "__main__":
    # init_cannons_six()
    # init_grids_five()
    cannons = init_cannons_five()
    step = 2
    # cannon_shot(5, 1,500,500)
    # current time
    start_time = time.time()
    for i in range(1, 6):
        for j in range(1, 10, 2):
            cannon_shot(j, i, 800, 500)

    end_time = time.time()
    print("Time used: ", end_time - start_time)