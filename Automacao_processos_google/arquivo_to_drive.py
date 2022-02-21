"""
pip install pyautogui
pyautogui
 - Biblioteca para controlar Mouse, Teclado e Tela do computador com Python
    link: https://pyautogui.readthedocs.io/en/latest/quickstart.html

 - Isso serve para: qualquer site, programa ou pasta do seu pc, qualquer Sistema que vc tenha acesso e automatizar
 
 
# * Desafio: Jogar uma pasta do pc para o google drive
  
  passo 1 - Abrir o google drive no meu pc
  passo 2 - Entrar na minha área de trabalho 
  passo 3 - Clicar no arquivo e arrastar
  passo 4 - entrar no google driver
  passo 5 - largar o arquivo no google driver
  passo 6 - Esperar 5 segundos

"""

import pyautogui
import time


print(pyautogui.KEYBOARD_KEYS)
pyautogui.alert('O código vai começar!')
pyautogui.PAUSE = 0.5   

# * passo 1 - Abrir o google drive no meu pc

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')


# * Entrar na area de trabalho
# win + d

pyautogui.hotkey('winleft', 'd')


# * pra ver a posição do mouse e saber onde clicar

print(pyautogui.position())  


# * pressiona o botao esquerdo do mouse esquerdo no arquivo da area de traablho e arrasta para o google drive

pyautogui.moveTo(1557, 282)  # Point(x=1557, y=282)
pyautogui.mouseDown()  # aperta o botam esquerdo do mouse
pyautogui.moveTo(890, 668)  # Point(x=890, y=668)


# * Enquanto arrasto o arquivo, mudar para o google drive

pyautogui.hotkey('alt', 'tab')
time.sleep(1)
 
# * Larguei o arquivo no google drive
pyautogui.mouseUp()

# * esperar 5 segundos
time.sleep(5)
pyautogui.alert('O código acabou! Pode usar seu pc novamente')