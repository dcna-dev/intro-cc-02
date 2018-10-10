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

    num_linhas = len(m1)
    num_col = len(m2[0])

    matriz_result = cria_matriz(num_linhas, num_col)

    for linha in range(num_linhas):
        for coluna in range(num_col):
            matriz_result[linha][coluna] = m1[linha][coluna] * m2[linha][coluna] + m1[linha+1][coluna+1] * m2[linha+1][coluna+1]
    return matriz_result

def test_multiplica_matrizes():
    m1 = [[1,2],[3,4]]
    m2 = [[-1, 3], [4, 2]]
    assert multiplica_matrizes(m1, m2) == [[7,7], [13,17]]


