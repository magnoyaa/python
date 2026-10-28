numeros = []
ordinais = ["primeiro", "segundo", "terceiro", "quarto", "quinto"]

for i in range(5):
    numero = float(input(f"Digite o {ordinais[i]} valor: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma / 5
maior = max(numeros)
menor = min(numeros)

print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")