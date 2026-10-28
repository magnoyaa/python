numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a operação desejada: ")

match opcao:
    case "1":
        resultado = numero_1 + numero_2
    case "2":
        resultado = numero_1 - numero_2
    case "3":
        resultado = numero_1 * numero_2
    case "4":
        resultado = numero_1 / numero_2
    case _:
        resultado = "Opção inválida"

print(f"Resultado: {resultado}")