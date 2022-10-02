from random import shuffle
import time


class perso:
    nombre_perso = 0

    def __init__(self, nom, genre):
        print("constructeur")
        self.lenom = nom
        if genre == "M":
            self.titre = "Monsieur"
        if genre == "F":
            self.titre = "Madame"


p1 = perso("Barbar", "M")
print(p1.lenom)


class carte():
    def __init__(self, valeur, couleur):
        if valeur < 1 or valeur > 13:
            print("Valeur Impossible")
            return None
        if couleur not in ["Pique", "Coeur", "Carreau", "Trefle"]:
            print("Couleur inexistante")
            return None
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        if (self.valeur >= 2 and self.valeur <= 10):
            var = "%d" % (self.valeur)
        if self.valeur == 11:
            var = "valet"
        if self.valeur == 12:
            var = "dame"
        if self.valeur == 13:
            var = "roi"
        if self.valeur == 1:
            var = "as"
        return (var + " de " + self.couleur)

    def __lt__(self, ob2):
        if ob2.valeur < self.valeur:
            return True
        else:
            return False

    def __eq__(self, other):
        return (self.valeur == other.valeur)


deck = []
for c in ["Pique", "Coeur", "Carreau", "Trefle"]:
    for v in range(1, 14):
        deck.append(carte(v, c))

score1 = score2 = 0
shuffle(deck)
while (len(deck) >= 2):
    c1 = deck.pop()
    c2 = deck.pop()
    print("Joueur 1 joue", c1, "contre", c2)
    time.sleep(0.5)
    if c1 > c2:
        score1 += 1
        print(score1, "point(s) pour le J1 !!")
        time.sleep(0.5)
    if c2 > c1:
        score2 += 1
        print(score2, "point(s) pour le J2 !!")
        time.sleep(0.5)
if score1 > score2:
    print("J1 a GAGNE !!")
else:
    print("J2 a GAGNE !!")
