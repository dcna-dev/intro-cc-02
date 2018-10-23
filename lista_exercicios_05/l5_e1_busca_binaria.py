def busca(lista, elemento):

    primeiro = 0
    ultimo = len(lista) -1

    while primeiro <= ultimo:
        i = (primeiro + ultimo) // 2
        print(i)
        if elemento == lista[i]:
            return i
        elif elemento > lista[i]:
            primeiro = i + 1
        else:
            ultimo = i - 1
    return False


def test_busca_binaria():
    lista = [1,2,3,4,5,6,7,8,9]
    elemento = 3
    assert busca_binaria(lista,elemento) == 2


def test_busca_binaria_nao_existe():
    lista = [1,2,3,4,5,6,7,8,9]
    elemento = 21
    assert busca_binaria(lista, elemento) == False
