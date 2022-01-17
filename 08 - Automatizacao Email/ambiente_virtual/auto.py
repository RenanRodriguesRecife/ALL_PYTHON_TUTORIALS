# 1 - entrar no sistema da empresa (no caso o link do drive)
# 2 - navegar no sistema (até a pasta exportar)
# 3 - fazer o download da base de vendas
# 4 - Inportar a base de vendas pro Python
# 5 - Calcular o faturamente e a quantidade de produtos vendidos (os indicadores)
# 6 - Enviar o email para a diretoria

import pyautogui
import pyperclip
# import webbrowser

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
pyautogui.write('http//drive.google.com/drive/folders/149xknr93vrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.press("enter")