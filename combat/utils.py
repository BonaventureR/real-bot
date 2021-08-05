import pyautogui as control
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def screenshot():
    """Take screenshot and return the grayscale image"""
    control.screenshot("curr_img/tmp.png")  # window 1
    img = cv.imread("curr_img/tmp.png", 0)
    return img


def check_health(img):
    """Check current health."""
    health_template = cv.imread("./templates/health.png", 0)
    return image_comparison(img, health_template)


# def check_inventory(img):
#     ''' check the inventory '''
#     inventory_template = cv.imread('./templates/inventory.png', 0)
#    top_left, top_right, bottom_left, bottom_right = check_inventory(img)
#    bag = img[top_left[1]:bottom_left[1], top_left[0]:top_right[0]]
#     return image_comparison(img, inventory_template)


def check_inventory(img):
    w, h = img.shape[::-1]
    threshold = 0.7
    num_food = 0

    # type of food
    for food_type in ["salmon", "lobster", "shark"]:
        if food_type == "shark":
            threshold = 0.65
        else:
            threshold = 0.7
        template_nm = cv.imread("./templates/{}.png".format(food_type), 0)
        res = cv.matchTemplate(img, template_nm, cv.TM_CCOEFF_NORMED)
        locations = np.where(res >= threshold)
        num_food += len(locations[0])

    return num_food


def image_comparison(img, template):
    """run template matching"""
    w, h = template.shape[::-1]

    res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv.minMaxLoc(res)

    # # top_left, top_right, bottom_left, bottom_right points
    return (
        (max_loc[0], max_loc[1]),
        (max_loc[0] + w, max_loc[1]),
        (max_loc[0], max_loc[1] + h),
        (max_loc[0] + w, max_loc[1] + h),
    )


def image_comparison_and_show(img, template):
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img, max_loc, bottom_right, 255, 5)
    plt.subplot(121), plt.imshow(res, cmap="gray")
    plt.title("Matching Result"), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap="gray")
    plt.title("Detected Point"), plt.xticks([]), plt.yticks([])
    plt.show()
