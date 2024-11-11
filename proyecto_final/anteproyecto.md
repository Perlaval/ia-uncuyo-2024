<h1>Algoritmos de búsqueda local  para jugar Tetris</h1>

**Código del proyecto:** TETRIS  
**Integrantes:** Valerio Perla, Perea Trinidad

## Descripción

El proyecto consistirá en desarrollar un agente que juegue al Tetris utilizando técnicas de búsqueda local, para determinar la mejor posición para cada pieza, con el objetivo de maximizar la puntuación obtenida. Tetris es un videojuego clásico en el que el jugador debe colocar piezas geométricas que caen, conocidas como tetrominós, en un espacio de juego con el fin de completar filas. Cuando una fila se completa, desaparece y se acumulan puntos. La dificultad radica en ubicar las piezas de manera eficiente para evitar que el espacio de juego se llene antes de completar una línea, lo que termina la partida.

<p align="center">
  <img src="https://github.com/Perlaval/ia-uncuyo-2024/raw/main/proyecto_final/images/juego.jpg" alt="Descripción de la imagen" style="width: 77%; height: auto;"  />
</p>

El juego de Tetris sobre el cual se realizarán las pruebas lo desarrollaremos usando la biblioteca pygame, la cual es una librería para el desarrollo de juegos en 2D con lenguaje de programación python. A continuación se especifica cómo se puntúan los movimientos y objetivos cumplidos:

- Se obtienen más puntos en el juego cuando se completan varias líneas a la vez (el mínimo es 1 línea y el máximo es 4\)

- A lo largo del juego, al aumentar la velocidad también aumenta el puntaje que se obtiene al completar líneas

* Puntos Base:

  - 1 línea: 100 puntos.   
  - 2 líneas: 200 puntos.   
  - 3 líneas: 400 puntos.   
  - 4 líneas: 800 puntos

### Objetivo

El objetivo principal del proyecto será implementar un agente que, dada la secuencia de piezas que caen, utilice los algoritmos de búsqueda local: Simulated Annealing y Algoritmo Genético, para determinar la mejor posición para colocar cada pieza y maximizar la puntuación de acuerdo con las reglas del juego.

### Alcance

 El alcance del proyecto estará limitado a la implementación de un algoritmo que evalúe diversas posiciones posibles y seleccione la mejor opción para cada pieza, con el fin de optimizar la jugabilidad.

### Limitaciones

Al jugar al tetris los algoritmos tendrán un tiempo determinado para poder tomar las decisiones antes de que la pieza se posicione sobre el lugar elegido por lo que puede haber un conflicto con el tiempo de cómputo de cada algoritmo 

### Forma de evaluación de los resultados

Para medir el rendimiento usaremos como base los resultados obtenidos de un agente que implementa el algoritmo de búsqueda local, Hill Climbing, y evaluaremos las siguientes métricas:

- Puntaje obtenido   
- Número de filas eliminadas  
- Número de movimientos antes de perder

A partir de los resultados obtenidos del algoritmo base podremos evaluar que tan bien se están cumpliendo los objetivos y si se ha logrado superar valores base obtenidos del algoritmo de Hill Climbing.

## Justificación
Implementar un agente que juegue al Tetris utilizando algoritmos de búsqueda local es interesante por varias razones. La primera es que Tetris es un juego que no requiere habilidades cognitivas complejas, pero sí de una estrategia para organizar y adaptar las piezas a las configuraciones posibles del tablero. Con el uso de Hill Climbing como algoritmo base, el agente puede explorar las posiciones óptimas para cada pieza y maximizar su rendimiento en términos de puntuación, por ello, consideramos que es una buena medida inicial para poder evaluar el rendimiento de los algoritmos: Simulated annealing y Genético, que ofrecen al agente la capacidad de explorar una gama más amplia de soluciones, esperando que estos últimos puedan superar o alcanzar los resultados de las métricas obtenidas por el algoritmo base.

## Listado de actividades a realizar

1. Ampliación de los conocimientos previos sobre algoritmos de búsqueda local y técnicas de optimización a través de investigación complementaria **\[2 días\]**  
2. Revisión de la documentación y desarrollo del juego Tetris **\[3 días\]**  
3. Desarrollo del algoritmo base (Hill Climbing) **\[4 días\]** 

   3.1. Implementación del algoritmo de Hill Climbing para determinar las mejores posiciones de las piezas  
   3.2. Definición de la función de evaluación que calcule la puntuación basada en la ubicación de las piezas 

4. Implementación de Simulated Annealing y Algoritmo Genético **\[14 días\]**

   4.1. Desarrollo y ajuste de Simulated Annealing teniendo en cuenta el factor tiempo para la toma de decisiones  
   4.2. Desarrollo y ajuste del Algoritmo Genético teniendo en cuenta el factor tiempo para la toma de decisiones 

5. Pruebas y comparación de soluciones entre los algoritmos **\[3 días\]**  
6. Recopilación y análisis de métricas de rendimiento **\[4 días\]**  
7. Elaboración de gráficos y visualización de resultados **\[2 días\]**  
8. Elaboración del informe final **\[7 días\]**  
9. Elaboración de la presentación del proyecto **\[1 día\]**

## Cronograma Gantt

![](https://github.com/Perlaval/ia-uncuyo-2024/raw/main/proyecto_final/images/cronogramaGantt.png)

## Referencias

[https://nlp.fi.muni.cz/aiproject/ui/kuna\_karol2016/tetris-documentation.pdf](https://nlp.fi.muni.cz/aiproject/ui/kuna_karol2016/tetris-documentation.pdf)

[https://codemyroad.wordpress.com/2013/04/14/tetris-ai-the-near-perfect-player/](https://codemyroad.wordpress.com/2013/04/14/tetris-ai-the-near-perfect-player/)

[https://cs229.stanford.edu/proj2012/BodoiaPuranik-ApplyingReinforcementLearningToCompetitiveTetris.pdf](https://cs229.stanford.edu/proj2012/BodoiaPuranik-ApplyingReinforcementLearningToCompetitiveTetris.pdf)

[https://www.pygame.org/news](https://www.pygame.org/news)

[https://noob.fandom.com/es/wiki/Tetris\#:\~:text=El%20Tetris%3A%20Se%20obtiene%20m%C3%A1s,m%C3%A1s%20l%C3%ADneas%20acumuladas%2C%20mejor%20puntaje](https://noob.fandom.com/es/wiki/Tetris#:~:text=El%20Tetris%3A%20Se%20obtiene%20m%C3%A1s,m%C3%A1s%20l%C3%ADneas%20acumuladas%2C%20mejor%20puntaje).

