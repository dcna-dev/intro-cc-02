def incomodam(n):

    if n <= 0:
        return ''
    elif n == 1:
        return 'incomodam'
    return 'incomodam ' + incomodam(n-1)


def elefantes(n):
    if n < 1:
        return ''
    elif n == 1:
        return 'Um elefante incomoda muita gente\n'
    elif n == 2:
        return 'Um elefante incomoda muita gente\n' + str(n) + ' elefantes ' + incomodam(n) + ' muito mais\n'
    return elefantes(n-1) + str(n-1) + ' elefantes ' + incomodam(n-1) + ' muita gente\n' + str(n) + ' elefantes ' + incomodam(n) + ' muito mais\n'

def test_incomodam():
    n = 5
    assert incomodam(n) == 'incomodam incomodam incomodam incomodam incomodam'

