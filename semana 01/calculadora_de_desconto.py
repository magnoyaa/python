valor_produto = float(input("Digite o valor do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

valor_desconto = valor_produto * (percentual_desconto / 100)
valor_final = valor_produto - valor_desconto

print(f"O valor final é: {valor_final:.2f}")