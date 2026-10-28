def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_para_kelvin(celsius):
    return celsius + 273.15


if __name__ == "__main__":
    celsius = float(input("Digite a temperatura em Celsius: "))

    print("Escolha a conversão:")
    print("1 - Fahrenheit")
    print("2 - Kelvin")

    opcao = input("Digite o número da opção: ")

    match opcao:
        case "1":
            resultado = celsius_para_fahrenheit(celsius)
            print(f"{celsius}°C equivale a {resultado:.2f}°F")
        case "2":
            resultado = celsius_para_kelvin(celsius)
            print(f"{celsius}°C equivale a {resultado:.2f}K")
        case _:
            print("Opção inválida")