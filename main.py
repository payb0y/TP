from agentVacuum import AgentAspirateur
from environmentVacuum import EnvironmentVacuum
import matplotlib.pyplot as plt


def main():
    agent_aspirateur = AgentAspirateur(environnement)
    environnement.afficher() 
    
    agent_aspirateur.agir("auto_pilot")

    plt.show() 
if __name__ == "__main__":
    main()