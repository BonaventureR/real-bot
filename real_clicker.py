import numpy as np
import argparse
import pyautogui as mouse
import time
from timeit import default_timer as timer
from datetime import datetime


def autoclicker(
    duration, mouse_movement=25, camera_movement=100, sleep_time=500, start_time=timer()
):
    print("Start Time:", start_time)
    start_x, start_y = mouse.position()
    print(start_x, start_y)

    potential_cam_moves = ["left", "right", "up", "down"]
    j = k = 0
    x_coords = np.random.uniform(
        low=start_x - 3, high=start_x + 3, size=(mouse_movement, 1)
    )
    y_coords = np.random.uniform(
        low=start_y - 3, high=start_y + 3, size=(mouse_movement, 1)
    )
    pos = np.hstack((x_coords, y_coords))

    # 10,000 => 5 minutes
    for i in range(60000):
        if not (i % sleep_time) and i:
            now = datetime.now().strftime("%H:%M:%S")
            print('Taking Break. Time: ', now)
            print("Elapsed Time: ", (timer() - start_time)//60)
            time.sleep(30)  # sleep for 30 seconds
        if timer() - start_time > (60 * duration):
            break
        interval = np.random.uniform(0.1, 0.8)
        if not (i % mouse_movement):
            x, y = pos[(i + k) % mouse_movement]
            k += 1
            mouse.moveTo(x, y, duration=0.2)
        time.sleep(interval)
        mouse.click(x, y, clicks=1, button="left")
        if not (i % camera_movement):
            sample = potential_cam_moves[np.random.randint(0, 4)]
            mouse.press(sample, presses=np.random.randint(25, 100))
            j += 1

    time.sleep(15)
    # log out
    logout_x, logout_y = start_x - 70, start_y + 175
    mouse.click(logout_x, logout_y, duration=1)
    mouse.click(logout_x, logout_y - 55, duration=1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process n.")
    parser.add_argument("--n", type=int, help="set n minutes to go for")
    duration = parser.parse_args().n
    autoclicker(duration=duration)  # in minutes