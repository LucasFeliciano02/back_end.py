import pyautogui
import time


# print(pyautogui.KEYBOARD_KEYS)
pyautogui.alert('O código vai começar!')
# pyautogui.PAUSE = 0.5

# * passo 1 - Abrir o youtube

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://www.youtube.com/')
pyautogui.press('enter')


time.sleep(2)
# pyautogui.alert('O código acabou! Pode usar seu pc novamente')

# print(pyautogui.position())
