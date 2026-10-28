from caixa import calcular_troco
from calculadora import somar, subtrair, multiplicar, dividir
from conversor_de_temperatura import celsius_para_fahrenheit, celsius_para_kelvin
from lista_segura import adicionar_fruta
from media_dados_do_aluno import calcular_media
from validador_de_senha import validar_senha


if __name__ == "__main__":
    print("=== Calculadora de troco ===")
    troco = calcular_troco(50, 20)
    print(f"O troco é: {troco:.2f}")

    print("\n=== Calculadora ===")
    print(f"Soma: {somar(10, 5)}")
    print(f"Subtração: {subtrair(10, 5)}")
    print(f"Multiplicação: {multiplicar(10, 5)}")
    print(f"Divisão: {dividir(10, 5)}")

    print("\n=== Conversor de temperatura ===")
    print(f"25°C em Fahrenheit: {celsius_para_fahrenheit(25):.2f}°F")
    print(f"25°C em Kelvin: {celsius_para_kelvin(25):.2f}K")

    print("\n=== Lista segura ===")
    frutas = ["maçã", "banana", "uva"]
    frutas_atualizada = adicionar_fruta(frutas, "morango")
    print(f"Lista original: {frutas}")
    print(f"Lista atualizada: {frutas_atualizada}")

    print("\n=== Média de notas ===")
    media = calcular_media(nota_1=7, nota_2=8.5, nota_3=6)
    print(f"A média é: {media:.2f}")

    print("\n=== Validador de senha ===")
    validar_senha("python123")