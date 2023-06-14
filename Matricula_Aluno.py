#Prova 2
#Nome Vinicius Fontes 25388
# Função para obter o valor atual do contador de matrícula
def obter_contador():
    try:
        with open('C:\python\contador.txt', 'r') as arquivo:
            contador = int(arquivo.read())
    except FileNotFoundError:
        contador = 1
    return contador

# Função para atualizar o valor do contador no arquivo
def atualizar_contador(contador):
    with open('C:\python\contador.txt', 'w') as arquivo:
        arquivo.write(str(contador))

def obter_dados_pessoais():
    contador_matricula = obter_contador()  # Obtendo o valor atual do contador

    matricula = contador_matricula
    contador_matricula += 1


    nome = input("Digite seu nome completo: ").upper()
    sexo = input("Digite o seu sexo: 'Masculino', 'Feminino', 'Outro': ").upper()
    endereco = input("Logradouro: ").upper()
    endereco1 = input("Número da sua casa: ").upper()
    endereco2 = input("Complemento: ").upper()
    endereco3 = input("Bairro: ").upper()
    endereco4 = input("CEP: ").upper()
    endereco5 = input("Cidade: ").upper()
    contato = input("Telefone para contato: ")
    email = input("Digite seu email: ")

    while sexo not in ["MASCULINO", "FEMININO","OUTRO"]:
        sexo = input("Digite o seu sexo: 'Masculino', 'M', 'Feminino', 'F', 'Outro': ").upper()

# Atualizando o valor do contador no arquivo
    atualizar_contador(contador_matricula)
    dados = {
        "matricula": matricula,  # Adicionando a matrícula aos dados pessoais
        "nome": nome,
        "sexo": sexo,
        "endereco": endereco,
        "endereco1": endereco1,
        "endereco2": endereco2,
        "endereco3": endereco3,
        "endereco4": endereco4,
        "endereco5": endereco5,
        "contato": contato,
        "email": email
    }
    return dados


def obter_opcao():
    print("Selecione uma curso:")
    print("1.0 Inglês")
    print("1.1 Inglês e Francês")
    print("1.2 Inglês e Espanhol")
    print("1.3 Inglês, Francês e Espanhol")
    print("2.0 Francês")
    print("2.1 Francês e Inglês")
    print("2.2 Francês e Espanhol")
    print("2.3 Francês, Inglês e Espanhol")
    print("3.0 Espanhol")
    print("3.1 Espanhol e Inglês")
    print("3.2 Espanhol e Francês")
    print("3.3 Espanhol , Inglês e Francês")
    while True:
        opcao = input("Digite o número da opção escolhida: ")
        if opcao == "1.0":
            return "Inglês 1.0"
        elif opcao == "1.1":
            return "Inglês e Francês 1.1"
        elif opcao == "1.2":
            return "Inglês e Espanhol 1.2"
        elif opcao =="1.3":
            return "Inglês, Françês e Espanhol 1.3"
        elif opcao == "2.0":
            return "Françês 2.0"
        elif opcao == "2.1":
            return "Francês e Inglês 2.1"
        elif opcao == "2.2":
            return "Francês e Espanhol 2.2"
        elif opcao == "2.3":
            return "Francês, Inglês e Espanhol 2.3"
        elif opcao == "3.0":
            return "Espanhol 3.0"
        elif opcao == "3.1":
            return "Espanhol e Inglês 3.1"
        elif opcao == "3.2":
            return "Espanhol e Francês 3.2"
        elif opcao == "3.3":
            return "Espanhol, Inglês e Francês 3.3"
        else:
            print("Opção inválida. Digite um número válido.")




dados_pessoais = obter_dados_pessoais()
opcao_selecionada = obter_opcao()
print("Opção selecionada:", opcao_selecionada)


# Gravar os dados em um arquivo de texto
with open('C:\python\cadastro.txt', "a") as arquivo:
   arquivo.write(str(dados_pessoais) )
   arquivo.write(str(opcao_selecionada + "\n"))
