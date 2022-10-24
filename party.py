import pyautogui
import time

pyautogui.PAUSE = 0.01

input = "/Users/dylank/rick.txt"
file = open(input)
string = file.read()
arr = string.split()
print(arr)

time.sleep(5)

for x in arr:
    print(x)
    pyautogui.write(x)
    pyautogui.press('return')

