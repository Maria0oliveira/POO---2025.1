class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
    
primeiro_carro = Carro ('Fiat', 'Uno', '1990','verde')
segundo_carro = Carro ('Chevrolet', 'Celta', '2001', 'preto')

primeiro_carro.exibir_informacoes()
segundo_carro.exibir_informacoes()