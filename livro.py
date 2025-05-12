class Livro:
    def __init__(self, titulo, autor, ano_publicação, preço):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicação = ano_publicação
        self.preço = preço
    def informações_livro(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print (f"Ano de Publicação: {self.ano_publicação}")
        print(f"Preço: {self.preço}") 

primeiro_livro = Livro ('Mar Morto','Jorge Amado','1936','R$ 45,00')   
segundo_livro = Livro ('A Revolução do Bichos','Geoge Orwell', '1903', 'R$ 60,00')    

primeiro_livro.informações_livro()
segundo_livro.informações_livro()