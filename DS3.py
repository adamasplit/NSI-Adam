# la classe pile
class Pile:
    ''' classe Pile '''

    def __init__(self):
        "Initialisation d'une pile vide"
        self.L = []

    def vide(self):
        "teste si la pile est vide"
        return self.L == []

    def depiler(self):
        "dépile"
        assert not self.vide(), "Pile vide"
        return self.L.pop()

    def empiler(self, x):
        "empile"
        self.L.append(x)

    def taille(self):
        return (len(self.L))

    # un plus pour un affichage sous forme de pile
    def __str__(self):
        s = ""
        for k in range(self.taille() - 1, -1, -1):
            s = s + "|" + str(self.L[k]) + "|" + "\n"
        return s


class file():
    # retourne une file vide
    def __init__(self):
        "Initialisation d'une pile vide"
        self.L = []

    def vide(self):
        return self.L == []

    def enfiler(self, x):
        # ajoute x à la file f"
        return self.L.append(x)

    def defiler(self):
        # enlève et renvoie le premier élément de la file
        if self.vide() == True: pass
        return self.L.pop()


p = Pile()  # On crée une pile vide
a = 4
b = 5


#On remplit la pile (example de remplissage)
p.empiler(a)
p.empiler(b)
p.empiler(b)
# Correction exercice 2
"""
p.empiler(a)
p.empiler(b)
a = p.depiler()
b = p.depiler()

TEST :
# print(a)
# print(b)
"""



def inverse(p):
    # Création d'une file/pile temporaire
    f_temp = file()
    p_temp = Pile()
    while p.vide() == False:
        #on vide la pile intiale dans la pile temporaire(le processus permet d'inverser les 2 piles)
        p_temp.empiler(p.depiler())
    while p_temp.vide() == False:
        #on vide la pile temporaire dans une file(ainsi, on garde l'ordre inversé de la pile)
        f_temp.enfiler(p_temp.depiler())
    while f_temp.vide() == False:
        #on fait défiler la file dans la pile initiale
        p.empiler(f_temp.defiler())


def copie(p):
    # Création d'une file/pile temporaire
    f_temp = file()
    p_temp = Pile()
    while p.vide() == False:
        # tant que la pile n'est pas vide, dépiler la pile et ajouter la valeur à la file
        f_temp.enfiler(p.depiler())

    while f_temp.vide() == False:
        #Création d'une variable temporaire
        val=f_temp.defiler()
        # On empile au deux piles les valeurs de la file
        p.empiler(val)
        p_temp.empiler(val)
    return p_temp


print(p)
inverse(p)
print(p)
