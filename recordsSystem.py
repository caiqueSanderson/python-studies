def menu():
  """ 
  Esta função imprime as escolhas possíveis para o usuário e retorna a escolha
  :return: O número referente a opção escolhida
  """
  
  print(f"\n----- Seja bem-vindo ----- \n")
  print(" Insira 1 para criar um registro \n Insira 2 para consultar um registro pelo ID \n Insira 3 para listar os registros \n Insira 4 modificar um registro \n Insira 5 para apagar um registro \n Insira 6 para sair")
  escolha = int(input("Opção desejada: "))
  if escolha >= 1 and escolha <= 6:
    return escolha
  else:
    print("Escolha inválida!")


def nome_completo():
  """ 
  Esta função solicita o nome completo do usuário e capitaliza cada palavra
  :return: Nome completo do usuario no formato capitalize
  """
  nome = input("Insira seu nome completo: ")
  nome_completo_formatado = nome.title()
  return nome_completo_formatado

def data_nascimento():
  """ 
  Esta função solicita a data de nascimente e verifica se é uma data válida
  :return: Se for válida retorna a data formatada, se for inválida retorna False
  """
  data = input("Insira sua data de nascimento(ddmmaaaa): ")

  dia = int(data[0] + data[1])
  mes = int(data[2] + data[3])
  ano = int(data[4] + data[5] + data[6] + data[7])

  if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    dias_por_mes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  else:
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  if 1 <= mes <= 12 and 1 <= dia <= dias_por_mes[mes]:
    data_formatada = f"{dia:02d}-{mes:02d}-{ano:04d}"
    return data_formatada
  else:
    return False
  
def valida_cpf(cpf):
  """
  Esta função recebe o cpf como parametro e válida o cpf
  :param cpf: CPF formato XXXXXXXXXXX
  :return: Se o cpf for válido retorna True, se for inválido False
  """
  cpf_str = str(cpf)
  if len(cpf_str) != 11:
    return False

  elif len(cpf_str) == 11:
    cpf_lista_inteiros = [int(char) for char in cpf_str]
    if len(set(cpf_lista_inteiros)) == 1:
      return False
    else:
      soma = sum([(cpf_lista_inteiros[i] * (10 - i)) for i in range(9)])
      resto = (soma * 10) % 11
      if resto == cpf_lista_inteiros[9]:
        soma = sum([(cpf_lista_inteiros[i] * (11 - i)) for i in range(10)])
        resto = (soma * 10) % 11
        if resto == cpf_lista_inteiros[10]:
          return True
      else:
        return False
      
def solicita_cpf():
  """
  Esta função solicita o CPF e se for válido devolve no formato XXX.XXX.XXX-XX
  :return: Se for válido retorna CPF formatado, se for inválido retorna False
  """
  cpf = input("Insira seu cpf: ")
  if valida_cpf(cpf) == True:
    cpf_str = str(cpf)
    cpf_formatado = "{}.{}.{}-{}".format(cpf_str[:3], cpf_str[3:6], cpf_str[6:9], cpf_str[9:])
    return cpf_formatado
  else:
    return False
  
def valida_email():
  """
  Esta função válida o email verificando se tem "@" e "."
  :return: Se for válido retorna o e-mail, se for inválido retorna False
  """
  email = input("Insira seu e-mail: ")
  if "@" in email and "." in email:
    return email
  else:
    return False

def solicita_dados_cadastrais():
  """
  Esta função cria um registro usando as funções posteriormente criadas para solicitar e validar algum dos dados do usuário,separadamente
  :return: Retorna todos os dados do usuário dentro de uma lista
  """
  while True:
    print("\n----- Criar Registro -----\n")
    nome = nome_completo()
    if not nome:
      print("Nome inválido, tente novamente")
      continue
    data_de_nascimento = data_nascimento()
    if not data_de_nascimento:
      print("Data de nascimento inválida, tente novamente")
      continue
    cpf = solicita_cpf()
    if not cpf:
      print("CPF inválido")
      continue
    email = valida_email()
    if not email:
      print("E-mail inválido")
      continue

    dados_usuario = [nome,data_de_nascimento,cpf,email]
    return dados_usuario

