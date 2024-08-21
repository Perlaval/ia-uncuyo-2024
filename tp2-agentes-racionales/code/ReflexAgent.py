from Environment import Environment
import random

#env = Environment

class ReflexAgent():
    def __init__(self,env):
        self.env = env
        

    def up(self):
        if self.env.agent_posy > 0:
            self.env.agent_posy -= 1

    def down(self):
        if self.env.agent_posy < self.env.sizey - 1:
            self.env.agent_posy += 1

    def left(self):
        if self.env.agent_posx > 0:
            self.env.agent_posx -= 1
            

    def right(self):
        if self.env.agent_posx < self.env.sizex - 1:
            self.env.agent_posx += 1
            

    
    def suck(self):
        self.env.grilla[self.env.agent_posx][self.env.agent_posy] = False
        self.env.performance += 1

    def idle(self):
        pass

    def perspective(self): #devuelve el estado actual del recuadro en el que se encuentra
        return self.env.grilla[self.env.agent_posx][self.env.agent_posy]
        #True = sucio
        #False = limpio


    def think(self):
        if self.perspective():
            self.suck()
        else:
            actions = ["up","down","left","right"]
            action = random.choice(actions)
            getattr(self,action)() #accede al metodo(segundo parametro) de la clase que se le indica en el 1er parametro

env = Environment(128,128,1,1,0.8)
agent = ReflexAgent(env)
#env.print_environment()

for i in range(0,10):
    agent.think()
    #env.print_environment()

print(f"Medida de rendimiento: {env.get_performance()}")

