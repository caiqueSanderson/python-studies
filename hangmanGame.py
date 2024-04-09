import random

lista_diversificada = ["banana","maça","abacaxi","ford","audi","caneta","lapis","brasil","argentina","america"]

def conversor_string(lista):
  """
  Esta função escolhe uma palavra aleatória da lista e transforma a palavra em uma lista contendo as letras da palavra
  :param lista: Lista diversificada de palavras
  :return: Lista de letras que forma uma palavra
  """
  palavra_aleatorio = random.choice(lista)

  lista_letras = []
  for letra in palavra_aleatorio:
    lista_letras.append(letra)

  return lista_letras

def checar_letra(palavra,progresso,palpite):
  """
  Esta função verifica se o palpite do usuário está correto
  :param palavra: Lista contendo as letras da palavra
  :param progresso: Lista contendo as letras já advinhadas pelo usuário
  :param palpite: String contendo a letra que o usuário acha que a palavra têm.
  :return: Lista das letras já encontradas, ordenadas(progresso) e um booleano caso para saber se a letra foi encontrada.
  """
  letra_encontrada = False
  for i in range(len(palavra)):
    if palavra[i] == palpite:
      progresso[i] = palpite
      letra_encontrada = True

  return progresso, letra_encontrada

def verificar_lista(progresso):
  """
  Esta função verifica se ainda possui letras a ser advinhadas
  :param progresso: Lista contendo as letras adivinhadas e letras que não foram advinhada como "_"
  :return: Booleano para caso ainda tem letras a serem advinhadas ou não
  """
  for elemento in progresso:
    if elemento == "_":
      return False
  return True

def desenha_enforcado(i):
  """
  Esta função contém uma lista de listas para cada parte do desenho do enforcado
  :param i: Indice da lista
  :return: Uma lista contém uma parte do enforcado
  """
  partes_enforcado = [
        [ " O "],
        [ " | "],
        [ "/ \\"],
        [ " | "],
        [ " | "],
        [" / \\"],
    ]
  return partes_enforcado[i]

def verifica_repeticao(palpites,palpite):
  """
  Esta função verifica se o palpite já foi feito
  :param palpites: Lista contendo os palpites feitos pelo usuário
  :palpite: A letra que o usuário deseja verificar
  :return: Booleano referente se é uma letra nova ou não
  """
  if palpite in palpites:
    elemento_novo = False
  else:
    elemento_novo = True
  return elemento_novo

#----- Fluxo principal -----

#Variáveis necessárias
progresso = []
palpites = []
enforcado = []

palavra_escolhida = conversor_string(lista_diversificada)

# Criar uma copia da lista, substituindo as letras por "_"
progresso = palavra_escolhida.copy()
for i in range(len(progresso)):
  progresso[i] = "_"
print(f"A palavra a ser advinhada possui essa quantidade de letras: {progresso}")



# Se o palpite estiver correto ele continua a perguntar o pŕoximo palpite verificando se a lista já foi totalmente preenchida ou se o palpite é repetido
while len(enforcado) < 6:

  palpite = input("Qual é o seu palpite: ").lower()
  if verifica_repeticao(palpites, palpite) == False:
    print("Você já tentou essa letra. Tente novamente.")
    continue

  elif verifica_repeticao(palpites, palpite):
    palpites.append(palpite)
    lista, letra_encontrada = checar_letra(palavra_escolhida,progresso,palpite)

    if letra_encontrada:
      verifica_lista_preenchida = verificar_lista(progresso)

      if verifica_lista_preenchida:
        print(f"Parabéns você advinhou a palavra {progresso}")
        break
      else:
        print(f"Seu progresso: {progresso} \n Seus palpites: {palpites} \n")

    else:
      parte_enforcado = desenha_enforcado(len(enforcado))
      enforcado.append(parte_enforcado)
      print("Letra incorreta! Tente novamente.")

      for parte in enforcado:
        print(parte)

if len(enforcado) == 6 and "_" in progresso:
    print("Você perdeu! A palavra correta era:", ''.join(palavra_escolhida))
