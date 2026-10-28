programa
{
    funcao logico validar_senha(cadeia senha_correta, inteiro max_tentativas)
    {
        cadeia senha_digitada
        inteiro tentativas

        tentativas <- 0

        enquanto (tentativas < max_tentativas) {
            escreva("Digite a senha: ")
            leia(senha_digitada)
            tentativas <- tentativas + 1

            se (senha_digitada == senha_correta) {
                escreva("Senha correta! Você acertou em ", tentativas, " tentativa(s).")
                retorne verdadeiro
            } senao {
                escreva("Senha incorreta, tente novamente.\n")
            }
        }

        escreva("Você excedeu o número máximo de tentativas.")
        retorne falso
    }

    funcao inicio()
    {
        logico resultado

        resultado <- validar_senha("python123", 3)
    }
}