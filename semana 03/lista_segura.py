def adicionar_fruta(lista_frutas, fruta):
    nova_lista = lista_frutas.copy()
    nova_lista.append(fruta)

    return nova_lista


if __name__ == "__main__":
    frutas = ["maçã", "banana", "uva"]
    print(f"Lista original: {frutas}")

    continuar = "s"

    while continuar == "s":
        fruta_nova = input("Digite o nome da fruta: ")
        frutas = adicionar_fruta(frutas, fruta_nova)

        print(f"Lista atualizada: {frutas}")

        continuar = input("Deseja adicionar outra fruta? (s/n): ").lower()