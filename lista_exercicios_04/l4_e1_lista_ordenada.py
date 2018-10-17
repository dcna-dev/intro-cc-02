def ordenada(lista):

    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True


def test_lista_ordenada():
    lista = [1,2,3,4,5,6]
    assert ordenada(lista) == True


def test_lista_nao_ordenada():
    lista = [1,2,3,7,3,1]
    assert ordenada(lista) == False
