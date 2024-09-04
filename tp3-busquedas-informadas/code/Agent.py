from queue import Queue


class Agent():
    def __init__(self, env, start):
        self.env = env
        self.pos = start
        
        
        #costo_accion= 1 o 2
        # 1: cada acción tiene costo 1
        # 2: cada acción tiene costo asociado un entero más que el que represenat la accion

    def busquedaPorAnchura(self):
        frontera = Queue()
        cant_acciones = self.env.action_space.n
        list_acciones = list(range(cant_acciones))
        print(list_acciones)
                
        camino = []
        frontera.put((self.env.reset(),camino))
        no_visitar = []
        no_combinar = []
        visitados = []
        
        while not frontera.empty():             #done=false, reward=1 no va a pasar nunca
            (state, camino) = frontera.get()            #done=true, reward=1 ganó
                                                        #done=false, reward=0 save
            if state not in no_visitar:                 #done=true, reward=0 hoyo
                for accion in list_acciones:
                    if (state,accion) not in no_combinar:
                        self.recorrerCamino(camino)
                        new_state, reward, done, _, _ = self.env.step(accion) #partiendo del estado actual ejecuto cada una de las acciones posibles para tomar la siguiente decision
                                            #esto tambien me ayuda a evitar que se repita un estado cuando hay una accion que no se puede ejecutar porque el agente se sale de la grilla 
                        if new_state not in visitados:
                            if done and reward == 1:
                                print(f"Costo: {len(camino)+1}")
                                print(camino + [accion]) #el costo es la cantidad de pasos porque cada accion tiene cosoto 1
                                return camino + [accion]            #gano                                                             
                            elif not done and reward == 0:          #esta save
                                frontera.put((new_state, camino + [accion])) #se guarda en la lista una tupla y cada vez que se evalue el estado que contiene la tupla se toma el camino actualizado, en caso de que el estado solo conduzca a un hoyo entoces se descarta ese estado y se pasa al siguiente tomando el camino correspondiente 
                                visitados.append(new_state)
                            else:
                                no_combinar.append((state,accion))
                                no_visitar.append(new_state)  

        return [] #no hay ningun camino posible desde la posicion inicial hasta el objetivo 
    
    def recorrerCamino(self,camino):
        self.env.reset()
        for paso in camino:
            self.env.step(paso)
        
    def busquedaPorProfundidad():
        pass

    def busquedaPorProfLimitada():
        #límite = 10
        pass

    def busquedaCostoUniforme():
        pass



