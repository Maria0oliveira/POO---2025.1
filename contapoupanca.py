from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, agencia, usuario, dataAbertura, saldo, extrato):
        super().__init__(agencia, usuario, dataAbertura, saldo)
        self.extrato = extrato

ContaPoupanca = ContaPoupanca()
print (ContaPoupanca)