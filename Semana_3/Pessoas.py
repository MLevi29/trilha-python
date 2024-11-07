import random

class Pessoa:
    def __init__(self, nome, nascimento, cpf):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        
        self.estado = "parado"
        self.voz = "calada"
        self._esport = "nenhum"
        self.comidafav = "nenhuma"

    # Estados
    def correr(self):
        self.estado = "correr"
        return print(f"A pessoa {self.nome} está {self.estado}.")
    
    def andar(self):
        self.estado = "andar"
        return print(f"A pessoa {self.nome} está {self.estado}.")
    
    def parar(self):
        self.estado = "parada"
        return print(f"A pessoa {self.nome} está {self.estado}.")
    
    def dormir(self):
        self.estado = "dormindo"
        return print(f"A pessoa {self.nome} está {self.estado}.")

    def acordar(self):
        self.estado = "acordada"
        return print(f"A pessoa {self.nome} está {self.estado}.")
    
    # Voz
    def falar(self):
        self.voz = "conversando"
        return print(f"A pessoa {self.nome} está {self.voz}.")
    
    def calar(self):
        self.voz = "calada"
        return print(f"A pessoa {self.nome} está {self.voz}.")

    # Atividades
    def esporte(self, modalidade):
        self._esport = modalidade
        return print(f"Agora, a pessoa {self.nome} pratica {self._esport}.")

    # Comida favorita
    def fav_comida(self, alim):
        self.comidafav = alim
        return print(f"A comida preferida de {self.nome} é {self.comidafav}.")
    

class Mae(Pessoa):
    def __init__(self, nome, nascimento, cpf):
        super().__init__(nome, nascimento, cpf)

    def procurar(self, objeto):
        escolha = input(f"Como mãe, {self.nome} consegue encontrar qualquer objeto perdido, inclusive {objeto}. Mas, se ela encontar, ela irá esfregar na sua cara. Deseja que ela encontre?\n1. Sim\n2.Não\nEscolha: ")
        
        while (escolha != 1) or (escolha != 2):
            if escolha == 1:
                return print("Ela encontrou e esfregou na sua cara. Coloque no devido lugar da próxima vez.")
            
            elif escolha == 2:
                return print("Ela gostou que você decidiu procurar melhor.")
            
            else:
                return print("Escolha uma das respostas. Ela não gosta de tomar vácuo.")


class Irma(Pessoa):
    def __init__(self, nome, nascimento, cpf):
        super().__init__(nome, nascimento, cpf)

    def desleixo(self):
        objetos = ['brinco', 'colar', 'maquiagem', 'casca de banana', 'prato usado', 'fio dental', 'sua roupa que ela usou sem pedir']
        ob = random.randint(0, len(objetos)-1)
        return print(f"Sua irmã acabou de deixar {objetos[ob]} jogado em qualquer lugar da casa, menos no seu devido lugar.")
    

class Professor(Pessoa):
    def __init__(self, nome, nascimento, cpf, materia):
        super().__init__(nome, nascimento, cpf)
        self._materia = materia
        self.desist = "Não"

    def assunto(self):
        return print(f"Seu(sua) professor(a) da aulas de {self._materia}.")

    def desistir(self):
        self.desist = "Sim"
        return print(f"O(A) professor(a) {self.nome} não aguentou as condições monstruosas das salas de aula brasileiras e desistiu. Agora, sua nova missão é encontrar um novo emprego.")


class Prof_Jiujitsu(Professor):
    def __init__(self, nome, nascimento, cpf, materia):
        super().__init__(nome, nascimento, cpf, materia)
        self._materia = "Jiu jitsu"
        self._esport = "Jiu jitsu"

    def esporte(self):
        self._esport = 'Jiu jitsu'
        return print("Seu(sua) professor(a) pratica Jiujitsu e nada mais.")


if __name__ == '__main__':

    diego = Prof_Jiujitsu('Diego Pacheco', '05/10/1973', '12345678910', 'Culinária')
    diego.assunto()
    diego.esporte()

    julia = Irma('Julia', '01/08/1990', '01987654321')
    julia.desleixo()