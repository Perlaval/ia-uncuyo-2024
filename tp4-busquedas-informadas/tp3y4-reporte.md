<h1>INTRODUCCIÓN</h1>

<p style="text-align: justify">Un agente inteligente es una entidad que percibe su entorno y actúa de forma autónoma para alcanzar un objetivo. En el caso de los agentes resuelve-problemas, su tarea principal es encontrar la secuencia de acciones que le permiten llegar al estado deseado y para lograrlo, el mismo debe decidir su próximo movimiento considerando las restricciones del entorno y aplicando las acciones permitidas, de modo que pueda acercarse progresivamente a su estado objetivo y resolver el problema.</p>

<p style="text-align: justify">Dicho agente puede emplear estrategias de búsqueda no informadas en las que no tiene conocimiento sobre el problema más allá de la información básica proporcionada por el entorno, de manera que termina explorando todas las posibles soluciones sin utilizar ningún conocimiento previo que le permita guiar su búsqueda para saber qué tan lejos se encuentra del objetivo. Por otro lado, también puede emplear la búsqueda informada en la que se usa conocimiento adicional o heurísticas que ayudan al agente a tomar decisiones que le acerquen al objetivo en menos pasos.</p> 

<p style="text-align: justify">En el presente trabajo práctico vamos a evaluar los resultados de un agente resuelve-problemas que utiliza tanto algoritmos de búsqueda informada (A*) como algoritmos de búsqueda no informada (BFS, DFS, FLS y UCS) para alcanzar el objetivo con el fin de analizar la eficiencia y tiempo de búsqueda y calidad de las soluciones.</p>

<h1>MARCO TEÓRICO</h1>

<p>Los agentes resolventes-problemas son un tipo de agente basado en objetivo que aunque no siempre conocen todo sobre el problema que van a solucionar, buscan secuencias de acciones que conduzcan a los estados deseables.</p>

Fases de un agente resolvente de problemas:

* Formular: Elige un objetivo y trata de satisfacerlo. Define un problema (proceso de decidir qué acciones y estados considerar).  
* Buscar: Si tiene distintas opciones inmediatas de valores desconocidos examina las diferentes secuencias posibles de acciones que le conduzcan a estados de valores conocidos, y entonces escoge la mejor secuencia.  
* Ejecutar: Ejecuta la secuencia de acciones definidos anteriormente.

**Búsqueda no informada**: consiste en la selección e implementación de estrategias de búsqueda de un estado solución a partir de un estado inicial sin introducir al algoritmo de solución conocimiento sobre el impacto de las transiciones en la exploración del espacio de estados. Algunos métodos son:

- Búsqueda en anchura (BFS): La búsqueda en anchura (BFS, breadth-first search) provee un algoritmo simple (basado en el recorrido de árboles por niveles) para encontrar un estado solución desde un estado inicial  
  Al implementarse mediante el recorrido por niveles, se requiere una estructura cola (FIFO, first-in, first-out)  
- Búsqueda en profundidad (DFS): se basa en el método de recorrido de árboles en profundidad. Algoritmo pre-orden  
  Al implementarse enversión iterativa requiere una estructura tipo pila (LIFO, last-in, first-out).   
- Búsqueda en profundidad limitada (DLS): es una modificación del algoritmo de búsqueda primero en profundidad (DFS) que trata de limitar el avance del algoritmo por ramas que no conducen a un estado solución  
  Su estrategia consiste en especificar una profundidad máxima de exploración y truncar la expansión de los nodos de un nivel dado hacia sus hijos, cuando esa expansión supera el límite establecido  
- Búsqueda de costo uniforme (UCS):  explora los nodos en función de su costo de ruta desde el nodo raíz. La estrategia consiste en expandir el estado n solo si g(n) (costo total del recorrido del estado inicial al nodo n) es mínimo

**Búsqueda informada**: utiliza una función heurística, que mide el coste estimado más barato desde el nodo n a un nodo objetivo. Esta función permite guiar el proceso haciendo que en cada momento se seleccione el estado o las operaciones más prometedoras. 

- Búsqueda A*: Es una mejora desarrollada a los postulados del algoritmo Dijsktra que se encarga de encontrar rutas más cortas dentro de un grafo. En esta modificación se toma como punto central la observación de búsquedas informadas dentro del grafo que nos permitan tomar decisiones óptimas sobre los caminos que deben tomarse para recorrer de forma eficiente el grafo.

<h1>DISEÑO EXPERIMENTAL</h1> 

Las pruebas se hicieron sobre el entorno (determinista) FrozenLake de la biblioteca gymnasium de python modificado de la siguiente manera:

