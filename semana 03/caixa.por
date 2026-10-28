programa
{
    funcao real calcular_troco(real valor_pago, real valor_produto)
    {
        retorne valor_pago - valor_produto
    }

    funcao inicio()
    {
        real valor_pago
        real valor_produto
        real troco

        escreva("Digite o valor pago: ")
        leia(valor_pago)
        escreva("Digite o valor do produto: ")
        leia(valor_produto)

        troco <- calcular_troco(valor_pago, valor_produto)

        escreva("O troco é: ", troco)
    }
}