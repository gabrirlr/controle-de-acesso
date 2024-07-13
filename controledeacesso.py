class ControleAcesso:
    def __init__(self, inicio_memoria, fim_memoria, tamanho_dados):
        self.inicio_memoria = 10
        self.fim_memoria = 1000
        self.tamanho_dados = 10
        self.banco_de_dados = []

    def inserir_cartao(self, cartao):
        if len(cartao) != self.tamanho_dados:
            print("Erro: Tamanho do cartão inválido.")
            return

        if len(self.banco_de_dados) >= (self.fim_memoria - self.inicio_memoria) // self.tamanho_dados:
            print("Erro: Memória cheia.")
            return

        if cartao in self.banco_de_dados:
            print("Erro: Cartão já existente.")
            return

        self.banco_de_dados.append(cartao)
        print("Cartão inserido com sucesso.")

    def consultar_cartoes(self):
        print("Cartões no banco de dados:")
        for cartao in self.banco_de_dados:
            print(cartao)

    def verificar_cartao(self, cartao):
        return cartao in self.banco_de_dados
