from agent import Agent
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import time

#dictionary with current position and state

class AgentAspirateur(Agent):
    def __init__(self, environnement):
        super().__init__(environnement)
        self.current_position = (0, 0)
        self.historique = []
    def percevoir(self):
        return self.environnement.grid[self.current_position[0]][self.current_position[1]] == 1


    def agir(self, action):
        if action == "aspirer":
            self.environnement.grid[self.current_position[0]][self.current_position[1]] = 0
            self.environnement.ax.add_patch(patches.Rectangle((self.current_position[1], self.current_position[0]), 1, 1, color='black'))
        elif action == "haut" and self.current_position[0] > 0:
            self.current_position = (self.current_position[0] - 1, self.current_position[1])
        elif action == "bas" and self.current_position[0] < self.environnement.hauteur - 1:
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
        elif action == "gauche" and self.current_position[1] > 0:
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
        elif action == "droite" and self.current_position[1] < self.environnement.largeur - 1:
            self.current_position = (self.current_position[0], self.current_position[1] + 1)
        elif action == "retourner_start":
            while self.current_position != self.start_position:
                if self.current_position[0] < self.start_position[0]:
                    self.current_position = (self.current_position[0] + 1, self.current_position[1])
                elif self.current_position[0] > self.start_position[0]:
                    self.current_position = (self.current_position[0] - 1, self.current_position[1])
                elif self.current_position[1] < self.start_position[1]:
                    self.current_position = (self.current_position[0], self.current_position[1] + 1)
                elif self.current_position[1] > self.start_position[1]:
                    self.current_position = (self.current_position[0], self.current_position[1] - 1)
                self.environnement.afficher_agent(self.current_position)
                plt.pause(0.1)
        elif action == "auto_pilot":
            plt.pause(10)
            start_time = time.time()
            while not self.agir("verifier"):
                def get_choice():
                    choice = random.choice(["gauche", "droite", "bas", "haut"])
                    if choice == "gauche" and self.current_position[1] == 0:
                        print("[gauche] impossible car le mur est à gauche")
                        return get_choice()
                    elif choice == "droite" and self.current_position[1] == self.environnement.largeur - 1:
                        print("[droite] impossible car le mur est à droite")
                        return get_choice()
                    elif choice == "haut" and self.current_position[0] == 0:
                        print("[haut] impossible car le mur est en haut")
                        return get_choice()
                    elif choice == "bas" and self.current_position[0] == self.environnement.hauteur - 1:
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
        
        self.environnement.afficher_agent(self.current_position)
    
    def apprendre(self):
        if self.current_position not in self.historique: 
            self.historique.append(self.current_position)