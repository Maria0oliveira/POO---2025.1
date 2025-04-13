from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, usuario, dataAbertura, saldo, tipoConta, limiteCredito):
        super().__init__(agencia, usuario, dataAbertura, saldo)
        self.tipoConta = tipoConta
        self.limiteCredito = limiteCredito

ContaCorrente = ContaCorrente()
print(ContaCorrente)