# 1 - entrar no sistema da empresa (no caso o link do drive)
# 2 - navegar no sistema (até a pasta exportar)
# 3 - fazer o download da base de vendas
# 4 - Inportar a base de vendas pro Python
# 5 - Calcular o faturamente e a quantidade de produtos vendidos (os indicadores)
# 6 - Enviar o email para a diretoria

import pyautogui
import pyperclip
# import webbrowser
import time

#tempo de PAUSA entre um comando e outro
pyautogui.PAUSE = 1

# 1 - entrar no sistema da empresa (no caso o link do drive)

# alguns comandos
# aperta uma tecla do teclado - pyautogui.press("c")
# clica com o mouse - pyautogui.click()
# combinação de teclas - pyautogui.hotkey("ctrl","c")
# escrever - pyautogui.write("qualquer coisa")

# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# webbrowser.get(chrome_path).open("http://docs.python.org/")

#abre uma nova no navegador:
pyautogui.hotkey("ctrl","t")
#pyperclip trabalha com textos com caracteres especiais
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing') #copiando um link
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")

#esperar 5 segundos para dar tempo para tudo carregar
time.sleep(5)

#Macete para pegar o valor da posicao do mouse
#time.sleep(5)
#pyautgui.position()

#2 - clicar na pasta do drive
pyautogui.click(x=974,y=676,clicks=2)
time.sleep(2)

#3 - fazer download
pyautogui.click(x=922,y=828) #clica no arguivo
pyautogui.click(x=3339, y=404) #clica nos 3 pontos
pyautogui.click(x=2890, y=1406) #clica em fazer download

time.sleep(5) #esperar o download


#importar a base de vendas pro python
import pandas as pd
import display

tabela = pd.read_excel(r"C:\Users\z400\Downloads\Vendas - Dez.xlsx")
display(tabela)

#5 - calcular o faturamento e a quantidade de produtos vendidos
faturamento = tabela["Valor Final"].sum()
qtde_produtos = tabela["Quantidade"].sum()