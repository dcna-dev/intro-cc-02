def nome_mais_curto(lista_nomes):

    menor = 100000000000
    mais_curto = ''
    for nome_comp in lista_nomes:
        for nome in nome_comp.split(' '):
            if len(nome) <= menor:
                mais_curto = nome
                menor = len(nome)
    return mais_curto.capitalize()

def test_nome_mais_curto():
    lista_nomes = ['Diego Cananea', 'Jose Pedro', 'Maria Josefa']
    assert nome_mais_curto(lista_nomes) == 'Jose'

    lista_nomes = ['ana', 'jose', 'diego']
    assert nome_mais_curto(lista_nomes) == 'Ana'