def consultar_registro(registros, id):
  """
  Esta função procura o registro
  :param registros: Lista contendo os registros que foram cadastrados
  :param id: ID do registro que deve ser procurado
  :return: Todos os dados do usuário caso encontrado, se não existir o ID, retorna a mensagem que não foi encontrado
  """
  indice = id - 1
  if 0 <= indice < len(registros):
    print(registros[indice])
  else:
    print("Registro não encontrado")

def listar_registros(registros):
  """
  Esta função lista todos os registros caso exista
  :param registros: Lista contendo os registros que foram cadastrados
  """
  if not registros:
    print("Não possui nenhum registro no banco de dados")
  for i, registro in enumerate(registros):
    print(f"ID: {i + 1}:", registro)

def remover_registro(registros, id):
  """
  Esta função apaga a lista que contém o indice informado pelo usuário
  :param registros: Lista contendo os registros que foram cadastrados
  :param id: ID do registro que deve ser removido
  """
  indice = id - 1
  if 0 <= indice < len(registros):
    print(f"O registro removido foi: {registros[indice]}")
    del registros[indice]
  else:
    print("Registro não encontrado")

def atualizar_registro(registros):
  """
  Esta função atualiza os dados cadastrados
  :param registros: Lista contendo os registros que foram cadastrados
  """
  id = int(input("Insira o ID do registro que deseja modificar: "))
  indice = id - 1

  if 0 <= indice < len(registros):
    print(" Insira 1 para modificar o nome \n Insira 2 para alterar a data de nascimento \n Insira 3 para alterar CPF \n Insira 4 para alterar o e-mail")
    campo_escolhido = int(input("Qual o campo que será modificado? "))
    if campo_escolhido == 1:
      novo_nome = input("Insira o novo nome: ")
      registros[indice][0] = novo_nome
    elif campo_escolhido == 2:
      nova_data_nascimento = input("Insira a nova data de nascimento: ")
      registros[indice][1] = nova_data_nascimento
    elif campo_escolhido == 3:
      novo_cpf = input("Insira o novo CPF: ")
      registros[indice][2] = novo_cpf
    elif campo_escolhido == 4:
      novo_email = input("Insira o novo e-mail: ")
      registros[indice][3] = novo_email
    else:
      print("Opção inválida. Nenhum campo foi alterado.")

  else:
    print("Registro não encontrado")

  return id, registros[indice]

def modificar_registro(registro):
  """
  
  """
  id_para_modificar = int(input("Insira o ID do registro que deseja modificar: "))
  indice = id_para_modificar - 1

  if 0 <= indice < len(registro):
    print(" Insira 0 para encerrar as modificaçes \n Insira 1 para modificar o nome \n Insira 2 para alterar a data de nascimento \n Insira 3 para alterar CPF \n Insira 4 para alterar o e-mail")

    while True:
      campo_escolhido = int(input("Qual o campo que será modificado? "))
      if campo_escolhido == 0:
        break
      if 1 <= campo_escolhido <= 4:
        novo_valor = input(f"Insira o novo valor para o campo {campo_escolhido} ({registro[indice][campo_escolhido-1]}): ")
        registro[indice][campo_escolhido-1] = novo_valor if novo_valor.strip() else registro[indice][campo_escolhido-1]
      else:
        print("Opção inválida. Nenhum campo foi alterado.")

  return registro[indice]

def modificar_registro(registros, posicao, novos_valores):
  indice = posicao - 1
  if 0 <= indice < len(registros):
    registros[indice] = novos_valores
    return registros
  else:
    print("Posição de modificação inválida. Nenhum registro foi modificado.")
    return registros
  

#----- Fluxo principal do programa -----

registros = []

while True:
  opcao_escolhida = menu()
  if opcao_escolhida == 1:
    solicita_dados_cadastrais()
    continue
  
  elif opcao_escolhida == 2:
    id = int(input("Insira o ID que você deseja consulta: "))
    consultar_registro(registros, id)
    continue
  
  elif opcao_escolhida == 3:
    listar_registros(registros)
    continue
  
  elif opcao_escolhida == 4:
    modificar_registro(registros)
  
  elif opcao_escolhida == 5:
    id = int(input("Insira o ID que você deseja consulta: "))
    remover_registro(registros, id)
    continue 
  
  elif opcao_escolhida == 6:
    break
  else:
    print("Opção inválida")
    continue

 
