senha_correta = "python123"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha_digitada = input("Digite a senha: ")
    tentativas += 1

    if senha_digitada == senha_correta:
        print(f"Senha correta! Você acertou em {tentativas} tentativa(s).")
        break

    print("Senha incorreta, tente novamente.")
else:
    print("Você excedeu o número máximo de tentativas.")