class Usuario:
    def __init__(self, rg, cpf, nome, dataNascimento):
        self.rg = rg
        self.cpf = cpf
        self.nome = nome
        self.data = dataNascimento
        
    def get_rg(self):
        return self.rg
    def set_rg(self,rg):
        self.rg = rg

    def get_cpf(self):
        return self.cpf
    def set_cpf(self,cpf):
        self.cpf = cpf
    
    def get_nome(self):
        return self.nome
    def set_nome(self,nome):
        self.nome= nome
    
    def get_dataNascimento(self):
        return self.dataNascimento
    def set_dataNascimento(self,dataNascimento):
        self.dataNascimento = dataNascimento

    def __str__ (self):
        return (f"RG:{self.rg}"
               f"CPF:{self.cpf}"
               f"Nome:{self.nome}"
               f"Data de Nascimento:{self.dataNascimento.strftime('%d/%m/%Y')}")
            