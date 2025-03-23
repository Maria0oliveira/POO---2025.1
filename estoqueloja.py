#Estoque da loja
estoque = {
    "Arroz": 8,
    "Feijão": 10,
    "Farinha": 5,
    "Açucar": 7,
    "Café": 6,
    "Cuscuz":7,
}
    
produto = (input("Digite o nome do novo produto:"))
quantidade = int (input("Digite a quantidade nova:"))
if produto in estoque:
    estoque[produto]+= quantidade
else:
    estoque[produto] = quantidade
print ("\nEstoque atualizado:")
print (estoque)