"""Estudo de listas em Python"""

nomes = ['Joao', 'Miguel', 'Arthur', 'Gael', 'Davi', 'Bernardo', 'Gabriel']

# BUSCA
def buscalista(k, lt):
    """Implementacao de busca em lista contigua"""

    i = 0
    n = len(lt)

    while i < n:
        if lt[i] == k:
            return print(i)
        else:
            i = i + 1


def brinkslista(lt):

    i = 1
    n = len(lt)

    while i < n:
        print(lt[:i])
        i = i + 1

brinkslista(nomes)
