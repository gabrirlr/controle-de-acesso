class ControleAcessoRFID:
    def __init__(self):
        self.inicio_memoria = 100
        self.fim_memoria = 1000
        self.tamanho_cartao = 10
        self.memoria = {}

    def ler_cartao(self, numero_cartao):
        return self.memoria.get(numero_cartao, None)

    def verificar_cartao_existe(self, numero_cartao):
        return numero_cartao in self.memoria

    def deletar_memoria(self):
        self.memoria = {}

    def adicionar_cartao(self, numero_cartao):
        if self.verificar_cartao_existe(numero_cartao):
            print(f"O cartão {numero_cartao} já está na memória.")
        else:
            if len(self.memoria) < (self.fim_memoria - self.inicio_memoria) / self.tamanho_cartao:
                self.memoria[numero_cartao] = True
                print(f"Cartão {numero_cartao} adicionado com sucesso.")
            else:
                print("Memória cheia, não é possível adicionar mais cartões.")

# Função para interagir com o usuário via terminal
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
            print("Memória de cartões deletada.")

        elif escolha == '4':
            break

        else:
            print("Opção inválida. Escolha novamente.")

# Executar o menu principal
menu_principal()
