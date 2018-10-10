def conta_letras(frase, contar='vogais'):
    count_vogais = 0
    count_consoantes = 0
    for letra in range(len(frase)):
        if frase[letra].lower() in 'aeiou':
            count_vogais += 1
        elif frase[letra].lower() == ' ':
            pass
        else:
            count_consoantes += 1
    if contar == 'vogais':
        return count_vogais
    else:
        return count_consoantes



def test_conta_letras():
    frase = 'programamos em python'
    assert conta_letras(frase) == 6

    frase = 'programamos em python'
    contar = 'vogais'
    assert conta_letras(frase, contar) == 6

    frase = 'programamos em python'
    contar = 'consoantes'
    assert conta_letras(frase, contar) == 13
