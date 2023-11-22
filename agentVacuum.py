from agent import Agent
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import time


class AgentAspirateur(Agent):
    def bfs(self,target):
        # Initialize the queue with the start position
        queue = [self.current_position]
        visited = set()
        path = []

        while queue:
            position = queue.pop(0)
            if position not in visited:
                visited.add(position)
                path.append(position)
                if position == target:
                    break
                # Add adjacent positions to the queue
                # Check if the new position is within the grid and not already visited
                x, y = position
                if x > 0 and (x - 1, y) not in visited:
                    queue.append((x - 1, y))
                if y > 0 and (x, y - 1) not in visited:
                    queue.append((x, y - 1))
                if x < self.environnement.hauteur - 1 and (x + 1, y) not in visited:
                    queue.append((x + 1, y))
                if y < self.environnement.largeur - 1 and (x, y + 1) not in visited:
                    queue.append((x, y + 1))
        print(path)
        return path
    def dfs(self,target):
        # Initialize the queue with the start position
        stack = [self.current_position]
        visited = set()
        path = []

        while stack:
            position = stack.pop()
            if position not in visited:
                visited.add(position)
                path.append(position)
                if position == target:
                    break
                # Add adjacent positions to the queue
                # Check if the new position is within the grid and not already visited
                x, y = position
                if x > 0 and (x - 1, y) not in visited:
                    stack.append((x - 1, y))
                if y > 0 and (x, y - 1) not in visited:
                    stack.append((x, y - 1))
                if x < self.environnement.hauteur - 1 and (x + 1, y) not in visited:
                    stack.append((x + 1, y))
                if y < self.environnement.largeur - 1 and (x, y + 1) not in visited:
                    stack.append((x, y + 1))

        return path

    def __init__(self, environnement):
        super().__init__(environnement)
        self.current_position = (0, 0)
        self.historique = []
        self.start_position = self.current_position

    def percevoir(self):
        dirty_cells = []
        for x in range(self.environnement.hauteur):
            for y in range(self.environnement.largeur):
                if self.environnement.grid[x][y] == 1:  # Assuming 1 represents dirt
                    dirty_cells.append((x, y))
        return dirty_cells
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
            while self.percevoir():
                dirty_cell = self.percevoir().pop(0)
                path = self.bfs(dirty_cell)
                for position in path:
                    self.current_position = position
                    if self.percevoir():
                        self.agir("aspirer")
                    self.apprendre()
                    plt.pause(0.1)

            start_time = time.time()
            
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