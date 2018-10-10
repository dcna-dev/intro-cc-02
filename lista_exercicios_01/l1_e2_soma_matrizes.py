def soma_matrizes(m1, m2):

    if len(m1) != len(m2):
        return False
    soma_mat = []
    for i in range(len(m1)):
        soma = []
        for j in range(len(m1[i])):
            soma.append(m1[i][j] + m2[i][j])
        soma_mat.append(soma)
    return soma_mat

def test_soma_matrizes():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    assert soma_matrizes(m1, m2) == [[3, 5, 7], [9, 11, 13]]

    m1 = [[1], [2], [3]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    assert soma_matrizes(m1, m2) == False

