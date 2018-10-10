def maiusculas(frase):

    maiusculas = ''
    for letra  in range(len(frase)):
        if ord(frase[letra]) >= 65 and ord(frase[letra]) <= 90:
            maiusculas += frase[letra]
    return maiusculas


def test_maiusculas():
    frase = 'Programamos em python 2?'
    assert maiusculas(frase) == 'P'

    frase = 'Programamos em Python 3.'
    assert maiusculas(frase) == 'PP'

    frase = 'PrOgRaMaMoS em python!'
    assert maiusculas(frase) == 'PORMMS'
