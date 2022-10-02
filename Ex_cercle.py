import math

pi = math.acos(-1)


class cercle:
    def __init__(self, rayon):
        self._rayon = rayon

    def aire(self):
        return pi * self._rayon ** 2

    def perimetre(self):
        return 2 * self._rayon * pi

    def set_rayon(self, val):
        if (val < 0):
            print("Valeur interdite")
            return None
        else:
            self._rayon = val

    def get_rayon(self):
        return (self._rayon)

    def __repr__(self):
        return ("aire = %f perimetre = %f") % (self.aire(), self.perimetre())


c = cercle(34)
print(c)
