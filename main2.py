from usuario import Usuario
from conta import Conta

usuario1 = Usuario()

rg = int (input("Digite o RG do usuário:"))
cpf = int (input("Digite o CPF do usuário:"))
nome = string (input("Digite o nome do usuário:"))
dia = int (input("Digite o dia o aniversário do usuário:"))
mes = int (input("Digite o mês do aniversário do usuário:"))
ano = int (input("Digite o ano do aniversário do usuário:"))

usuario1.set_rg(rg)
usuario1.set_cpf(cpf)
usuario1.set_nome(nome)
usuario1.set_dataNascimento(dia,mes,ano)

conta1 = Conta ("1025", 10/03/2025, 10,78)

print ("Informações da Conta:")
print (f"Conta:{conta1.get_agencia()}")
print (f"Usuario:{conta1.get_dataAbertura()}")
print (f"Saldo:{conta1.get_saldo()}")

print("\nInformações do Usuário:")
print (f"Nome:{usuario1.get_nome()}")
print (f"RG:{conta1.get_usuario().get_rg()}")
print (f"CPF:{conta1.get_usuario().get_cpf()}")
print (f"Data de Abertura: {conta1.get_usuario().get_dataNascimento()}")
print (f"Saldo:{conta1.get_usuario().get_saldo()}")



