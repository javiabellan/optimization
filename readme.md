Invesitigación operativa / programación entera




# Tecnicas y Algoritmos

- **Metaheuristicas**: Siempre tiene una solución en la mano.
  - Muchas soluciones: Algoritmo genéticos
  - Una única solución y hacer pequeñas soluciones en esa solución.
    - Tabu Search
    - Simulated Annealing
- **Programación por restricciones** (1)
- **Programación lineal** (2)
  - Programación lineal continua
    - Simplex (optimización global) (de caja negra)
  - Programación lineal entera (discreta)
    - Simplex Lineal Entero
- **Programación no lineal**



Ver sus pros y contras
- (1) HAY QUE PROGRAMAR DE FORMA EFICIENTE LA IMPLEMETACION
- (2) Lineal significa que tanto las restricciones como la funcion objetivo son lineales

# Librerias
- [Google OR Tools](https://developers.google.com/optimization)
- Para Constraint Programming sin dudarlo **Choco Solver**. Open Source. Java
- Para Local Search **Optaplanner**. Open Source.
- Para Mixed Integer Programming no hay nada open source y bueno.
  - Pero CPLEX, de IBM, tiene una versión community limitada por tamaño de problema.


# Curso
- https://www.coursera.org/learn/discrete-optimization
- https://www.gestiondeoperaciones.net

# Problema Np-Completo
Cumple
- Es muy rápido de checkear si la solucion propuesta es correcat
- Si sabes resolver un problema NP-Completo, sabesresolverlos todos
- Existe el mito de que se resuelven con coste exponencial

# Ejemplos

- Problema de la mochila
- Optimización de rutas
  - Pickup & delivery
    - Datos: Puntos en el mapa de regida, puntos de entrega, tiempo max de mercancía en camión
  - Dijkstra shortest path (Google Map calcular ruta)
  - Problema del viajante de comercio
- Relajación Lagrangeana (empresa eléctrica, arrancar o parar una central térmica)
- Constraint programming
  - Turnos de Madrid
  - problema de asignación de turnos
  - Procesos de aprovisonamiento, inventario...
  - Cuánto envío del almacén a la tienda

# Pasos

1. Traducir el problema de negocio a un problema de optimización
   Identificar Variables de decisión.
   - Hora que empieza.
   - Hora que acaba.
   - Tarea que hace en el minuto 3
   - Tarea que hace en el minuto 4

2. Normalemete se acaban con muchas soluciones que igualan la mejor función objetivo
   - Recomendable: Añadir funciones objetivo secundarias hasta que queden pocas soluciones e idelamente una unica solucion. Ejemplo de turnos

   Funcion pricipal: encajar horarios
   Fucion Scundaria: que esten más contentos con su horario



