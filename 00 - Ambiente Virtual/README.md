Criar um ambiente virsual (instalando python da maneira correta)

Dá a possibilidade de ter uma cópia do python em quantas pasta você quiser

- Isso evita problemas de conflistos de versões e depencias de pacotes.
- Facilita a remoção de pacotes.


OBS: Você vai precisar ter uma vensão recente do python instalado (acima da versão 3.5). Pq já está incorporado o virtualenv.

1 - No terminal navegue até a pasta que você deseja criar o ambiente virtual

2 - 
    Para windows:
    <code>py -m venv nome_que_você_quer_colocar</code>
    Para Linux:
    <code>python3 -m venv nome_que_você_quer_colocar</code>