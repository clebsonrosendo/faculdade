import datetime
import pyautogui



datetime = str(datetime.datetime.now())
position = str(pyautogui.position())

with open("log.txt", "a") as file:
    file.write("\n" + datetime + " " + position)

