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
        self.dataAbertura = dataAbertura

    def get_saldo(self):
        return self.saldo
    def set_saldo (self,saldo):
        self.saldo =saldo
    
    def consultarSaldo(self):
        return self.consultarSaldo
    
    def get_depositar(self):
        return self.depositar 
    def set_depositar (self, depositar):
        self.depositar = depositar
    
    def get_sacar(self):
        return self.sacar 
    def set_sacar (self, sacar):
        self.sacar = sacar
    
    def get_transferir(self):
        return self.transferir
    def set_transferir (self, transferir):
        self.transferir = transferir
        
    def __str__ (self):
        return (f"Agencia:{self.agencia}"
                f"Usuario:{self.usuario}"
                f"Data de Abertura:{self.dataAbertura}"
                f"Saldo:{self.saldo}")