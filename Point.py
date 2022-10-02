class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplacer(self, dx, dy):
        self.x += dx
        self.y += dy


class triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def deplacer(self, dx, dy):
        self.p1.deplacer(dx, dy)
        self.p2.deplacer(dx, dy)
        self.p3.deplacer(dx, dy)


a = point(1, 2)
b = point(15, 8)
c = point(3, 5)
d = point(-2, -3)

t1 = triangle(a, b, c)
t2 = triangle(b, c, d)

t1.deplacer()

class Z:
    def __init__(self,num, den):
        self.num=num
        self.den=den
    def __str__(self):
        return ("%d/%d"%(self.num,self.den))
    def __add__(self, other):
        num2=(self.num*other.den+fr2)
        return ()

