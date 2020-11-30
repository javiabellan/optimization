Analítica prescriptiva / Investigación operativa / optimización combinatoria / programación entera

> ### *Mediante la analítica prescriptiva se consiguen recomendaciones sobre las acciones que se han de seguir para reducir costes o mejorar los beneficios.*

# Optimization paradigms segun coursera
1. Greedy: Solución a mano
2. Global techinques: Techniques that are guaranteed to find the optimal solution if you give the enough time.
   - Dynamic Programming (**DP**) (backtracking and branch & bound)
   - Constraint Programming (**CP**)
   - Mixed Integer Programming (**MIP**)
   - Linear Programming (**LP**) ??? (no se si va aquí)
3. Local Search (**LS**): Scale very well with problems of large size (may not give you the best solution).
4. Hybrids: Combina lo mejor de Global y Local.




### Constraint Programming
> - Discrete math
> - Like solving puzzles
> - Lots of logic

CP is branch and pruning:

Pruning: Reduce the search sapce as much as possible.


Propagation engine:

```python
for c in contraints:
    if c_is_feasible:
        # apply the prunning associated with c
    else:
        return failure
return success
```

Modela tu problema lo mejor posible (contraints) para que el solver lo resuleva

### Mixed Integer Programming
- Continuous math
- Linear algebra

### Local Search
- Intuition based, most significant coding
- Writing efficient code really helps
- Lost of staring at the terminal


---

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





# Problema Np-Completo
Cumple
- Es muy rápido de checkear si la solucion propuesta es correcat
- Si sabes resolver un problema NP-Completo, sabesresolverlos todos
- Existe el mito de que se resuelven con coste exponencial




# Ejemplos

> - **Feasibily Problems**: Any solution meeting all the criteria is acceptable.
> - **Optimization Problems**: Find the best solution that satisfies the criteria.


### Feasibily Problems
- Sudoku
- N queens
- Cryptarithmetic


### Optimization Problems
- Knapsack (Problema de la mochila)
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



### Optimization Problems approach

1. Traducir el problema de negocio a un problema de optimización
   Identificar Variables de decisión.
   - Hora que empieza.
   - Hora que acaba.
   - Tarea que hace en el minuto 3
   - Tarea que hace en el minuto 4

2. Normalemete se acaban con muchas soluciones que igualan la mejor función objetivo
   - Recomendable: Añadir funciones objetivo secundarias hasta que queden pocas soluciones e idelamente una unica solucion. Ejemplo de turnos

   Funcion pricipal: Encajar horarios
   Fucion Scundaria: Que esten más contentos con su horario



# Referencias

- https://www.coursera.org/learn/discrete-optimization
- https://www.gestiondeoperaciones.net
- https://medium.com/@AlainChabrier/scheduling-with-constraint-programming-35a23839e25c

### Librerias
- Python
  - [Google OR Tools](https://developers.google.com/optimization)
  - [PuLP](https://github.com/coin-or/pulp)
- Para Constraint Programming sin dudarlo **Choco Solver**. Open Source. Java
- Para Local Search **Optaplanner**. Open Source.
- Para Mixed Integer Programming no hay nada open source y bueno.
  - Pero CPLEX, de IBM, tiene una versión community limitada por tamaño de problema.
