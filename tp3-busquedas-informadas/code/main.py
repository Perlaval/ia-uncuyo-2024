from frozen_lake import*
from Agent import*
from gymnasium import wrappers

#1. Crea un entorno determinista, aleatorio de 100x100, con probabilidad 0.8, vida = 1000 acciones

def main():
    map, start = generate_random_map_custom(4,0.5)
    env = gym.make('FrozenLake-v1', desc = map, render_mode = 'human', is_slippery = False).env
    nuevo_limite = 1000
    env = wrappers.TimeLimit(env,nuevo_limite)
    agent = Agent(env,start)
    #print("hola")
    frozenLakeWithAgent(agent)
    

if __name__=="__main__":
    main()





#2. Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo (si es posible). Considere los siguientes escenarios posibles:
# Escenario 1: cada acción tiene costo 1
# Escenario 2: Las acciones tienen como costo asociado un entero m´as que el que representa a la acción, es decir, moverse a la izquierda tiene costo 1, moverse hacia abajo tiene costo 2, etc.

