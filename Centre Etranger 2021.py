class Noeud():
    def __init__(self, val):
        self.valeur = val
        self.fils = []

    def ajouter_fils(self, fi):
        self.fils.append((fi))

arbre = Noeud("A")
arbre.ajouter_fils("C")

arbre.ajouter_fils("B")
