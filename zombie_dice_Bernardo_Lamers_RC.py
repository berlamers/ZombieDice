from random import randint, shuffle



class Dado:                                             #definição da classe dado
    def __init__(self, cor, lados, ladoSorteado):
        self.cor = cor
        self.lados = lados
        self.ladoSorteado = ladoSorteado


class Jogador:                                          #definição da classe jogador
    def __init__(self, nome, cerebros, tiros):
        self.nome = nome
        self.cerebros = cerebros
        self.tiros = tiros


def ladosDados(argument):                            #função para guardar as siglas
    switcher = {
        "C": "Cerebro",
        "P": "Passo",
        "T": "Tiro",
    }
    return switcher.get(argument)


def JogaDado(listaDados):                               #função para armazenar os dados jogados
    dado = listaDados.pop()
    numSorteado = randint(0, 5)
    dado.ladoSorteado = dado.lados[numSorteado]
    print("    ", dado.cor, ' ', ladosDados(dado.ladoSorteado))

    return dado


def VerificaTipoLado(listaDadosJogados, jogadorAtual):          #função para checar o lado sorteado
    for dado in listaDadosJogados:
        if (dado.ladoSorteado == "C"):
            jogadorAtual.cerebros = jogadorAtual.cerebros + 1
        elif (dado.ladoSorteado == "T"):
            jogadorAtual.tiros = jogadorAtual.tiros + 1


aluno = "Bernardo Lamers"
curso = "Análise e Desenvolvimento de Sistemas - Raciocínio Computacional"

print(aluno)
print(curso)
print("WELCOME TO ZOMBIE DICE\n")
numJogadores = 0
while (numJogadores < 2):
    numJogadores = int(input("Insira o número de zumbis: "))            #pede para o usuario inserir o número de jogadores

    if (numJogadores < 2):
        print("São necessários no mínimo dois zumbis")                  #condição para a quantidade mínima de jogadores

listaJogadores = []

for i in range(0, numJogadores):                                           #faz o i variar 0 até o numero de jogadores
    nome = input("Insira o nome do zumbi" + str (i + 1) + ": ")
    listaJogadores.append(Jogador(nome, 0, 0))

ladosDadoVerde = ["C", "P", "C", "T", "P", "C"]                     #lados dos dados
ladosDadoAmarelo = ["T", "P", "C", "T", "P", "C"]
ladosDadoVermelho = ["T", "P", "T", "C", "P", "T"]
alguemGanhou = False

dadoVerde = Dado("Verde", ladosDadoVerde, "")
dadoAmarelo = Dado("Amarelo", ladosDadoAmarelo, "")
dadoVermelho = Dado("Vermelho", ladosDadoVermelho, "")

listaDados = [
    dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
    dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
    dadoVermelho, dadoVermelho, dadoVermelho
]

listaDadosJogados = []                                  #lista para armazenar os dados jogados

print("Iniciando a partida")
while (not alguemGanhou):
    for jogadorAtual in listaJogadores:
        print("É a rodada de:", jogadorAtual.nome)          #inicio da rodada do jogador atual

        shuffle(listaDados)                                     #randomiza os dados
        numSorteado = randint(0, 5)     

        dado1 = JogaDado(listaDados)
        dado2 = JogaDado(listaDados)
        dado3 = JogaDado(listaDados)

        shuffle(listaDados)

        listaDadosJogados.clear()
        listaDadosJogados.append(dado1)
        listaDadosJogados.append(dado2)
        listaDadosJogados.append(dado3)

        VerificaTipoLado(listaDadosJogados, jogadorAtual)           #funçao para verificar os lados sorteados

        listaDados.append(dado1)
        listaDados.append(dado2)
        listaDados.append(dado3)

        shuffle(listaDados)

        print("" + jogadorAtual.nome)
        print("" + "Cerebros ", jogadorAtual.cerebros)             #contabilização dos cerebros
        print("" + "Tiros ", jogadorAtual.tiros)                   #contabilizaçao dos tiros

        for jogador in listaJogadores:                                #condição para o jogador que chegar a 13 cérebros ganhar
            if (jogador.cerebros >= 13):
                print("O zumbi", jogador.nome, "venceu\n")
                alguemGanhou = True

        for jogador in listaJogadores:                                #condiçao para eliminar jogador que levar 3 tiros
            if (jogador.tiros >= 3):
                print("O zumbi", jogador.nome, "foi eliminado\n")
                listaJogadores.remove(jogador)

        if (len(listaJogadores) == 1):
            print("O zumbi ", listaJogadores[0].nome, "venceu\n")
            alguemGanhou = True
            break

print("O jogo acabou")