def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None
    return a / b


if __name__ == "__main__":
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))

    print(f"Soma: {somar(numero_1, numero_2)}")
    print(f"Subtração: {subtrair(numero_1, numero_2)}")
    print(f"Multiplicação: {multiplicar(numero_1, numero_2)}")
    print(f"Divisão: {dividir(numero_1, numero_2)}")