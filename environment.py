import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import random

class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grid = [[0] * (largeur + 1) for _ in range(hauteur + 1)]
        self.fig, self.ax = plt.subplots()  
        self.agent_marker = None 
        self.vacuum_image = Image.open('./assets/vacuum.png')

    def afficher_agent(self, position):
        if self.agent_marker:
            self.agent_marker.remove() 


        # Plot the agent image at the center
        ab = AnnotationBbox(OffsetImage(self.vacuum_image, zoom=0.03), (position[1] + 0.5, position[0] + 0.5), frameon=False)

        self.ax.add_artist(ab)
        self.agent_marker = ab

        self.fig.canvas.draw()
    

    def afficher(self):
        # Clear the previous grid
        self.ax.clear()
        
        # init the grid
        self.ax.imshow(self.grid, cmap='gray')

        # borders in white
        for i in range(self.hauteur + 1):
            self.ax.axhline(i, color='white')
        for j in range(self.largeur + 1):
            self.ax.axvline(j, color='white')

        # dirty cells
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if random.randint(0, 1) == 1:
                    self.ax.add_patch(patches.Rectangle((j, i), 1, 1, color='grey'))
                    self.grid[i][j] = 1
