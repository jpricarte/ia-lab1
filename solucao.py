import abc
from dataclasses import dataclass, field
from typing import Any
from collections import deque
import heapq

from pyrsistent import *

ESTADO_FINAL = "12345678_"

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado: str = estado
        self.pai: Nodo = pai
        self.acao: str = acao
        self.custo: int = custo
    
    def __lt__(self, other):
        return self.custo < other.custo


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return: []
    """
    lista_possiveis: [(str, str)] = []
    pos = estado.find('_')
    if pos <= 5:
        novo_estado = list(estado)
        novo_estado[pos], novo_estado[pos+3] = novo_estado[pos+3], novo_estado[pos]
        lista_possiveis.append(('abaixo', str(''.join(novo_estado))))
    if pos >= 3:
        novo_estado = list(estado)
        novo_estado[pos], novo_estado[pos-3] = novo_estado[pos-3], novo_estado[pos]
        lista_possiveis.append(('acima',str(''.join(novo_estado))))
    if pos % 3 != 2:
        novo_estado = list(estado)
        novo_estado[pos], novo_estado[pos+1] = novo_estado[pos+1], novo_estado[pos]
        lista_possiveis.append(('direita',str(''.join(novo_estado))))
    if pos % 3 != 0:
        novo_estado = list(estado)
        novo_estado[pos], novo_estado[pos-1] = novo_estado[pos-1], novo_estado[pos]
        lista_possiveis.append(('esquerda',str(''.join(novo_estado))))
    return lista_possiveis


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return: []
    """
    # Chama a função sucessor para o nodo
    # Pega o retorno e faz um map (lembrar de converter pra list no final)
    # map(lambda item: item[] expression, iterable)
    filhos = map(lambda tup: Nodo(tup[1],nodo,tup[0],nodo.custo+1),sucessor(nodo.estado))
    return list(filhos)

