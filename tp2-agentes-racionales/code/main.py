from ReflexAgent import*
from Environment import*


def main():
    suciedad = [0.1,0.2,0.4,0.8]
    dimensiones = [2,4,8,16,32,64,128]
    #[2,4,8,16,32,64,128]
    #[0.1,0.2,0.4,0.8]

    print("Agente Reflexivo aleatorio")

    for dimension in dimensiones:
        print(f"Medida de rendimiento entorno {dimension}x{dimension} ")
        for dirt_rate in suciedad:
            print(f"dirt_rate = {dirt_rate}: ", end='')
            env = Environment(dimension,dimension,random.randint(0,dimension-1),random.randint(0,dimension-1),dirt_rate)
            agent = ReflexAgent(env)
            #env.print_environment()
            for i in range(0,9):
                agent.think()
                #env.print_environment() 
            
            result = env.get_performance()
            promedio_rendimiento = result/10
            print(f"{result}")
            print(f"rendimiento promedio: {promedio_rendimiento}\n")
    
    

if __name__=="__main__":
    main()
    




