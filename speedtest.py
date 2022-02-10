from solucao import *
import time

def teste_alg(version, initial_state):
    inicio = time.time()
    a = version(initial_state)
    print(len(a))
    fim = time.time()
    print(fim-inicio)