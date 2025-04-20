from abc import ABC, abstractmethod
class metodoPagamento (ABC):
    def __init__(self, valor, float):
        self.valor = valor
    @abstractmethod
    def pagar (self):
        pass

class CartaoCredito (metodoPagamento):
    def __init__(self, valor):
        super().__init__(valor)
    def pagar(self):
        return "Pagamento com taxa de 5% em cima do valor"
class Boletobancario (metodoPagamento):
    def __init__(self, valor):
        super().__init__(valor)
    def pagar(self):
        return "Pagamento com taxa de 2% em cima do valor"
class pix (metodoPagamento):
    def __init__(self, valor):
        super().__init__(valor)
    def pagar(self):
        return "Valor sem acrescimos ou descontos"