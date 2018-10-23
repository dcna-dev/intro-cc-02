def insercao_direta(lista):


    for i in range(1, len(lista)):
        chave = lista[i]
        j = i
        while j > 0 and chave < lista[j -1]:
            lista[j] = lista[j - 1]
            j -= 1
        lista[j] = chave
    return lista


def test_insercao_direta():

    lista = [3,1,6,2,4,0]

    assert insercao_direta(lista) == [0, 1, 2, 3, 4, 6]
