def dimensoes(matriz):

    resultado = str(len(matriz)) + 'X' + str(len(matriz[0]))
    print(resultado)

def test_dimensoes01():
    assert dimensoes([[1], [2], [3]]) == '3X1'
    assert dimensoes([[1, 2, 3], [4, 5, 6]]) == '2X3'
    assert dimensoes([[1, 2], [4, 5]]) == '2X2'

