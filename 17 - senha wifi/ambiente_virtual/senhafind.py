import subprocess

nome_wi_fi = "---" #nome da rede wifi

informacoes = subprocess.check_output(["netsh","wlan","show","profile",nome_wi_fi,"key","=","clear"],encoding='cp860')

print(informacoes)