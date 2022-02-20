import pyautogui
import time


# print(pyautogui.KEYBOARD_KEYS)
pyautogui.alert('O código vai começar!')
# pyautogui.PAUSE = 0.5   

# * passo 1 - Abrir o google e o site

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://redeglobo.globo.com/sp/tvdiario/programacao/#202202151')
pyautogui.press('enter')


time.sleep(2)
# pyautogui.alert('O código acabou! Pode usar seu pc novamente')