import os

ARQUIVO = "itens.txt"

def adicionar():
    item = input('Digite o item: ').strip()

    if not item:
        print('Item não pode ficar vazio!')
        return
    
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(item + "\n")

    print('Item adicionado')

def listar():
    if not os.path.exists(ARQUIVO):
        print("Nenhum item encontrado!")
        return
    
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        itens = [linha.strip() for linha in arquivo if linha.strip()]

    if not itens:
        print('Nenhum item encontrado!')
        return

    for i, item in enumerate(itens, 1):
        print(f"{i} {item}")

def editar():
    listar()

    try:
        numero = int(input("Númmero do item: "))

        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            itens = [linha.strip() for linha in arquivo if linha.strip()]
            if numero < 1 or numero > len(itens):
                print('Número inválido!')
                return
            
            novo = input("Digite o novo nome: ").strip()

            if not novo:
                print("O nome não pode ficar vazio!")
                return

            itens[numero - 1] = novo

            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                arquivo.write("\n".join(itens) + "\n")

            print("Item adicionado!")

    except ValueError:
        print("Digite um nome válido!")

def excluir():
    listar()

    try:
        numero = int(input("Número do item: "))

        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            itens = [linha.strip() for linha in arquivo if linha.strip()]

        if numero < 1 or numero > len(itens):
            print("Número inválido!")
            return
        
        removido = itens.pop(numero - 1)

        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            arquivo.write("\n".join(itens) + ("\n" if itens else ""))

        print(f"Item {removido} excluído!")

    except ValueError:
        print("Digite um número válido!")

while True:
    print(f"\n========= CRUD =========")
    print("[1] - Adicionar")
    print("[2] - Listar")
    print("[3] - Editar")
    print("[4] - Excluir")
    print("[5] - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        editar()
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        print("Encerrando o sistema...")
        break
    else:
        print("Digite um valor válido!")