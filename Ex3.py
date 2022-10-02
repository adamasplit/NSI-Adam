class fraction():
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        if (denom <= 0):
            print("denimonateur negatif ou nul INTERDIT ")
            return None

    def __str__(self):
        ch = str(self.num) + "/" + str(self.denom)
        return (ch)

    def __eq__(self, other):
        if (self.num != other.num):
            return False
        if (self.denom != other.denom):
            return False
        return True

    def __lt__(self, other):
        val1 = self.num / self.denom
        val2 = other.num / other.denom
        return val1 < val2

    def __add__(self, other):
        nu = (self.num * other.denom + other.num * self.denom)
        de = (self.denom * other.denom)
        return fraction(nu, de)

    def __mul__(self, other):
        nu= self.num*other.num
        de = self.denom*other.denom
        return fraction(nu,de)


toto = fraction(2, 3)
print(toto)
tata = fraction(2, 0)
print(tata)
print(toto == toto)
print(toto == tata)
