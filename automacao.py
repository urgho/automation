#import pyautogui "as" auto << Determina um apelido ao comando pyautogui, mudando para auto ou outra coisa.
import pyautogui
import time

#Para não perder o controle da automação.
pyautogui.FAILSAFE = True

#Pausa geral de 0.3 segundos.
pyautogui.PAUSE = 0.3

#Delay para rodar o código.
time.sleep(5)

#Pegar posição do mouse.
"print(pyautogui.position())"

#Pegar a resolução da Tela.
"print(pyautogui.size())"

#Clicar com o mouse.
pyautogui.press("win")

time.sleep(3.5)
pyautogui.write("Chrome")
pyautogui.press("enter")

time.sleep(3.5)
pyautogui.click(x=204, y=63)

pyautogui.write("Senai Textil Bras", interval = 0.1)
pyautogui.press("enter")

time.sleep(2)
pyautogui.click(x=370, y=359)

#Clicar com o botão direito do mouse.
#pyautogui.click(x=370, y=359, button="right")
#pyautogui.rightClick(x=370, y=359)

#Double Clique
#pyautogui.click(x=370, y=359, click="2")

#Mover o Mouse
pyautogui.moveTo(x=682, y=228, duration = 0.5)

pyautogui.click(x=1204, y=316)

#Scrollar o site
#Rolar a página - nmr negativo = scroll para baixo
pyautogui.scroll(-1500)

pyautogui.moveTo(x=965, y=874, duration = 0.5)
pyautogui.click(x=965, y=874)

time.sleep(0.5)

pyautogui.moveTo(x=448, y=385, duration = 0.5)
pyautogui.click(x=448, y=385)

pyautogui.write("Superior de Tecnologia em Analise e Desenvolvimento de Sistemas", interval = 0.1)

#Funções do Teclado
pyautogui.press("enter")

pyautogui.moveTo(x=815, y=751)
pyautogui.click(x=815, y=751)

time.sleep(0.3)
pyautogui.leftClick(x=1235, y=864)

time.sleep(2)
pyautogui.scroll(-1700)

pyautogui.click(x=680, y=919)

time.sleep(1.5)
pyautogui.moveTo(x=953, y=689)
pyautogui.click(x=953, y=689)

pyautogui.moveTo(x=941, y=618, duration = 1.2)
pyautogui.click(x=941, y=618)