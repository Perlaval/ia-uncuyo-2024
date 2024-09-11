from queue import Queue
from collections import deque
import math
import heapq
import time

class Agent():
    def __init__(self, env):
        self.env = env
        
    #ESCENARIOS POSIBLES------------------------------------------------------------------ 
    
    #hacer funcion que calcula el costo
    #costo_accion= 1 o 2
    # 1: cada acción tiene costo 1
    # 2: cada acción tiene costo asociado un entero más que el que represenat la accion

    #BUSQUEDA POR ANCHURA----------------------------------------------------------------

    def busquedaPorAnchura(self):
        start_time = time.time()
        frontera = Queue()
        cant_acciones = self.env.action_space.n
        list_acciones = list(range(cant_acciones))
        
        camino = []
        frontera.put((self.env.reset(),camino))
        no_visitar = []
        no_combinar = []
        visitados = set()
        
        while not frontera.empty():                     #done=false, reward=1 no va a pasar nunca
            (state, camino) = frontera.get()            #done=true, reward=1 ganó
                                                        #done=false, reward=0 save
            if state not in no_visitar:                 #done=true, reward=0 hoyo
                for accion in list_acciones:
                    if (state,accion) not in no_combinar:
                        self.recorrerCamino(camino)
                        new_state, reward, done, _, _ = self.env.step(accion) #partiendo del estado actual ejecuto cada una de las acciones posibles para tomar la siguiente decision
                        if new_state not in visitados:
                            if done and reward == 1:
                                end_time = time.time()           
                                #return True, len(camino), self.calcularCosto2(camino), camino + [accion]                                                            #el costo es la cantidad de pasos porque cada accion tiene cosoto 1
                                return True, len(visitados), len(camino), self.calcularCosto2(camino), end_time - start_time            #gano                                                             
                            elif not done and reward == 0:          #esta save
                                frontera.put((new_state, camino + [accion])) #se guarda en la lista una tupla y cada vez que se evalue el estado que contiene la tupla se toma el camino actualizado, en caso de que el estado solo conduzca a un hoyo entoces se descarta ese estado y se pasa al siguiente tomando el camino correspondiente 
                                visitados.add(new_state)
                            else:
                                no_combinar.append((state,accion))
                                no_visitar.append(new_state)  
                                break

        return False, 0, 0, 0, 0 #no hay ningun camino posible desde la posicion inicial hasta el objetivo 
    
    def recorrerCamino(self,camino):
        self.env.reset()
        for paso in camino:
            self.env.step(paso)
        
    #BUSQUEDA POR PROFUNDIDAD ------------------------------------------------------------------------------
        
    def busquedaPorProfundidad(self):
        start_time = time.time()
        cant_acciones = self.env.action_space.n
        list_acciones = list(range(cant_acciones))
        
        camino = []
        initial_state, _ = self.env.reset()
        
        pila = [(initial_state,camino)]
        visitados = set()
        cont = 1
        
        while pila:             
            (state, camino) = pila.pop()           
            if state not in visitados:  
                visitados.add(state)  
            for accion in list_acciones:
                new_state, reward, done, _, _ = self.env.step(accion)   #partiendo del estado actual ejecuto cada una de las acciones posibles para tomar la siguiente decision
                
                #esto tambien me ayuda a evitar que se repita un estado cuando hay una accion que no se puede ejecutar porque el agente se sale de la grilla 
                if new_state not in visitados and state != new_state:                        
                    if done:
                        if reward == 1:
                            end_time = time.time()
                            #return True, len(camino), self.calcularCosto2(camino), camino + [accion]
                            return True, len(visitados), len(camino), self.calcularCosto2(camino),  end_time-start_time  #gano
                        else:
                            visitados.add(new_state)
                            self.recorrerCamino(camino)
                            break
                    else:   
                                                            #esta save
                        pila.append((new_state, camino + [accion]))
                        visitados.add(new_state)
                else:
                    self.recorrerCamino(camino)  

            if (pila == [] and cont < 4):
                cont += 1
                camino = []
                initial_state, _ = self.env.reset()
                pila.append((initial_state,camino))
                
        
        return False, 0, 0, 0, 0 #no hay ningun camino posible desde la posicion inicial hasta el objetivo       

    #BUSQUEDA POR PROF LIMITADA -------------------------------------------------------------------------

    def busquedaPorProfLimitada(self, limit = 10):
        start_time = time.time()
        cant_acciones = self.env.action_space.n
        list_acciones = list(range(cant_acciones))
                        
        camino = []
        initial_state, _ = self.env.reset()
        depth = 0
        pila = [(initial_state,camino)]
        visitados = set()
        cont = 1
        while pila: 
                                                    #done=false, reward=1 no va a pasar nunca
            (state, camino) = pila.pop()            #done=true, reward=1 ganó
                                                    #done=false, reward=0 save
            if state not in visitados:              #done=true, reward=0 hoyo
                visitados.add(state)
                                                        
            for accion in list_acciones:
                new_state, reward, done, _, _ = self.env.step(accion)   #partiendo del estado actual ejecuto cada una de las acciones posibles para tomar la siguiente decision
                if state != new_state and new_state not in visitados: #esto tambien me ayuda a evitar que se repita un estado cuando hay una accion que no se puede ejecutar porque el agente se sale de la grilla 
                    if done:
                        if reward == 1:
                            #return True, len(camino), self.calcularCosto2(camino), camino + [accion]  #gano
                            end_time = time.time()
                            return True, len(visitados), len(camino), self.calcularCosto2(camino+[accion]), end_time-start_time
                        else:
                            visitados.add(new_state)
                            self.recorrerCamino(camino)
                            break
                    else:   
                        depth += 1                                     #esta save
                        pila.append((new_state, camino + [accion]))
                        visitados.add(new_state)
                        #break 
                else:
                    self.recorrerCamino(camino)
            
            if (depth > limit or (pila == [] and cont < 4)):
                cont += 1
                camino = []
                initial_state, _ = self.env.reset()
                pila.append((initial_state,camino))
                depth = 0            

        return False, 0, 0, 0, 0
        

    def calcularCosto2(self,path):
        costo2 = 0
        for paso in path:
            costo2 += paso+1
        return costo2  
            
        
    #COSTO UNIFORME ---------------------------------------------------------------------
    
    def busquedaCostoUniforme(self, escenario):
        start_time = time.time()
        cant_acciones = self.env.action_space.n
        list_acciones = list(range(cant_acciones))
                        
        camino = []
        initial_state, _ = self.env.reset()
        
        queue = []
        heapq.heappush(queue, (0, initial_state, camino))
        visitados = set()

                
        while queue: 
                                                            #done=false, reward=1 no va a pasar nunca
            (cost, state, camino) = heapq.heappop(queue)    #done=true, reward=1 ganó
                                                            #done=false, reward=0 save
            if state not in visitados:                      #done=true, reward=0 hoyo
                visitados.add(state)
                                                        
            for accion in list_acciones:
                
                new_state, reward, done, _, _ = self.env.step(accion)   #partiendo del estado actual ejecuto cada una de las acciones posibles para tomar la siguiente decision
                
                if state != new_state and new_state not in visitados: #esto tambien me ayuda a evitar que se repita un estado cuando hay una accion que no se puede ejecutar porque el agente se sale de la grilla 
                                        
                    if done:
                        if reward == 1:
                            #return True, cost, camino  #gano
                            end_time = time.time()
                            return True, len(visitados), cost, end_time-start_time
                        else:
                            visitados.add(new_state)
                            self.recorrerCamino(camino)
                            break                                
                    else:   
                        if escenario == 2:
                            cost += accion+1
                        else:
                            cost += 1
                                                            #esta save
                        heapq.heappush(queue, (cost, new_state, camino + [accion]))
                        visitados.add(new_state)
                        #break 
                else:
                    self.recorrerCamino(camino)

        return False, 0, 0, 0
    
    #A* --------------------------------------------------------------------------------------------
    
    def busquedaAEstrella(self):
        start_time = time.time()
        mapa = self.env.unwrapped.desc
        
        flag = False
        for x in range(len(mapa)): #obtengo el estado donde se encuentra el objetivo 
            for y in range(len(mapa[0])):
                
                if mapa[x][y] == b"G":
                    goal_state = (x,y)
                    flag = True
                    break
            if flag: 
                break
        
        cant_acciones = self.env.action_space.n
        list_acciones = list(range(cant_acciones))

        camino = []
        state, _ = self.env.reset()
        
        frontera = [(0, 0, state, camino)] 
        visitados = set()
        
        #costog = costo de ruta desde el nodo raiz al nodo actual
        #costoh = costo estimado desde el nodo n al nodo objetivo 

        while frontera:
            costo_total, costog, state, camino = heapq.heappop(frontera)

            if state not in visitados:
                visitados.add(state)

            for accion in list_acciones:
                new_state, reward, done, _, _ = self.env.step(accion)

                if new_state != state and new_state not in visitados:
                    costog_nuevo = costog+1
                    xy_new_state = self.calcularCoordenadas(new_state,mapa) #calculo las coordenadas del new_state, tupla
                    costoh = self.funcionHeuristica(xy_new_state,goal_state)
                    costo_total_nuevo = costog_nuevo+costoh #calculamos el costo 

                    if done:
                        if reward == 1: #alcanzo el obj
                            end_time = time.time()
                            return True, len(visitados), costog_nuevo, self.calcularCosto2(camino+[accion]), end_time-start_time
                        else:
                            visitados.add(new_state) #cayo en un hoyo
                            self.recorrerCamino(camino)
                            break
                            
                    else:
                        #usamos la cola de prioridad para seleccionar siempre el camino con menor costo total
                        heapq.heappush(frontera, (costo_total_nuevo, costog_nuevo, new_state, camino + [accion]))
                        visitados.add(new_state)
                else:
                    self.recorrerCamino(camino)

        return False, 0, 0, 0, 0

    def funcionHeuristica(self, state, goal_state):
        x1, y1 = state
        x2, y2 = goal_state
        return abs(x1-x2)+abs(y1-y2) #esto es para tener la distancia entre el estado actual y el objetivo


    def calcularCoordenadas(self, state, mapa):
        cont = 0

        for x in range(len(mapa)): #obtengo el estado donde se encuentra el objetivo 
            for y in range(len(mapa[0])):
                
                if cont == state:
                    return (x,y)
                cont += 1
                    
                    
                

        
        
    


        
