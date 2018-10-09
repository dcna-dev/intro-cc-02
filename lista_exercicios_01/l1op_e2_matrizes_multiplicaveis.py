def sao_multiplicaveis(m1, m2):
    colunas_m1 = len(m1[0])
    linhas_m2 = len(m2)

    if colunas_m1 == linhas_m2:
        return True
    else:
        return False


def test_sao_multiplicaveis():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    assert sao_multiplicaveis(m1, m2) == False

    m1 = [[1], [2], [3]]
    m2 = [[1, 2, 3]]
    assert sao_multiplicaveis(m1, m2) == True
