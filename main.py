from environment import Grille
from agentVacuum import AgentAspirateur
import matplotlib.pyplot as plt


def main():
    environnement = Grille(3, 3)
    agent_aspirateur = AgentAspirateur(environnement)
    environnement.afficher() 
    
    agent_aspirateur.agir("auto_pilot")

    plt.show() 
if __name__ == "__main__":
    main()