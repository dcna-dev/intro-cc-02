def sao_multiplicaveis(m1, m2):
    colunas_m1 = len(m1[0])
    linhas_m2 = len(m2)

    if colunas_m1 == linhas_m2:
        return True
    else:
        return False


def cria_matriz(num_linhas, num_col, valor = 0):

    matriz = []
    for linha in range(num_linhas):
        linha_mat = []
        for coluna in range(num_col):
            linha_mat.append(valor)
        matriz.append(linha_mat)
    return matriz


def multiplica_matrizes(m1, m2):

    num_linhas_m1, num_colunas_m1 = len(m1), len(m1[0])
    num_col = len(m2[0])

    matriz_result = cria_matriz(num_linhas_m1, num_col)
    for linha in range(num_linhas_m1):
        for coluna in range(num_col):
            for k in range(num_colunas_m1):
                matriz_result[linha][coluna] += m1[linha][k]*m2[k][coluna]
    return matriz_result

def test_multiplica_matrizes():
    m1 = [[1,2],[3,4]]
    m2 = [[-1, 3], [4, 2]]
    assert multiplica_matrizes(m1, m2) == [[7,7], [13,17]]

    m1 = [[2, 3],[0, 1], [-1,4]]
    m2 = [1, 2, 3], [-2, 0, 4]
    assert multiplica_matrizes(m1, m2) == [[-4, 4, 18], [-2, 0, 4], [-9, -2, 13]]


