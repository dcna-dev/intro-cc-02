def bubble_sort(lista):

    trocado = True
    while trocado:
        for i in range(len(lista)-1):
            for j in range(len(lista)-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocado = True
                    print(lista)
                else:
                    trocado = False
    return lista
'''
    for i in range(len(lista)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                print(lista)
    return lista
'''

def test_bubble_sort():
    lista = [5,1,4,2]
    assert bubble_sort(lista) == [1, 2, 4, 5]
