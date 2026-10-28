def calcular_troco(valor_pago, *precos):
    valor_produto = sum(precos)
    troco = valor_pago - valor_produto

    return troco


if __name__ == "__main__":
    valor_pago = float(input("Digite o valor pago: "))
    valor_produto = float(input("Digite o valor do produto: "))

    troco = calcular_troco(valor_pago, valor_produto)

    print(f"O troco é: {troco:.2f}")