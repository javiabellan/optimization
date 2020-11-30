![](img/title.jpg)

`Analítica prescriptiva` / `Investigación operativa` / `Optimización combinatoria` / `Programación entera`

> ### *Mediante la analítica prescriptiva se consiguen recomendaciones sobre las acciones que se han de seguir para reducir costes o mejorar los beneficios.*

# Optimization paradigms
1. Greedy: Solución a mano
2. Global techinques: Techniques that are guaranteed to find the optimal solution if you give the enough time.
   - Dynamic Programming (**DP**) (backtracking, branch & bound)
   - Constraint Programming (**CP**)
   - Linear Programming (**LP**)
     - Programación lineal continua: Simplex
     - Programación lineal entera (discreta): Simplex Lineal Entero
   - Programación no lineal ???
   - Mixed Integer Programming (**MIP**)
3. Local Search (**LS**): Scale very well with problems of large size (may not give you the best solution).
4. Hybrids: Combina lo mejor de Global y Local.

| Tecnicas           | Puntos Fuertes               |
|--------------------|------------------------------|
| ![](img/pasos.png) | ![](img/best_techniques.png) |



# Greedy

### Greedy solutions for common problems
- **Travelling Salesman Problem**: At each step of the journey, visit the nearest unvisited city.
- **Knapsack**: Sort items in decreasing order of value per weight (V/W), then insert them into the sack in that order until there is no space.


# Constraint Programming (CP)
> - Discrete math
> - Like solving puzzles
> - Lots of logic


> ### REMEMBER: The more constraints you add to your model, the faster the computation will be.

Modela tu problema lo mejor posible (contraints) para que el solver lo resuleva

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

### Global Constraints

Gobal constraints make it possible to detect infeasibilities earlier.

- **AllDifferent(array_of_decision_variables)**: Indicates that all items of the list must be different.

### Symmetry-breaking Constraints
Eliminate symmetries and reduce the search space size. Example:
- Days to record a scene in a movie



# Linear Programming (LP)

Lineal significa que tanto las restricciones como la funcion objetivo son lineales


# Mixed Integer Programming (MIP)
- Continuous math
- Linear algebra

# Local Search
- Intuition based, most significant coding
- Writing efficient code really helps
- Lost of staring at the terminal

### **Metaheuristicas**: Siempre tiene una solución en la mano.
- Muchas soluciones: Algoritmo genéticos
- Una única solución y hacer pequeñas soluciones en esa solución.
  - Tabu Search
  - Simulated Annealing
  
---



> ### Un problema NP-Completo cumple
> - Es muy rápido de checkear si la solucion propuesta es correcta.
> - Si sabes resolver un problema NP-Completo, sabes resolverlos todos.
> - Existe el mito de que se resuelven con coste exponencial.




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
- https://www.coursera.org/learn/delivery-problem
- https://www.gestiondeoperaciones.net
- https://medium.com/@AlainChabrier/scheduling-with-constraint-programming-35a23839e25c


### Competiciones

- Kaggle Santa 🎅🏻
  - [Traveling Santa Problem](https://www.kaggle.com/c/traveling-santa-problem) 2012
  - [Helping Santa's Helpers](https://www.kaggle.com/c/helping-santas-helpers) 2014
  - [Santa's Stolen Sleigh](https://www.kaggle.com/c/santas-stolen-sleigh) 2015
  - [Santa's Uncertain Bags](https://www.kaggle.com/c/santas-uncertain-bags) 2016
  - [Santa Gift Matching Challenge](https://www.kaggle.com/c/santa-gift-matching) 2017
  - [Traveling Santa 2018: Prime Paths](https://www.kaggle.com/c/traveling-santa-2018-prime-paths) 2018
  - [Santa 2019: Revenge of the Accountants](https://www.kaggle.com/c/santa-2019-revenge-of-the-accountants) 2019
  - [Santa's Workshop Tour 2019](https://www.kaggle.com/c/santa-workshop-tour-2019) 2019
- Hash Code
  - [Hash Code Kaggle Archive: Drone Delivery](https://www.kaggle.com/c/hashcode-drone-delivery): Can you help coordinate the drone delivery supply chain?
  - [Hash Code Kaggle Archive: Photo Slideshow Optimization](https://www.kaggle.com/c/hashcode-photo-slideshow): Optimizing a photo album from Hash Code 2019
- ROADEF: Bastante complicada.
  - [ROADEF 2020](https://www.roadef.org/challenge/2020)
  - [ROADEF 2018](https://www.roadef.org/challenge/2018)
  
  
### Librerias
- Python
  - [Google OR Tools](https://developers.google.com/optimization)
  - [PuLP](https://github.com/coin-or/pulp)
- Para Constraint Programming sin dudarlo **Choco Solver**. Open Source. Java
- Para Local Search **Optaplanner**. Open Source.
- Para Mixed Integer Programming no hay nada open source y bueno.
  - Pero CPLEX, de IBM, tiene una versión community limitada por tamaño de problema.
