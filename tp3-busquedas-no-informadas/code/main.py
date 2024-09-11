from frozen_lake import*
from Agent import*
from gymnasium import wrappers
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




def main():

    # #EJERCICIO 1: ----------------------------------------------------------------------------
    # # map = generate_random_map_custom(100,0.08)
    # # nuevo_limite = 1000
    # # env = gym.make('FrozenLake-v1', desc = map, render_mode = 'human', is_slippery = False).env
    # # env = wrappers.TimeLimit(env,nuevo_limite)

    # #EJERCICIO 2 - AGENTE BASADO EN OBJETIVOS: -----------------------------------------------
    # #agent = Agent(env)
    # # frozenLakeWithAgent(agent)

    # #EJERCICIO 3 -----------------------------------------------------------------------------
    # #1. Crea un entorno determinista, aleatorio de 100x100, con probabilidad 0.8, vida = 1000 acciones
    # #2. 2. Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino ´optimo (si es posible).

    # # Ejecutar un total de 30 veces cada algoritmo en escenarios aleatorios con las características descriptas en el ejercicio 1. Evaluar cada uno de los algoritmos sobre los mismos entornos generados

    # headers = ["algorithm_name","env_n","states_n","cost_e1","cost_e2","time","solution_found"] #para despues agregarlo en el .csv
    # results_gral = []

    # envList = []

    # for i in range(30):
    #     map = (generate_random_map_custom(100,0.08))
    #     nuevo_limite = 1000
    #     env = gym.make('FrozenLake-v1', desc = map, render_mode = None, is_slippery = False).env
    #     env = wrappers.TimeLimit(env,nuevo_limite)
    #     envList.append(env)
        
    # i = 0
    # for environment in envList:
    #     agent = Agent(environment)
        
    #     found, states_n, cost1, cost2, time = agent.busquedaPorAnchura()
    #     #print(f"BFS,{i+1},{states_n},{cost1},{cost2},{time},{found}")
    #     results_gral.append(["BFS",i+1,states_n,cost1,cost2,time,found])
        
    #     found, states_n, cost1, cost2, time = agent.busquedaPorProfundidad()
    #     #print(f"DFS,{i+1},{states_n},{cost1},{cost2},{time},{found}")
    #     results_gral.append(["DFS",i+1,states_n,cost1,cost2,time,found])

    #     found, states_n, cost1, cost2, time = agent.busquedaPorProfLimitada()
    #     #print(f"DLS,{i+1},{states_n},{cost1},{cost2},{time},{found}")
    #     results_gral.append(["DLS",i+1,states_n,cost1,cost2,time,found])

    #     found, states_n, cost1, time = agent.busquedaCostoUniforme(1)
    #     #print(f"UCS_e1,{i+1},{states_n},{cost1},NaN,{time},{found}")
    #     results_gral.append(["UCS_e1",i+1,states_n,cost1,"NaN",time,found])

    #     found, states_n, cost2, time = agent.busquedaCostoUniforme(2)
    #     #print(f"UCS_e2,{i+1},{states_n},NaN,{cost2},{time},{found}")
    #     results_gral.append(["UCS_e2",i+1,states_n,"NaN",cost2,time,found])

    #     found, states_n, cost1, cost2, time = agent.busquedaAEstrella()
    #     #print(f"A*,{i+1},{states_n},{cost1},{cost2},{time},{found}")
    #     results_gral.append(["A*",i+1,states_n,cost1, cost2, time,found])

    #     i+=1
    

    # with open('resultados1.csv', mode="w", newline="") as file:
    #     writer = csv.writer(file)

    #     writer.writerow(headers) 

    #     for result in results_gral:
    #         writer.writerow(result)

    #MEDIANA Y DESVIACION ESTANDAR ---------------------------------------------------------------
    df = pd.read_csv('resultados.csv')

    #df_solved es el DataFrame que contiene los datos a graficar
    df_solved = df[df['solution_found'] == True] #filtramos las filas donde hay datos
    
    #calcula la media y la desviacion estandar
    mean_states = df_solved['states_n'].mean() 
    std_states = df_solved['states_n'].std() 

    mean_cost_e1 = df_solved['cost_e1'].mean()
    std_cost_e1 = df_solved['cost_e1'].std()

    mean_time = df_solved['time'].mean()
    std_time = df_solved['time'].std()

    #Muetra los resultados
    print(f"Media de estados explorados: {mean_states}, Desviación estándar: {std_states}")
    print(f"Media del costo total (e1): {mean_cost_e1}, Desviación estándar: {std_cost_e1}")
    print(f"Media del tiempo: {mean_time}, Desviación estándar: {std_time}")

    #GRAFICOS ------------------------------------------------------------------

    plt.figure(figsize=(14, 8))

    # Boxplot - cantidad de estados explorados
    plt.subplot(1, 3, 1)
    sns.boxplot(x='algorithm_name', y='states_n', data=df_solved)
    plt.title('Cantidad de estados explorados')
    plt.xlabel('algorithm_name')
    plt.ylabel('Estados explorados')
    
    # # Boxplot - costo total
    plt.subplot(1, 3, 2)
    sns.boxplot(x='algorithm_name', y='cost_e1', data=df_solved)
    plt.title('Costo total de las acciones (e1)')
    plt.xlabel('algorithm_name')
    plt.ylabel('Costo total')
    

    # # Boxplot - tiempo empleado
    plt.subplot(1, 3, 3)
    sns.boxplot(x='algorithm_name', y='time', data=df_solved)
    plt.title('Tiempo empleado (segundos)')
    plt.xlabel('algorithm_name')
    plt.ylabel('Tiempo (s)')
    

    # #Mostrar el gráfico
    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    main()





