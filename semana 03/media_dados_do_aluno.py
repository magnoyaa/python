def calcular_media(**dados):
    soma = sum(dados.values())
    media = soma / len(dados)

    return media


if __name__ == "__main__":
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
    nota_3 = float(input("Digite a terceira nota: "))

    media = calcular_media(nota_1=nota_1, nota_2=nota_2, nota_3=nota_3)

    print(f"A média é: {media:.2f}")