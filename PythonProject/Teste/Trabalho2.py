# Nodo para representar cada estado
class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

# Tabela Hash com encadeamento
class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho  # Inicializa a tabela com 10 posições

    # Função hash
    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7  # Para o Distrito Federal, a posição será 7
        else:
            # Calcula a posição com base nos valores ASCII das letras da sigla
            ascii1 = ord(sigla[0])
            ascii2 = ord(sigla[1])
            return (ascii1 + ascii2) % self.tamanho  # A posição é o módulo da soma dos ASCII

    # Inserção na tabela (no início da lista encadeada)
    def inserir(self, sigla, nomeEstado):
        pos = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla, nomeEstado)
        # Inserção no início da lista encadeada (cabeça da lista)
        novo_nodo.proximo = self.tabela[pos]
        self.tabela[pos] = novo_nodo

    # Impressão da tabela hash
    def imprimir(self):
        for i in range(self.tamanho):
            print(f"Posição {i}: ", end="")
            atual = self.tabela[i]
            while atual:
                print(f"{atual.sigla} ", end="-> ")
                atual = atual.proximo
            print("None")


# Função principal para inserir todos os estados e o Distrito Federal
def main():
    tabela = TabelaHash()

    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
        ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
        ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
        ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
        ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
    ]

    for sigla, nome in estados:
        tabela.inserir(sigla, nome)

    tabela.inserir("FP", "Fernando Gonçalves Prudente")
    tabela.imprimir()

# Executa o programa principal
if __name__ == "__main__":
    main()
