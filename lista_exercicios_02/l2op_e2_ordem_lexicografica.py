def primeiro_lex(lista):

    menor = 10000000
    primeiro = ''
    for i in range(len(lista)):
            if ord(lista[i][0]) < menor:
                primeiro = lista[i]
                menor = ord(lista[i][0])
    return primeiro



def test_primeiro_lex():
    lista = ['oĺá', 'A', 'a', 'casa']
    assert primeiro_lex(lista) == 'A'

    lista = ['AAAAAA', 'b']
    assert primeiro_lex(lista) == 'AAAAAA'

    lista = ['maria', 'josé', 'PAULO', 'Catarina']
    assert primeiro_lex(lista) == 'Catarina'
