![](img/title.jpg)

`Analítica prescriptiva` / `Investigación operativa` / `Optimización combinatoria` / `Programación entera`

> ### *Mediante la analítica prescriptiva se consiguen recomendaciones sobre las acciones que se han de seguir para reducir costes o mejorar los beneficios.*

# Optimization paradigms

1. **Greedy**: Solución a mano
   - **Travelling Salesman Problem**: At each step of the journey, visit the nearest unvisited city.
   - **Knapsack**: Sort items in decreasing order of value per weight (V/W), then insert them into the sack in that order until there is no space.
2. Global techinques: Techniques that are guaranteed to find the optimal solution if you give the enough time.
   - Dynamic Programming (**DP**) (backtracking, branch & bound)
   - Constraint Programming (**CP**)
   - Linear Programming (**LP**)
     - Programación lineal continua: Simplex
     - Programación lineal entera (discreta): Simplex Lineal Entero
   - Mixed Integer Programming (**MIP**)
     - Continuous math, Linear algebra,...
3. Local Search (**LS**): Scale very well with problems of large size (may not give you the best solution).
   - Tabu Search: Past moves or solutions are prohibited (tabu)
   - Simulated Annealing: Random at the beggining, deterministic at the end.
4. Hybrids: best of Global and Local.


> ### Deep learing
> - **Implicit MLE**: Backpropagating Through Discrete Exponential Family Distributions [paper](https://arxiv.org/pdf/2106.01798.pdf), [repo](https://github.com/uclnlp/torch-imle)

| Tecnicas           | Puntos Fuertes               |
|--------------------|------------------------------|
| ![](img/pasos.png) | ![](img/best_techniques.png) |



### Visualize everithing

- CP: How much it prunes?
- LS: What are the sequence of solutions? How fast it goes down?
- LP, MIP: What is the relaxation? how good is it?





---



> ### Un problema NP-Completo cumple
> - Es muy rápido de checkear si la solucion propuesta es correcta.
> - Si sabes resolver un problema NP-Completo, sabes resolverlos todos.
> - Existe el mito de que se resuelven con coste exponencial.




# Ejemplos

> - **Feasibily Problems**: Any solution meeting all the criteria is acceptable.
> - **Optimization Problems**: Find the best solution that satisfies the criteria.


### Feasibily Problems

> **DP**=Dynamic Programming, **CP**=Constraint Programming, **MIP**=Mixed Integer Programming

| Problem                                               | My solution | OR Tools Doc                                                |
|-------------------------------------------------------|:-----------:|:-----------------------------------------------------------:|
| [Cryptarithmetic](problems/Cryptarithmetic)           | CP          | [doc](https://developers.google.com/optimization/cp/cryptarithmetic) |
| [N queens](problems/N%20Queens)                       | CP          | [doc](https://developers.google.com/optimization/cp/queens) |
| [Sudoku](problems/Sudoku)                             | DP, CP      |                                                             |
| [Graph Coloring](problems/Graph%20Coloring)           | CP          |                                                             |
| [Employee Scheduling](problems/Employee%20Scheduling) | CP          | [doc](https://developers.google.com/optimization/scheduling/employee_scheduling) |
| [The Job Shop](problems/Job%20Shop)                   | CP          | [doc](https://developers.google.com/optimization/scheduling/job_shop) |


### 📍 Vehicle Routing Problems
  
| Routing problem                      | Description                                                                 | OR-Tools                                                                    |
|--------------------------------------|-----------------------------------------------------------------------------|:---------------------------------------------------------------------------:|
| **Traveling Salesman Problem (TSP)** | Visit all locations once and come back to the starting location.            | [link](https://developers.google.com/optimization/routing/tsp)              |
| **Vehicle Routing Problem (VRP)**    | A generalisation of the TSP with multiple vehicles.                         | [link](https://developers.google.com/optimization/routing/vrp)              |
| **VRP with capacity constraints**    | Vehicles have maximum capacities for the items they can carry.              | [link](https://developers.google.com/optimization/routing/cvrp)             |
| **VRP with Pickups and Deliveries**  | Each vehicle picks up items at some locations and drops them off at others. | [link](https://developers.google.com/optimization/routing/pickup_delivery)  |
| **VRP with time windows**            | Vehicles must visit the locations in specified time intervals.              | [link](https://developers.google.com/optimization/routing/vrptw)            |
| **VRP with resource constraints**    | Load and unload vehicles at the depot (the starting point).                 | [link](https://developers.google.com/optimization/routing/cvrptw_resources) |
| **VRP with dropped visits**          | When you must pay a penalty for unvisited locations.                        | [link](https://developers.google.com/optimization/routing/penalties)        |
| **Dijkstra shortest path**           | Find the shortest path between 2 locations (ej. Google Map finding route)   |                                                                             |
  
### Optimization Problems
- Knapsack (Problema de la mochila)
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



## References

- COURSE: https://www.coursera.org/learn/discrete-optimization
- BOOK: [Competitive Programming 4](https://cpbook.net/) by Steven Halim, Felix Halim
- https://www.coursera.org/learn/delivery-problem
- https://www.gestiondeoperaciones.net
- https://medium.com/@AlainChabrier/scheduling-with-constraint-programming-35a23839e25c
- [Twit de @JFPuget](https://twitter.com/JFPuget/status/1471420224721362948) recommendos for learing MILP:
  - Read the [Model Building in Mathematical Programming](https://www.amazon.com/Model-Building-Mathematical-Programming-Williams/dp/1118443330) book
  - Read the [tesis](https://depositonce.tu-berlin.de/handle/11303/1931) of [@AchterbergT](https://twitter.com/AchterbergT) If you want to know about how MILP are solved
- [cmu-comp-or](https://github.com/rkimura47/cmu-comp-or): A series of tutorials for conducting computational experiments with optimization solvers by [@rkimura47](https://twitter.com/rkimura47)

## 🎅🏻 Kaggle Santa Competitions

| Year | Competition                                                                                  | Description                       |
|------|----------------------------------------------------------------------------------------------|-----------------------------------|
| 2012 | [Traveling Santa Problem](https://www.kaggle.com/c/traveling-santa-problem)                  | Traveling salesman                |
| 2014 | [Helping Santa's Helpers](https://www.kaggle.com/c/helping-santas-helpers)                   | Job Scheduling                    |
| 2015 | [Santa's Stolen Sleigh](https://www.kaggle.com/c/santas-stolen-sleigh)                       | Routing                           |
| 2016 | [Santa's Uncertain Bags](https://www.kaggle.com/c/santas-uncertain-bags)                     |                                   |
| 2017 | [Santa Gift Matching Challenge](https://www.kaggle.com/c/santa-gift-matching)                | Maximize child-gift happiness     |
| 2018 | [Traveling Santa 2](https://www.kaggle.com/c/traveling-santa-2018-prime-paths)               | Traveling salesman on prime paths |
| 2019 | [Revenge of the Accountants](https://www.kaggle.com/c/santa-2019-revenge-of-the-accountants) | Minimizing his workshop costs     |
| 2019 | [Santa's Workshop Tour 2019](https://www.kaggle.com/c/santa-workshop-tour-2019)              |                                   |
| 2021 | [The Merry Movie Montage](https://www.kaggle.com/c/santa-2021)                               | Optimize television programming   |

- Hash Code
  - [Hash Code Kaggle Archive: Drone Delivery](https://www.kaggle.com/c/hashcode-drone-delivery): Can you help coordinate the drone delivery supply chain?
  - [Hash Code Kaggle Archive: Photo Slideshow Optimization](https://www.kaggle.com/c/hashcode-photo-slideshow): Optimizing a photo album from Hash Code 2019
- ROADEF: Bastante complicada.
  - [ROADEF 2020](https://www.roadef.org/challenge/2020)
  - [ROADEF 2018](https://www.roadef.org/challenge/2018)
  
  
## Libraries
  
#### Constraint Programming Solvers

> #### Nota de Javier Lafuente
> Para Constraint Programming sin dudarlo **Choco Solver**.

| Library            | Languaje                         | Price                      |
|--------------------|:--------------------------------:|----------------------------|
| OR-Tools (Google)  | C++ (APIs: Java, Python, & .NET) | Open Source                |
| CHOCO              | Java                             | Open Source                |
| JACOP              | Java                             | Open Source                |
| Gecode             | C++                              | Free                       |
| ILog               | Binary                           | Free with academic license |
| MiniZinc / G12     | Binary                           | Free for students          |

#### Mixed Integer Programming Solvers

> #### Nota de Javier Lafuente
> Para Mixed Integer Programming no hay nada open source y bueno. Pero CPLEX, de IBM, tiene una versión community limitada por tamaño de problema.

| Library            | Languaje  | Price                      |
|--------------------|:---------:|----------------------------|
| GLPK               | C         | Open Source                |
| LPSolve            | C         | Open Source                |
| BCP                | C++       | Open Source                |
| CBC                | C++       | Open Source                |
| CPLEX (IBM)        | Binary    | Free with academic license |
| Gurobi             | Binary    | Free with academic license |
| SCIP               | Binary    | Free for academic use      |

#### Linear Programming Solvers

> #### Revisar [PuLP](https://github.com/coin-or/pulp)

| Library            | Languaje  | Price                      |
|--------------------|:---------:|----------------------------|
| CLP                | C++       | Open Source                |
| SimplexSolver      | Java      | Open Source                |

#### Local Search Solvers

> #### Nota de Javier Lafuente
> Para Local Search **Optaplanner**.

| Library            | Languaje  | Price                      |
|--------------------|:---------:|----------------------------|
| OptaPlanner        | Java      | Open Source                |
| Local Solver       | Binary    | Free with academic license |

#### SAT Solvers

| Library            | Languaje  | Price                      |
|--------------------|:---------:|----------------------------|
| cryptominisat      | C++       | Open Source                |
| Glucose            | C         | Open Source                |
| Lingeling          | C         | Open Source                |
| UBCSAT             | C         | Open Source                |
| MiniSat            | Binary    | Free                       |

#### Hybrid Solvers

| Library            | Languaje  | Price                      |
|--------------------|:---------:|----------------------------|
| SCIP               | Binary    | Free for academic use      |

https://kristerw.github.io/2022/11/01/verifying-optimizations/
