programa
{
    funcao inicio()
    {
        cadeia frutas[10]
        cadeia fruta_nova
        cadeia continuar
        inteiro quantidade
        inteiro i

        frutas[0] <- "maçã"
        frutas[1] <- "banana"
        frutas[2] <- "uva"
        quantidade <- 3

        escreva("Lista original: ")
        para (i <- 0; i < quantidade; i++) {
            escreva(frutas[i], " ")
        }
        escreva("\n")

        continuar <- "s"

        enquanto (continuar == "s") {
            escreva("Digite o nome da fruta: ")
            leia(fruta_nova)

            frutas[quantidade] <- fruta_nova
            quantidade <- quantidade + 1

            escreva("Lista atualizada: ")
            para (i <- 0; i < quantidade; i++) {
                escreva(frutas[i], " ")
            }
            escreva("\n")

            escreva("Deseja adicionar outra fruta? (s/n): ")
            leia(continuar)
        }
    }
}