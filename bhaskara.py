import math

class Bhaskara:

    def calculaDelta(self, a, b, c):
        return b**2 - 4*a*c


    def calculaRaizes(self, a, b, c):
        delta = self.calculaDelta(a, b, c)
        if delta < 0:
            return 0
        elif delta == 0:
            return (-b + math.sqrt(delta))/(2*a)
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            return x1, x2