def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return: []
    """
    # algoritmo :
    '''
    busca_grafo(estado_inicial)
       X <- {}
       F <- {s}
       loop:
         se F = vazio falha
         v <- retira algum nó de F
         se v é o objeto : retorna caminho s-v
         se v não pertence a X:
           insere v em x (como antecessor)
           insere vizinho de v em F
    '''
    inicial = Nodo(estado, None, None, 0)
    explorados: [Nodo] = []
    fronteira: deque = deque([inicial])
    while len(fronteira) != 0:
        atual = fronteira.popleft()  # Remove o elemento da fila
        if atual.estado == ESTADO_FINAL: # Se o estado for final, retorna a lista de movimentos
            return gera_caminho(atual)      
            
        if not estadoEstaLista(atual, explorados):  # Se o estado ainda não havia sido explorado
            explorados.append(atual) # Insere o estado em explorados
            fronteira.extend(expande(atual)) # Insere o nodos vizinhos na fronteira    
    return None # Se sair do laço é porque não tem caminho

def estadoEstaLista(nodo, lista):
    for e in lista:
        if nodo.estado == e.estado:
            return True
    return False
    
    #return nodo in list(map(lambda e: e.estado,explorados.copy()))

def gera_caminho(nodo_final):
    atual = nodo_final
    lista_acoes = []
    while atual.pai != None:
        lista_acoes.append(atual.acao)
        atual = atual.pai
    return lista_acoes.reverse()



def dfs(estado):
    raise NotImplementedError
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # Pilha 
    # substituir a linha abaixo pelo seu codigo
    # raise NotImplementedError
    inicial = Nodo(estado, None, None, 0)
    explorados: [Nodo] = []
    fronteira: deque = deque([inicial])
    while len(fronteira) != 0:
        # Remove o elemento da pilha
        atual = fronteira.pop()
        # Se o estado for final, retorna a lista de movimentos
        if atual.estado == ESTADO_FINAL:
            return gera_caminho(explorados, atual)
        # Se o estado ainda não havia sido explorado
        if not estadoEstaLista(atual, explorados):
            # Insere o estado em explorados
            explorados.append(atual)
            fronteira.extend(expande(atual))
    # Se sair do laço é porque não tem caminho
    return []



#fila de prioridades - min heap
'''
    busca_grafo(estado_inicial)
       X <- {}
       F <- {s}
       loop:
         se F = vazio falha
         v <- retira algum nó de F
         se v é o objeto : retorna caminho s-v
         se v não pertence a X:
           insere v em x (como antecessor)
           insere vizinho de v em F
'''
def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    inicial = Nodo(estado, None, None, 0)
    explorados = []
    fronteira = FronteiraHamming()
    fronteira.inserir(inicial)
    while fronteira.len() != 0:
        atual = fronteira.retirar()  # Remove o elemento da fila
        if atual.estado == ESTADO_FINAL:  # Se o estado for final, retorna a lista de movimentos
            print(str(len(explorados)) + "nodos explorados")
            return gera_caminho(atual)

        # Se o estado ainda não havia sido explorado
        if not estadoEstaLista(atual, explorados):
            explorados.append(atual)  # Insere o estado em explorados
            fronteira.inserir_lista(expande(atual))
    return None  # Se sair do laço é porque não tem caminho


def hammingDist(estado):
    foraLugar = 0
    for peca in range(1, 9):
        if ondeEsta(estado, peca) != ondeDeveriaEstar(peca):
            foraLugar = foraLugar + 1
    return foraLugar


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    inicial = Nodo(estado, None, None, 0)
    explorados = []
    fronteira = FronteiraManhattan()
    fronteira.inserir(inicial)
    while fronteira.len() != 0:
        atual = fronteira.retirar()  # Remove o elemento da fila
        if atual.estado == ESTADO_FINAL:  # Se o estado for final, retorna a lista de movimentos
            #print(str(len(explorados)) + "nodos explorados")
            return gera_caminho(atual)

        # Se o estado ainda não havia sido explorado
        if not estadoEstaLista(atual, explorados):
            explorados.append(atual)  # Insere o estado em explorados
            fronteira.inserir_lista(expande(atual))
    return None  # Se sair do laço é porque não tem caminho

def manhattanDistTotal(estado):
    distAcumulada = 0
    for peca in range(1, 9):
        distAcumulada = distAcumulada + manhattanDistPeca(estado, peca)
    return distAcumulada


def manhattanDistPeca(estado, peca):
    esta = ondeEsta(estado, peca)
    deveriaEstar = ondeDeveriaEstar(peca)
    return abs(esta//3 - deveriaEstar//3) + abs(esta % 3 - deveriaEstar % 3)



def ondeEsta(estado, peca):
    return estado.index(str(peca))


def ondeDeveriaEstar(peca):
    return peca-1

class Fronteira(metaclass=abc.ABCMeta):
    def __init__(self):

        self.nodes = []  # a fila de prioridades do nodos

    @abc.abstractmethod
    def heuristic(self, estado):
        pass

    def inserir(self, nodo: Nodo):
        wrapper = PrioritizedItem(
            nodo.custo + self.heuristic(nodo.estado), nodo)
        heapq.heappush(self.nodes, wrapper)

    def inserir_lista(self, listaNodos):
        for nodo in listaNodos:
            self.inserir(nodo)

    def len(self):
        return len(self.nodes)

    def retirar(self):
        wrapper: PrioritizedItem = heapq.heappop(self.nodes)
        nodo = wrapper.item
        del wrapper
        return nodo


# @dataclass(order=True)
class PrioritizedItem:
    def __init__(self, heuristica, nodo):
        self.priority = heuristica
        self.item = nodo

    def __del__(self):
        return self.item

    def __lt__(self, other):
        return self.priority < other.priority


# @Fronteira.register()
class FronteiraHamming(Fronteira):
    def __init__(self):
        self.nodes = []
        super()

    def heuristic(self, estado):
        foraLugar = 0
        for peca in range(1, 9):
            if ondeEsta(estado, peca) != ondeDeveriaEstar(peca):
                foraLugar = foraLugar + 1
        return foraLugar

# @Fronteira.register()


class FronteiraManhattan(Fronteira):
    def __init__(self):
        self.nodes = []
        super()

    def heuristic(self, estado):
        distAcumulada = 0
        for peca in range(1, 9):
            distAcumulada = distAcumulada + \
                self.manhattanDistPeca(estado, peca)
        return distAcumulada

    def manhattanDistPeca(self, estado, peca):
        esta = ondeEsta(estado, peca)
        deveriaEstar = ondeDeveriaEstar(peca)
        return abs(esta//3 - deveriaEstar//3) + abs(esta % 3 - deveriaEstar % 3)

