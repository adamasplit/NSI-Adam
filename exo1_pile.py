# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 09:32:18 2022

@author: sdelr
"""

"""
Créer une classe Pile qui implémente le type abstrait pile en stockant les données de la pile dans un attribut privé _data de type list.

    L’initialisation s’effectue sans argument et affecte une liste vide à l’attribut _data.
    La méthode empiler(élément) ajoute l’élément à la fin de l’attribut _data.
    La méthode dépiler() retire l’élément à la fin de l’attribut _data et le renvoie.
    La méthode est_vide() renvoie True si la pile est vide et False sinon.
    La méthode sommet() renvoie l’élément présent au sommet de la pile, et None si la pile est vide.
"""

#CODE A COMPLETER !!



pile = Pile()
assert pile.est_vide() is True

pile.empiler(1)
assert pile.est_vide() is False
assert pile.sommet() == 1

pile.empiler(2)
assert pile.est_vide() is False
assert pile.sommet() == 2
assert pile.est_vide() is False

pile.empiler(3)
assert pile.sommet() == 3
assert pile.dépiler() == 3

while not pile.est_vide():
	pile.dépiler()

assert pile.est_vide() is True
assert pile.sommet() is None

#Pour aller plus loin, modifier la classe Pile afin que sommet() ne soit plus une 
#méthode, mais un attribut sommet. La série de tests précédents devra être modifié 
#en supprimant les parenthèses des appels des méthodes pile.sommet() en pile.sommet.