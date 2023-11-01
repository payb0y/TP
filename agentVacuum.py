from agent import Agent
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import time

class AgentAspirateur(Agent):
    def __init__(self, environnement):
        super().__init__(environnement)
        self.position = (0, 0)
        self.historique = []
        self.start_position = self.position
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
        elif action == "retourner_start":
            while self.position != self.start_position:
                if self.position[0] < self.start_position[0]:
                    self.position = (self.position[0] + 1, self.position[1])
                elif self.position[0] > self.start_position[0]:
                    self.position = (self.position[0] - 1, self.position[1])
                elif self.position[1] < self.start_position[1]:
                    self.position = (self.position[0], self.position[1] + 1)
                elif self.position[1] > self.start_position[1]:
                    self.position = (self.position[0], self.position[1] - 1)
                self.environnement.afficher_agent(self.position)
                plt.pause(0.1)
        elif action == "auto_pilot":
            start_time = time.time()
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
            self.agir("retourner_start")
            end_time = time.time()

            print(f"Temps d'exécution: {(end_time - start_time):.2f} secondes")
            print("L'agent a fini de nettoyer la grille")

        elif action == "verifier":
            return len(self.historique) == self.environnement.largeur * self.environnement.hauteur
        
        self.environnement.afficher_agent(self.position)
    
    def apprendre(self):
        if self.position not in self.historique: 
            self.historique.append(self.position)