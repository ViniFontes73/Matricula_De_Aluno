#Grupo Vinicius Fontes 25388
# ler o arquivo de texto
print("Olá usuario, como você deseja filtrar: ")
print("Opção 1 = Matrícula")
print("Opção 2 = Nome")
print("Opção 3 = Curso")
infor = int(input("Digite o número da opção: "))

if infor == 1:
    num_mat = input("Digite o número da matrícula desejada: ")
    with open('C:\python\cadastro.txt', 'r')as arquivo:
        for linha in arquivo:
            for linha in arquivo:
                posicao_inicio = linha.find(f"{num_mat}")
                if posicao_inicio != -1:
                    restante_linha = linha[posicao_inicio:]
                    print("Sua busca resultou em:", restante_linha)
elif infor == 2:
    aluno = input("Digite o nome desejado: ").upper()
    with open('C:\python\cadastro.txt', 'r') as arquivo:
        for linha in arquivo:
            posicao_inicio = linha.find(f"{aluno}")
            if posicao_inicio != -1:
                posicao_fim = linha.find("\n", posicao_inicio)  # Encontra a posição do próximo caractere de nova linha
                linha_completa = linha[:posicao_fim]  # Seleciona a linha completa até a posição de nova linha
                print(f"Sua busca pelo nome {aluno}", linha_completa)
elif infor == 3:
    curso = input("Digite o curso ou o número: ")

    with open('C:\python\cadastro.txt', 'r') as arquivo:
        for linha in arquivo:
            posicao_inicio = linha.find(f"{curso}")
            if posicao_inicio != -1:
                posicao_fim = linha.find("\n", posicao_inicio)  # Encontra a posição do próximo caractere de nova linha
                linha_completa = linha[:posicao_fim]  # Seleciona a linha completa até a posição de nova linha
                print(f"Sua busca pelo curso:{curso} ", linha_completa)