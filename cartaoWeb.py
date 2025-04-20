from abc import ABC, abstractmethod
class CartaoWeb (ABC):
    def __init__(self, destinatario: str):
        self.destinatario = destinatario
    @abstractmethod
    def showMessage(self):
        pass

class DiadosNamorados (CartaoWeb):
    def __init__(self, destinatario:str):
        super().__init__(destinatario)
    def destinatario(self):
        return "Para: {nome}"
