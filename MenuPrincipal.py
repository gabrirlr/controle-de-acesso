from controledeacesso import ControleAcessoRFID4
def menu_principal():
    controle_acesso = ControleAcessoRFID()

    while True:
        print("\n--- Controle de Acesso RFID ---")
        print("1. Verificar cartão")
        print("2. Adicionar cartão")
        print("3. Deletar memória")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            numero_cartao = input("Digite o número do cartão a ser verificado: ")
            if controle_acesso.verificar_cartao_existe(numero_cartao):
                print("Acesso permitido.")
            else:
                print("Acesso não permitido.")

        elif escolha == '2':
            numero_cartao = input("Digite o número do cartão a ser adicionado: ")
            controle_acesso.adicionar_cartao(numero_cartao)

        elif escolha == '3':
            controle_acesso.deletar_memoria()

        elif escolha == '4':
            break

        else:
            print("Opção inválida. Escolha novamente.")

    controle_acesso.salvar_memoria()  # Salvar novamente ao sair do programa

# Executar o menu principal
menu_principal()