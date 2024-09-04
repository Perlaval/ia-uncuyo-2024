#El agente percibe su ubicacion y si esa casilla contiene un agujero o es la meta
#Vida por defecto, 100 acciones como maximo 
#La dimension de la cuadricula se conoce de antemano 
#Las casillas permanecen solidas una vez cruzadas, y el objetivo del agente es alcanzar la meta sin caer en un agujero

import gymnasium as gym

from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import random
import Agent 

#import gym 
#from gym import spaces

def frozenLake(env):
    """
    ENTORNO 1
    env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", render_mode='human')


    ENTORNO 2
    desc=["SFFF", "FHFH", "FFFH", "HFFG"]
    S = start
    F = frozen
    H = hole
    G = goal

    cuando desc está definido no necesitamos map_name
    env = gym.make('FrozenLake-v1', desc=desc, render_mode='human')

    ENTORNO 3
    from gymnasium.envs.toy_text.frozen_lake import generate_random_map
    env = gym.make('FrozenLake-v1', desc=generate_random_map(size=8), render_mode='human')
    """

    #Obtener información del entorno
    print("Número de estados:", env.observation_space.n)
    print("Número de acciones:", env.action_space.n)

    #Ejecutar un episodio básico
    #la posicion inicial del agente es aleatoria y se define al generar el mapa 
    
    
    state = env.reset()
    print('Posición inicial del agente: ', state)
    
    done = truncated = False
    while not (done or truncated):
        action = env.action_space.sample() #accion aleatoria
        next_state, reward, done, truncated, _ = env.step(action)
        print(f"Acción: {action}, Nuevo estado: {next_state}, Recompensa: {reward}")
        print(f"¿Ganó? (encontró el objetivo): {done}")
        print(f"¿Frenó? (alcanzó el máximo de pasos posible): {truncated}\n")
        state = next_state


def frozenLakeWithAgent(agent):
    print("Número de estados:", agent.env.observation_space.n)
    print("Número de acciones:", agent.env.action_space.n)

    #Ejecutar un episodio básico
    #la posicion inicial del agente es aleatoria y se define al generar el mapa 
    
    print("Búsqueda por anchura:\n")

    state = agent.env.reset()
    print('Posición inicial del agente: ', state)
    
    lista_sol = agent.busquedaPorAnchura()

    if lista_sol != []:
        for i in range(len(lista_sol)):
            action = lista_sol[i]
            next_state, reward, done, truncated, _ = agent.env.step(action)
            print(f"Acción: {action}, Nuevo estado: {next_state}, Recompensa: {reward}")
            print(f"¿Ganó? (encontró el objetivo): {done}")
            print(f"¿Frenó? (alcanzó el máximo de pasos posible): {truncated}\n")
            state = next_state
    else: 
        print("no hay camino") 


def generate_random_map_custom(size, probabilidad):
    #la variable 'probabilidad' es la probabilidad que una casilla sea de hielo por lo que si num_aleatorio < probabilidad entonces hay agujero

    #1. verificamos que el tamaño ingresado sea par para poder definir un entorno con dimensiones pares
    if (size % 2 != 0):
        return "El tamaño de la cuadrícula debe ser un num par"
    
    #3. Definimos el un entorno del tamaño size con todos sus espacios congelados 

    map = [["F" for i in range(size)] for j in range(size)]

    #4. Ubicamos de forma alatoria los agujeros de start y goal

    map[random.randint(0,size-1)][random.randint(0,size-1)] = "S"

    i = random.randint(0,size-1)
    j = random.randint(0,size-1)

    while map[i][j] == "S":
        i = random.randint(0,size-1)
        j = random.randint(0,size-1)


    map[i][j] = "G"

    #4. colocamos los agujeros de forma aleatoria teniendo en cuenta la probabilidad
    cont = 0
    for i in range(size):
        for j in range(size):
            if map[i][j] != "S" and map[i][j] != "G":
                if random.random() < probabilidad:
                    map[i][j] = "H"
            if map[i][j] == "S":
                initial_state = cont

            cont +=1
    
    return map, initial_state


#gym.register(id = 'FrozenLakeEnv', entry_point='frozen_lake:FrozenLakeEnv')
# map = generate_random_map_custom(4,0.5)

# #env = gym.make('FrozenLake-v1', desc=map, render_mode='human')
# nuevo_limite = 10
# env = gym.make('FrozenLake-v1', desc=map, render_mode = 'human').env
# env = wrappers.TimeLimit(env,nuevo_limite)
# frozenLake(env)









