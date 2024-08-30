import random


class Environment():
    def __init__(self,sizex,sizey,init_posx,init_posy,dirt_rate):
        self.sizex = sizex
        self.sizey = sizey
        self.agent_posx = init_posx
        self.agent_posy = init_posy
        self.dirt_rate = dirt_rate

        #definimos la grilla
        
        self.grilla = [[random.random() < dirt_rate for i in range(0,sizex)] for j in range(0,sizey)]
        
        #medida de rendimiento: premia con un punto al agente por cada recuadro que limpia en un periodo de tiempo concreto

        self.performance = 0


    def is_dirty(self):
        if self.grilla[self.agent_posx][self.agent_posy] is True:
            return True 
        return False

    def acept_action(self,action):
        flag = False

        if action == "arriba" and self.agent_posy > 0:
            self.agent_posy -= 1
            flag = True

        elif action == "abajo" and self.agent_posy < self.sizey-1:
            self.agent_posy += 1
            flag = True

        elif action == "izquierda" and self.agent_posx > 0:
            self.agent_posx -= 1
            flag = True

        elif action == "derecha" and self.agent_posx < self.sizex-1:
            self.agent_posx += 1
            flag = True

        elif action == "limpia":
            self.grilla[self.agent_posx][self.agent_posy] = False
            self.performance += 1
        

    def get_performance(self):
        return self.performance

    def print_environment(self):

        for y in range(self.sizey):
            row = ""
            for x in range(self.sizex):
                if x == self.agent_posx and y == self.agent_posy:
                    row += "A" #en esta posicion se encuentra el Agente
                elif (self.grilla[x][y]):
                    row += "* " # "*" indica que el recuadro esta sucio
                else:
                    row += ". " # "." indica que el recuadro esta limpio
            print(row)
            
        print() #salto de linea

# env = Environment(5,5,2,2,0.5)
# env.print_environment()
# actions = ["arriba","abajo","derecha","izquierda"] #limpiar, noHacerNada
# for i in range(10):
#     action = random.choice(actions)
#     env.acept_action(action)
#     env.print_environment()
# print(f"Medida de rendimiento: {env.get_performance()}")









