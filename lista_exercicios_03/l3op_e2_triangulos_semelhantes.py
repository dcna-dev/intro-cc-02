class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def perimetro(self):

        return self.a + self.b + self.c


    def tipo_lado(self):

        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isósceles'
        else:
            return 'escaleno'


    def retangulo(self):

        if self.a**2 + self.b**2 == self.c**2:
            return True
        else:
            return False


    def semelhantes(self, triangulo):

        if self.a >= triangulo.a:
            t1 = [self.a, self.b, self.c]
            t2 = [triangulo.a, triangulo.b, triangulo.c]
        else:
            t1 = [triangulo.a, triangulo.b, triangulo.c]
            t2 = [self.a, self.b, self.c]

        t1 = sorted(t1)
        t2 = sorted(t2)

        for lado in range(3):
            if t1[lado] % t2[lado] != 0:
                return False
        return True


class Test_Triangulo:

    def test_semelhantes(self):
        triangulo1 = Triangulo(2,2,2)
        triangulo2 = Triangulo(4,4,4)
        assert triangulo1.semelhantes(triangulo2) == True
