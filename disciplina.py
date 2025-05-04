class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def exibir_dados(self):
        print(f"Disciplina: {self.nome}")
        print(f"Código: {self.codigo}")