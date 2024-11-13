<h1>Trabajo Práctico 2: Agentes racionales</h1>

### Ejercicio 1

## a) Jugar al CS (o cualquier otro 3d Shooter).

- Performance: obtener una alta puntuación al finalizar la partida, ganar rondas, cumplir con los objetivos de misión y minimizar muertes.  
- Environment:  mapa del juego con diferentes obstáculos, misiones, oponentes, aliados, municiones y armas.  
- Actuators: teclado, mouse, disparar, micrófonos.  
- Sensors: sonido, visualización en pantalla.

# Caraterísticas

- Parcialmente observable: El jugador solo puede ver lo que está en su campo de visión.
- Multi-agente: Permite la interacción con otros jugadores.
Estocástico: Las acciones de otros agentes y ciertos eventos pueden ser impredecibles.
- Secuencial: Cada acción depende de las anteriores.
- Dinámico: El entorno cambia constantemente.
- Continuo: Movimiento fluido en el espacio de juego.
- Conocido: Las reglas y el entorno son conocidos.

## b) Explorar los océanos

- Performance: cantidad de área desconocida que ha sido explorada, calidad de los datos recolectados, especies descubiertas, cumplimiento de objetivos de exploración.  
- Environment: océanos, vida marina, condiciones meteorológicas y oceanográficas, equipos usados para la exploración.  
- Actuators: dispositivos para recolectar muestras de agua u organismos marinos, motores y sistemas de control que permitan que el vehículo pueda moverse correctamente en el agua al realizar la exploración, cámaras fotográficas, dispositivos para transmitir datos a la superficie  
- Sensors: sensores para medir la temperatura, sensores de profundidad, sensores de movimiento

# Caraterísticas

Parcialmente observable: La visibilidad es limitada.
Agente simple: Si solo se explora sin interactuar con otros agentes.
Estocástico: Factores ambientales como corrientes marinas y condiciones meteorológicas son impredecibles.
Secuencial: Las decisiones afectan las acciones subsiguientes.
Dinámico: Cambios en el entorno por movimiento de animales o condiciones ambientales.
Continuo: Movimiento continuo en el agua.
Desconocido: Exploración de nuevos lugares sin información previa detallada.

## c) Comprar y vender tokens crypto (alguno).

- Performance: tasa de éxito de las transacciones, beneficios obtenidos, costos de operación (impuestos o tarifas), cumplimiento de la estrategia.  
- Environment: mercado de criptomonedas, regulaciones, información o eventos que pueden influir en el valor de los tokens, plataformas de intercambio.  
- Actuators: interfaz de usuario, automatización de trading.  
- Sensors: señales sobre tendencias y patrones de mercado, historial de transacciones, datos de precio.

# Caraterísticas

- Parcialmente observable: Solo se conoce información pública, mientras que factores internos de cada token pueden no ser visibles.
- Multi-agente: Competencia con otros compradores y vendedores.
- Estocástico: Los precios fluctúan de forma impredecible.
- Secuencial: Las decisiones afectan las ganancias/perdidas futuras.
- Dinámico: Cambios constantes en los precios de los tokens.
- Discreto: Las acciones (compra/venta) son discretas.
- Conocido: El funcionamiento del mercado y las reglas son conocidas.

## d) Practicar tenis contra una pared.

- Performance: cantidad de repeticiones, calidad del golpe, mantener el ritmo, tirar a un área específica, manejar la pelota en diferentes situaciones  
- Environment: pared, raqueta y pelota de tenis, espacio de práctica  
- Actuators: desplazamiento del jugador para posicionarse correctamente, movimientos de la raqueta, técnica de golpeo  
- Sensors: percepción visual, sonido, mecanismos de control del rendimiento

# Caraterísticas

- Totalmente observable: Todo el entorno es visible.
- Agente simple: Solo participa el jugador.
- Determinista: El rebote depende solo del ángulo y velocidad del golpe.
- Secuencial: Cada golpe depende de la posición actual.
- Dinámico: La pelota está en movimiento constante.
- Continuo: Movimiento continuo de la pelota.
- Conocido: Se conocen las reglas y el comportamiento de la pelota.

## e) Realizar un salto de altura.

- Performance: altura alcanzada, realizar un salto limpio, técnica de salto (aproximación, fase de despegue y técnica en el aire), consistencia en los saltos, velocidad de aproximación.  
- Environment: condiciones ambientales, área de salida, barra de salto, área de caída.  
- Actuators: movimiento de carrera, despegue, técnica de salto.  
- Sensors: monitor de rendimiento, percepción visual, sensación de impulso y fuerza durante el despegue y recepción en la zona acolchada

# PCaracterísticas

- Totalmente observable: El entorno es completamente visible.
- Agente simple: Solo el atleta participa en la acción.
- Determinista: El resultado depende de la técnica y fuerza del atleta.
- Episódico: Cada salto es una acción independiente.
- Estático: El entorno no cambia durante el salto.
- Continuo: Movimiento fluido y continuo.
- Conocido: Las reglas y condiciones son conocidas.

## f ) Pujar por un artículo en una subasta.

- Performance: ganar la subasta, que el precio pagado por el artículo sea factible en comparación con su valor real o el presupuesto estimado, efectividad de la estrategia usada.  
- Environment: otros postores, artículo que se está subastando, reglas de subasta.  
- Actuators: forma de comunicación a la hora de hacer una oferta, estrategia, tiempo para realizar la oferta  
- Sensors: información actualizada de la subasta del artículo, comportamiento de los otros postores, tiempo restante para hacer una oferta.

# Caraterísticas

- Parcialmente observable: No se conoce el límite de oferta de otros.
- Multi-agente: Interacción con otros postores.
- Estocástico: Las ofertas de otros son impredecibles.
- Episódico: Cada subasta es independiente.
- Dinámico: Las ofertas cambian con el tiempo.
- Discreto: Las ofertas son discretas.
- Conocido: Las reglas de la subasta son conocidas.