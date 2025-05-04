def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
        return linhas
    except FileNotFoundError:
        print(f"Erro: Arquivo {nome_arquivo} não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo {nome_arquivo}: {e}")
        return []

def carregar_alunos():
    linhas = ler_arquivo('alunos.txt')
    alunos = []
    for linha in linhas:
        try:
            # Supondo que cada linha seja: nome;idade;matricula
            dados = linha.strip().split(';')
            if len(dados) == 3:
                nome, idade, matricula = dados
                aluno = Aluno(nome, int(idade), matricula)
                alunos.append(aluno)
            else:
                print(f"Dados inválidos na linha: {linha}")
        except Exception as e:
            print(f"Erro ao processar linha de aluno: {linha}. Erro: {e}")
    return alunos

def carregar_professores():
    linhas = ler_arquivo('professores.txt')
    professores = []
    for linha in linhas:
        try:
            # Supondo que cada linha seja: nome;especialidade;salario
            dados = linha.strip().split(';')
            if len(dados) == 3:
                nome, especialidade, salario = dados
                professor = Professor(nome, especialidade, float(salario))
                professores.append(professor)
            else:
                print(f"Dados inválidos na linha: {linha}")
        except Exception as e:
            print(f"Erro ao processar linha de professor: {linha}. Erro: {e}")
    return professores

