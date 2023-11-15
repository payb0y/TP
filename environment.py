class Environment:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grid = [[0] * largeur for _ in range(hauteur)]

    def afficher(self):
        pass

    def initialiser(self):
        pass