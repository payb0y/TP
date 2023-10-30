from agent import Agent
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

class AgentAspirateur(Agent):
    def __init__(self, environnement):
        super().__init__(environnement)
        self.position = (0, 0)
        self.historique = []

    def percevoir(self):
        return self.environnement.grid[self.position[0]][self.position[1]] == 1

    def agir(self, action):
        if action == "aspirer":
            self.environnement.grid[self.position[0]][self.position[1]] = 0
            self.environnement.ax.add_patch(patches.Rectangle((self.position[1], self.position[0]), 1, 1, color='black'))
        elif action == "haut" and self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])
        elif action == "bas" and self.position[0] < self.environnement.hauteur - 1:
            self.position = (self.position[0] + 1, self.position[1])
        elif action == "gauche" and self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)
        elif action == "droite" and self.position[1] < self.environnement.largeur - 1:
            self.position = (self.position[0], self.position[1] + 1)
        elif action == "auto_pilot":
            #keep looping until the agent has finished
            while not self.agir("verifier"):
                def get_choice():
                    choice = random.choice(["gauche", "droite", "bas", "haut"])
                    if choice == "gauche" and self.position[1] == 0:
                        print("[gauche] impossible car le mur est à gauche")
                        return get_choice()
                    elif choice == "droite" and self.position[1] == self.environnement.largeur - 1:
                        print("[droite] impossible car le mur est à droite")
                        return get_choice()
                    elif choice == "haut" and self.position[0] == 0:
                        print("[haut] impossible car le mur est en haut")
                        return get_choice()
                    elif choice == "bas" and self.position[0] == self.environnement.hauteur - 1:
                        print("[bas] impossible car le mur est en bas")
                        return get_choice()
                    else: 
                        return choice
                self.agir(get_choice())
                if self.percevoir():
                    self.agir("aspirer")
                self.apprendre()
                plt.pause(0.1)

        elif action == "verifier":
            #if all cells has been visited, the agent has finished
            if len(self.historique) == self.environnement.largeur * self.environnement.hauteur:
                print("fini")
                return True
            else:
                print("pas fini")
                return False
        self.environnement.afficher_agent(self.position)
    
    def apprendre(self):
        #if the cell isn't in the history, add it
        if self.position not in self.historique: 
            self.historique.append(self.position)