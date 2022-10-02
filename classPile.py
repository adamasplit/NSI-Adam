class Pile():
    def __init__(self):
        self.maListe = []

    def __repr__(self):
        print(self.maListe)
    def empiler(self, el):
        return self.maListe.append(el)

    def depiler(self, ):
        return self.maListe.pop()

    def vide(self):
        return (len(self.maListe) == 0)

    def remplissage(self):
        return (len(self.maListe))


p = Pile()
p.empiler(15)
p.empiler(10)
p.empiler(-2)
print("Premier element recupere = ", p.depiler())
print("2eme element recupere = ", p.depiler())
