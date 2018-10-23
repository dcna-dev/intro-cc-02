from random import randrange

def lista_grande(n):

    lista = []
    for i in range(n):
        lista.append(randrange(n**10))
    return lista


def ordena(lista):

    fim = len(lista)
    for i in range(fim):
        for j in range(i+1, fim):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def test_lista_grande():
    n = 1000
    assert len(lista_grande(n)) == n

def test_ordena():
    lista = [4, 3,8,1,2,0]
    assert ordena(lista) == [0,1,2,3,4,8]
