class Conta: 
    def __init__(self, agencia, usuario, dataAbertura, saldo):
        self.agencia = agencia
        self.usuario = usuario
        self.dataAbertura =  dataAbertura
        self.saldo = saldo
    
    def get_agencia(self):
        return self.agencia
    def set_agencia (self,agencia):
        self.agencia = agencia
    
    def get_usuario(self):
        return self.usuario
    def set_usuario (self, usuario):
        self.usuario = usuario
    
    def get_dataAbertura(self):
        return self.dataAbertura
    def set_dataAbertura (self, dataAbertura):
        self.dataAbertura

    def get_saldo(self):
        return self.saldo
    def set_saldo (self,saldo):
        self.saldo =saldo
    
    def __str__ (self):
        return (f"Agencia:{self.agencia}"
                f"Usuario:{self.usuario}"
                f"Data de Abertura:{self.dataAbertura}"
                f"Saldo:{self.saldo}")