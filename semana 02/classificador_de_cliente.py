idade_cliente = int(input("Digite sua idade: "))
renda_cliente = float(input("Digite sua renda: "))

if renda_cliente >= 100 and renda_cliente <= 500:
    classificacao = "bronze"
elif renda_cliente >= 501 and renda_cliente <= 1000:
    classificacao = "prata"
elif renda_cliente >= 1001 and renda_cliente <= 1500:
    classificacao = "ouro"
else:
    classificacao = "diamante"

print(f"Sua idade é: {idade_cliente}, você é um cliente {classificacao}!")