def imprime_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == len(matriz[i]) -1:
                print(matriz[i][j])
            else:
                print(matriz[i][j], end = ' ')



def test_imprime_matriz(capfd):
    matriz = [[1], [2], [3]]
    imprime_matriz(matriz)
    out, err = capfd.readouterr()
    assert out == '1\n2\n3\n'

    matriz = [[1, 2, 3], [4, 5, 6]]
    imprime_matriz(matriz)
    out, err = capfd.readouterr()
    assert out == '1 2 3\n4 5 6\n'
