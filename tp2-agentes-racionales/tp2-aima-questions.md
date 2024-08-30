<h1>Ejercicio 6</h1>

<h1>2.10) Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement </h1>

a. Can a simple reflex agent be perfectly rational for this environment? Explain.

- No, porque para eso el agente tendría que ser capaz de tomar decisiones que maximicen su medición de desempeño moviéndose solo a casilleros que no ha visitado antes o recorriendo un camino específico hasta alcanzar una casilla nueva pero por ser un agente reflexivo simple no cuenta con una memoria que le permita conocer cuales son las casillas que aún no ha visitado por lo que se va a ir moviendo por todo el espacio de trabajo sin distinguir casillas nuevas de casillas ya visitadas.

b. What about a reflex agent with state? Design such an agent.

- En este caso sí porque el agente de reflejo basado en modelos mantiene un estado interno que le permite ver un modelo del mundo en el que está y gracias a esto puede seleccionar decisiones que en cada paso maximicen su medición de desempeño independientemente de que se penalice cada movimiento del agente, ya que cada movimiento va a ser útil para alcanzar el objetivo deseado 

c. How do your answers to a and b change if the agent’s percepts give it the clean/dirty status of every square in the environment?

- El agente de la pregunta a sería racional ya que podría adaptarse para que se mueva solo a las casillas sucias, evite movimientos redundantes y mejore la toma de decisiones y el agente de b sería mucho más eficiente porque no solo va a saber cuales son las casillas ya recorridas sino que podrá dirigirse directamente a las casillas sucias para cumplir con el objetivo.

<h1>2.11)Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)</h1>

a. Can a simple reflex agent be perfectly rational for this environment? Explain

- El agente no puede ser perfectamente racional porque como desconoce su entorno puede tomar decisiones que lo hagan chocar con obstáculos, salirse de los límites del entorno o moverse por casillas que no contienen suciedad, finalizando así su ejecución sin alcanzar el objetivo. Esto sucede porque al ser el entorno desconocido por el agente este no puede tomar decisiones que le permitan maximizar la medición de su desempeño.

b. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments.

- Sí, se puede lograr una mejor performance implementando un agente de reflejo simple que use una función aleatoria para determinar el próximo movimiento ya que esto permitiría que se visiten diferentes áreas del entorno evitando un comportamiento repetitivo e incluso los movimientos podrían evitar posibles coaliciones con los obstáculos desconocidos.

c. Can you design an environment in which your randomized agent will perform poorly? Show your results

- En este caso, habría que considerar un entorno en el que la aleatoriedad de los movimientos del agente no sean eficientes lo que impediría completar el objetivo del agente. Esto podría ocurrir en entornos muy grandes donde hay poca suciedad y no se concentra solo en una zona entonces el agente tomaría muchos pasos para poder limpiar toda el área asignada, también sucedería si además en el entorno hay muchos obstáculos lo que podría generar movimientos redundantes.

d. Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?

- Si lo puede superar porque el agente con estados toma decisiones más precisas a la hora de escoger el próximo movimiento 
