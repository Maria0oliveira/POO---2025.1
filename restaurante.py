class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha):
        nomeRestaurante (self):
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha

    def descreverRestaurante(self):
        descricao = (f"Restaurante:{self.nomeRestaurante}")
                    (f"TipodeCozinha:{self.tipoCozinnha}")
        print (descricao)
    def abriRestaurante(self):
    print (f"O Restaurante {self.nomeRestaurante} de cozinha {self.tipoCozinha} está aberto agora!")

    def __str__ (self):
        return (f"Nome:{self.nomeRestaurante}"
                f"Tipo:{self.tipoCozinha}")
