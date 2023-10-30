from environment import Grille
from agentVacuum import AgentAspirateur
import matplotlib.pyplot as plt


def main():
    environnement = Grille(5, 5)
    agent_aspirateur = AgentAspirateur(environnement)
    environnement.afficher()  # Display the initial grid

    agent_aspirateur.agir("auto_pilot")

    plt.show()  # Keep the final grid on screen

if __name__ == "__main__":
    main()