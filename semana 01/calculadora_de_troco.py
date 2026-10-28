valor_pago = float(input("Digite o valor pago: "))
valor_produto = float(input("Digite o valor do produto: "))

troco = valor_pago - valor_produto

print(f"O troco é: {troco:.2f}")