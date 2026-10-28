programa
{
    funcao inteiro somar(inteiro a, inteiro b)
    {
        retorne a + b
    }

    funcao inteiro subtrair(inteiro a, inteiro b)
    {
        retorne a - b
    }

    funcao inteiro multiplicar(inteiro a, inteiro b)
    {
        retorne a * b
    }

    funcao vazio dividir(inteiro a, inteiro b)
    {
        se (b == 0) {
            escreva("Divisão: None")
        } senao {
            escreva("Divisão: ", a / b)
        }
    }

    funcao inicio()
    {
        inteiro numero_1
        inteiro numero_2

        escreva("Digite o primeiro número: ")
        leia(numero_1)
        escreva("Digite o segundo número: ")
        leia(numero_2)

        escreva("Soma: ", somar(numero_1, numero_2), "\n")
        escreva("Subtração: ", subtrair(numero_1, numero_2), "\n")
        escreva("Multiplicação: ", multiplicar(numero_1, numero_2), "\n")
        dividir(numero_1, numero_2)
    }
}