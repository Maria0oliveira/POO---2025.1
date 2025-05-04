class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Matricula: {self.matricula}")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade):
        super().__init__(nome, idade)
        self.especialidade = especialidade

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Especialidade: {self.especialidade}")