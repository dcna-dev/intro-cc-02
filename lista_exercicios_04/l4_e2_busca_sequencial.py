def busca(lista, elemento):

    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False


def test_busca():
    lista = ['a', 'e', 'i']
    elemento = 'e'
    assert busca(lista, elemento) == 1


    lista = [12, 13, 14]
    elemento = 15
    assert busca(lista, elemento) == False



