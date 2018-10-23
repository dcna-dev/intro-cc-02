from random import randrange

def lista_grande(n):

    lista = []
    for i in range(n):
        lista.append(randrange(n**10))
    return lista

def test_lista_grande():
    n = 1000
    assert len(lista_grande(n)) == n
