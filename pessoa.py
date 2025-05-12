class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def apresentar(self):
        print (f"Olá, meu nome é {self.nome}, tenho {self.idade}, e moro em {self.cidade}")
    
primeira_pessoa = Pessoa ('Helena', '32', 'Fortaleza')
segunda_pessoa = Pessoa ('Horlanda', '45', 'Maracanaú')

primeira_pessoa.apresentar()
segunda_pessoa.apresentar()