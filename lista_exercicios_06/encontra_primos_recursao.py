def verifica_primos(n, d = 2):

    if d > n // 2:
        return True
    elif n % d == 0:
        return False
    else:
        return verifica_primos(n, d + 1)


def encontra_primos(lista):

    try:
        lista_primos
    except:
        lista_primos = []

    if len(lista) > 0:
        if verifica_primos(lista[0]) == False:
            lista_primos.append(lista[0])
        return encontra_primos(lista[1:])
    return lista_primos


def test_verifica_primos():
    n = 9
    assert verifica_primos(n) == False

    n = 5
    assert verifica_primos(n) == True

    n = 2
    assert verifica_primos(n) == True

    n = 10
    assert verifica_primos(n) == False


def test_encontra_primos():
    lista = [1,2,3,4,5,6,7,8,9]
    assert encontra_primos(lista) == [2, 3, 5, 7]
