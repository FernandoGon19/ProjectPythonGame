class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero  # número do paciente
        self.cor = cor  # cor do cartão (A ou V)
        self.proximo = None  # ponteiro para o próximo nodo (inicialmente None)


class ListaEncadeada:
    def __init__(self):
        self.head = None  # cabeça da lista (inicialmente vazia)
        self.contadorV = 0  # contador de pacientes "V"
        self.contadorA = 0  # contador de pacientes "A"

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            temp = self.head
            while temp.proximo:
                temp = temp.proximo
            temp.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            temp = self.head
            # Insere após todos os nodos com cor "A" e antes de "V"
            while temp.proximo and temp.proximo.cor == "A":
                temp = temp.proximo
            nodo.proximo = temp.proximo
            temp.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor (A ou V): ").upper()
        if cor not in ['A', 'V']:
            print("Cor inválida!")
            return

        if cor == 'A':
            self.contadorA += 1
            numero = self.contadorA
        else:
            self.contadorV += 1
            numero = self.contadorV

        nodo = Nodo(numero, cor)

        if not self.head:
            self.head = nodo
        elif cor == "V":
            self.inserirSemPrioridade(nodo)
        elif cor == "A":
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        if not self.head:
            print("A lista de espera está vazia!")
            return

        temp = self.head
        while temp:
            print(f"Paciente {temp.numero} - Cor: {temp.cor}")
            temp = temp.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Não há pacientes na fila.")
            return

        paciente_atendido = self.head
        self.head = self.head.proximo
        print(f"Paciente {paciente_atendido.numero} atendido.")

    def menu(self):
        while True:
            print("\n1 - Adicionar paciente a fila")
            print("2 - Mostrar pacientes na fila")
            print("3 - Chamar paciente")
            print("4 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.inserir()
            elif opcao == '2':
                self.imprimirListaEspera()
            elif opcao == '3':
                self.atenderPaciente()
            elif opcao == '4':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    lista_encadeada = ListaEncadeada()
    lista_encadeada.menu()
