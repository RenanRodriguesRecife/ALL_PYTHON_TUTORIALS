from forex_python.converter import CurrencyRates

c = CurrencyRates()

#valor que vai ser convertido
v1 = float(input("\nQual o valor em dolar:"))

#coverte e formata o resultado
r = round(c.convert("USD","BRL",v1),2)

#mostra o resultado
print(f"${v1} = R$ {r}")