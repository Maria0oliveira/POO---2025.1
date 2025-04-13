from conta import Conta
from contaCorrente import ContaCorrente

class ContaEspecial(ContaCorrente):
    def __init__(self, agencia, usuario, dataAbertura, saldo, tipoConta, limiteCredito, limiteSaque):
        super().__init__(agencia, usuario, dataAbertura, saldo, tipoConta, limiteCredito)
        self.limiteSaque = limiteSaque

    def consultarSaldo(self):
        return super().consultarSaldo()
    def sacar (self):
        return super().sacar()
    def transferir (self):
        return super().transferir
   
ContaEspecial = ContaEspecial()
print(ContaEspecial)