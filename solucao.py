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


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    lista_possiveis: [(str, str)] = []
    pos = estado.find('_')
    if pos <= 5:
        novo_estado = list(estado)
        novo_estado[pos], novo_estado[pos+3] = novo_estado[pos+3], novo_estado[pos]
        lista_possiveis.append(('abaixo',''.join(novo_estado)))
    if pos >= 3:
        novo_estado = list(estado)
        novo_estado[pos], novo_estado[pos-3] = novo_estado[pos-3], novo_estado[pos]
        lista_possiveis.append(('acima',''.join(novo_estado)))
    if pos % 3 != 2:
        novo_estado = list(estado)
        novo_estado[pos], novo_estado[pos+1] = novo_estado[pos+1], novo_estado[pos]
        lista_possiveis.append(('direita',''.join(novo_estado)))
    if pos % 3 != 0:
        novo_estado = list(estado)
        novo_estado[pos], novo_estado[pos-1] = novo_estado[pos-1], novo_estado[pos]
        lista_possiveis.append(('esquerda',''.join(novo_estado)))
    return lista_possiveis


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
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
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


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
    raise NotImplementedError
