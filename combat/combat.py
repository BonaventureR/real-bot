from utils import *
from matplotlib import pyplot as plt
import pyautogui as control

# Character Model, should be inheritable
class Character(object):
    def __init__(self, health=0, food=0):
        self.health = health
        self.food = food

    @property
    def health(self):
        return self._health

    @property
    def food(self):
        return self._food

    @health.setter
    def health(self, value):
        if 0 > value > 99:
            raise ValueError("Probably something wrong with the detection.")
            # try again
        else:
            self._health = value

    @food.setter
    def food(self, value):
        print("setting food")
        if 0 > value > 26:
            raise ValueError("Probably something wrong with the detection.")
            # try again
        else:
            self._food = value

    def __repr__(self):
        return "Health: {} , Food Left: {}".format(self.health, self.food)


# Vision on Screen that updates the current character
class Detector(object):
    def __init__(self, character, img=None):
        self.character = character
        self.image = img
        self.update_image()

    def update_image(self):
        self.img = screenshot()
        self.get_num_food()

    def get_num_food(self):
        self.character.food = check_inventory(self.img)
        return self.character.food

    def get_health(self):
        top_left, top_right, bottom_left, bottom_right = check_health(self.img)

        # TODO
        # use pytesseract to figure out the numbers

        # update health
        # self.health = ...

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, character):
        self._character = character

    def __repr__(self) -> str:
        return "{}".format(self.character)


# class CombatAssistant(object):
#     def __init__(self, detector):
#         self.detector = detector

#     # automates the clicking with the detector
#     def run():
#         ''' Run the bot '''
#         # TODO
#             # use the instance made to make the gui decisions

#         pass


if __name__ == "__main__":
    detector = Detector(Character())
    print(detector)

    # TODO
    # ... make a combat assistant class and pass in
    #     ... pass in the detector and do the gui work in this detector

    # img = screenshot()
    # top_left, top_right, bottom_left, bottom_right = check_health(img)
    # control.click(top_right[0], top_right[1],1,button='left')