1. Se definió la función generate\_random\_map\_custom para crear un entorno determinista, aleatorio, de 100 × 100, cuyas celdas representen un obstáculo para el agente (agujeros en el hielo) con probabilidad 0,08.   
2. Se modificó la vida del agente a 1000 acciones


Para este entorno implementamos un agente basado en objetivos de manera que que dado un punto de inicio y un punto destino, encuentre el camino óptimo (si es posible) considerando los siguientes escenarios:

- Escenario 1: Cada acción tiene costo 1\.   
- Escenario 2: Las acciones tienen como costo asociado un entero más que el que representa a la acción, es decir, moverse a la izquierda tiene costo 1, moverse hacia abajo tiene costo 2, etc. 

El agente debía capaz de resolver el problema planteado mediante los siguientes algoritmos de búsqueda no informada:   
1. Búsqueda por Anchura.   
2. Búsqueda por Profundidad.   
3. Búsqueda por Profundidad Limitada (límite \= 10).   
4. Búsqueda de Costo Uniforme.

y el algoritmo de búsqueda informada:  

5. Búsqueda A*

Para finalizar se ejecutó un total de 30 veces cada algoritmo en escenarios aleatorios con las características descritas anteriormente.

<h1>ANÁLISIS Y DISCUSIÓN DE LOS RESULTADOS</h1>

A continuación se presentan la media y la desviación estándar de la cantidad de estados explorados para llegar al objetivo, el costo de las acciones tomadas para las soluciones obtenidas y el tiempo empleado (segundos). Esto es, tomando en cuenta los resultados obtenidos en cada uno de los algoritmos.

1) Media de estados explorados: 2698.6190476190477

   Desviación estándar: 2458.091952231047

2) Media del costo total (e1): 221.7304964539007

   Desviación estándar: 278.25945958590063

3) Media del tiempo: 9.545045415560404

   Desviación estándar: 20.01787163692735

En todos los casos podemos ver como la desviación estándar se aleja considerablemente de la media y esto nos indica que los datos están muy dispersos a lo largo de un rango amplio de comparación con el valor de la media lo que quiere decir que por ejemplo si evaluamos el caso 3 (que es el caso más notable de los 3), en el que se evalúa el tiempo, vemos que aunque los algoritmos de búsqueda le hayan permitido al agente alcanzar el objetivo hay una diferencia significativa en el tiempo empleado entre unos y otros, esto puede deberse a que un algoritmo de búsqueda no informada va ir explorando el entorno y considerando todos los estados posibles a diferencia de un algoritmo de búsqueda informada que va explorando los estados de menor costo de acuerdo a la heurística lo que hace que la búsqueda sea más eficiente y mucho más rápida que en el otro caso. 

A continuación se muestran los resultados obtenidos por medio de un gráfico de caja y bigotes:

![](https://github.com/Perlaval/ia-uncuyo-2024/blob/main/tp4-busquedas-informadas/images/diagrama%20de%20caja%20y%20bigotes.png)

En el grafico 1 (cantidad de estados explorados) vemos como se representa que el algoritmo de búsqueda no informada recorre mucho menos estados para alcanzar el objetivo en comparación con los otros algoritmos esto puede estar relacionado con lo que se expresó anteriormente con respecto al tiempo empleado por los diferentes algoritmos.

También podemos observar que, de los algoritmos de búsqueda no informada, el que toma menos tiempo de búsqueda y produce un menor costo es el algoritmo de costo de uniforme, luego podríamos decir que en cuanto eficiencia el BFS podría ser una opción después del UCS ya que emplea mucho menos tiempo y costo que el DFS el cual por ser una búsqueda en profundidad va ir explorando por una misma rama hasta que ya no tenga más opciones y esto hace no sea tan útil ya que puede estar buscando en el camino equivocado y no cambiar de rama hasta que no lo queden más estados por explorar lo que es muy poco eficiente en entornos muy grandes.

<h1>CONCLUSIONES</h1>  

En general podemos observar que el algoritmo de búsqueda más apropiado a la hora de emplear un agente resuelve-problemas es la búsqueda A\* que utiliza una función heurística a partir de la cual puede ir tomando decisiones en la que cada movimiento permite que el agente se acerque más a su objetivo esto hace que la cantidad de estados explorados sea menor por lo tanto el costo y el tiempo empleado también serán mínimos en comparación con los otros.   
En conclusión, la elección del algoritmo de búsqueda depende mucho del tamaño y las condiciones del entorno, sin embargo vemos como algunos algoritmos se comportan mejores que otros ya que logran que el agente tome decisiones que lo acerque más al objetivo en cada movimiento independientemente del entorno, como por ejemplo los algoritmos A\* y UCS.  
