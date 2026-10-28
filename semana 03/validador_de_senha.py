def validar_senha(senha_correta, max_tentativas=3):
    tentativas = 0

    while tentativas < max_tentativas:
        senha_digitada = input("Digite a senha: ")
        tentativas += 1

        if senha_digitada == senha_correta:
            print(f"Senha correta! Você acertou em {tentativas} tentativa(s).")
            return True

        print("Senha incorreta, tente novamente.")

    print("Você excedeu o número máximo de tentativas.")
    return False


if __name__ == "__main__":
    validar_senha("python123")