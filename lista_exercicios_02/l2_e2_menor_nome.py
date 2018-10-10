def menor_nome(lista_nomes):

    menor = 100000000000
    mais_curto = ''
    for n in lista_nomes:
        nome = n.strip()
        if len(nome) < menor:
            mais_curto = nome
            menor = len(nome)
    return mais_curto.capitalize()

def test_menor_nome():
    lista_nomes = ['maria', 'josé', 'PAULO', 'Catarina']
    assert menor_nome(lista_nomes) == 'José'

    lista_nomes = ['maria', ' josé  ', '  PAULO', 'Catarina  ']
    assert menor_nome(lista_nomes) == 'José'

    lista_nomes = ['Bárbara', 'JOSÉ  ', 'Bill']
    assert menor_nome(lista_nomes) == 'José'
