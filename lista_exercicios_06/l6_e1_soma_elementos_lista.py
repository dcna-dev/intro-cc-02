def soma_lista(lista):

    if len(lista) > 1:
        lista[0] += lista[1]
        lista.pop(1)
        soma_lista(lista)
    return lista[0]



def test_soma_lista():
    lista = [1,2,3,4,5,6]
    assert soma_lista(lista) == 21
