def encontra_impares(lista):
    lista_impares = []

    if len(lista) > 0:

        if lista[0] % 2 != 0:
            lista_impares.append(lista[0])
        lista_impares = lista_impares + encontra_impares(lista[1:])

    return lista_impares

def test_encontra_impares():

    lista = [1,2,3,4,5,6,7,8,9]
    assert encontra_impares(lista) == [1,3,5,7,9]
