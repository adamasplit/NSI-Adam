# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 20:21:59 2021

@author: sdelr

1) c'est __init__
2) a vérifier une égalité
"""

nom_mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre",
            "octobre", "novembre", "decembre"]


class dateNSI():
    def __init__(self, jour, mois, annee):
        if (jour <= 31 and jour >= 1):
            self.jour = jour
        else:
            return None

        if (mois >= 1 and mois <= 12):
            self.mois = mois
        else:
            return None
        self.annee = annee

    def __repr__(self):
        return ("%d %s %d" % (self.jour, nom_mois[self.mois - 1], self.annee))

    def __eq__(self, d2):
        print("__eq__ date")
        if (d2.jour == self.jour and d2.mois == self.mois and self.annee == d2.annee):
            return True
        else:
            return False

    def __lt__(self, d2):
        if self.annee < d2.annee:
            return True
        elif self.mois < d2.mois:
            return True
        elif self.jour < d2.jour:
            return True
        return False



nouvel_an = dateNSI(1, 1, 2021)
fete_nationale = dateNSI(14, 7, 2021)

anniv = dateNSI(1, 1, 2021)

print("Les dates ", nouvel_an, " et ", fete_nationale, " sont égales ?", nouvel_an == fete_nationale)

print("Les dates ", nouvel_an, " et ", anniv, " sont égales ?", nouvel_an == anniv)

print(nouvel_an < fete_nationale)
