class Appartement:
    # nom est une string
    def __init__(self, nom, surface):
        # L'objet est une liste de pièces (objets issus de la classe Piece)
        self.listeDePieces = []
        self.nom = nom
        self.surface = surface

    def getNom(self):
        return self.nom

    def getSurface(self):
        return self.surface

    # pour ajouter une pièce de classe Piece
    def ajouter(self, piece):

    # pour avoir le nombre de pièces de l'appartement
    def nbPieces(self):
        return len(self.listedePieces)

    # retourne la surface totale de l'appartement (un float)
    def SurfaceTotale(self):


...
# retourne la liste des pièces avec les surfaces
def getListePieces(self):  # sous forme d'une liste de tuples
    l_piece = (self.nom)
    for p in self.listedePieces:
        surftot = surftot + p.getSurface()
