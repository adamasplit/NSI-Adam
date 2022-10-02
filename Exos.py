import random


class Identite:
    def __init__(self, nom, prenom, a):
        self._nom = nom
        self._prenom = prenom
        self._a = a

    def myst(self, b):
        return b - self._a

"""
EXERCICE 1 :

a) On a comme attributs le nom, le prénom, a
    On a 2 méthodes: __init__() et myst()
    
b) Id1 = Identite("Dupont", "Hugo", 1999)
"""
Id1 = Identite("Dupont", "Hugo", 1999)
print(Id1.myst(2020))  # c) Le résultat affiché est 21

"""

EXERCICE 2

"""


# Remplacement de a, b, c Pour la b) (On vérifie qu'un triangle est rectangle)
class toto:
    def __init__(self, AB, AC, BC):
        self._AB = AB
        self._AC = AC
        self._BC = BC

    def myst(self):
        if self._AB ** 2 + self._AC ** 2 == self._BC ** 2:
            return True
        else:
            return False


# Question a)
t1 = toto(3, 4, 5)
t2 = toto(4, 5, 6)
print(t1.myst())  # Cela renvoie True
print(t2.myst())  # Cela renvoie False

# Question c)
a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)
totoList = [toto(a, b, c).myst() for i in range(20)]

"""

EXERCICE 3 / 4 / 5:

"""


#  Exercice 3
class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def __repr__(self):
        if self._longueur < self._largeur:
            temp = self._longueur
            self._longueur = self._largeur
            self._largeur = temp
        print("Votre longueur est", self._longueur, "et votre largeur est", self._largeur)

    # Exercice 4

    def __eq__(self, other):
        return self._largeur == other._largeur and self._longueur == other._longueur

    def __gt__(self, other):
        return self._largeur > other._largeur and self._longueur > other._longueur

    def __ge__(self, other):
        return self._largeur >= other._largeur and self._longueur >= other._longueur

    # Exercice 5

    def __add__(self, val):
        return (self._longueur + val, self._largeur + val)

    def __mul__(self, val):
        return (self._longueur * val, self._largeur * val)


"""

Exercice 6 :

-classe contenant une boucle while qui soustrait 0.001 à la valeur entrée de base toute les
    0.001 sec (grace à la commande sleep() de la lib Time
    
-De la meme manière, avec la lib threading

"""