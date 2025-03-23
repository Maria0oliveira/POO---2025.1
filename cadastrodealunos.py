alunos = {
    "Francisco": [8.5, 7.0, 9.2, 6.8],
    "João": [5.5, 6.0, 7.5, 8.0],
    "Pedro": [9.0, 8.5, 10.0, 9.8],
    "Davi": [6.5, 7.2, 5.8, 6.9],
    "Paulo": [7.8, 8.2, 7.0, 8.5],
}
nome= (input("Digite o nome do aluno:"))
nota1 = float (input("Digite a primeira nota:"))
nota2 = float (input("Digite a segunda nota:"))
nota3 = float (input("Digite a terceira nota:"))
nota4 = float (input("Digite a quarta nota:"))
média = (nota1+nota2+nota3+nota4/4)
print(f"A média das 4 notas será:{média}")
print("\nLista de Alunos e Notas")
print (f"{nome}:{média}")
