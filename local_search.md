# Local Search

> - Intuition based, most significant coding
> - Writing efficient code really helps
> - Lost of staring at the terminal

**Siempre tiene una solución en la mano.** 

```python
def LocalSearch():
    current_solution = generate_initial_solution()
    best_solution    = current_solution
    for k in range(max_trials):
        current_solution = select_one_from_legal_neighbohood_moves()
        if satisfies(current_solution) and obj_fn(current_solution) < obj_fn(best_solution):
            best_solution = current_solution
    return best_solution
```

### Choosing a move of your neigbohood of moves:

- Type of moves
  - Move a value (N Queens: move a queen)
  - Swap 2 values
- Strategy of moves
  - Min/Max Conflict: (O(n^2) in N Queens)
    1. select the variable with the most violations
    2. asign it the value with the fewest resulting violations
  - Min-conflict (O(n) in N Queens)
    1. randomly select a variable with some violations
    2. asign it the value with the fewest resulting violations


You are still minimizing an objective function:
- Feasibility problems: Minimizing violatons
- Optimization prblems: Objective function


### Heuristic vs Metaheuristic

- Heuristics: search towards local minima. **Tells you how to choose the next neighbour**.
- Metaheuristics: search towards global minima. Tyically includes some memory or learning.
  - Muchas soluciones:
    - Iterated Local Search
    - Genetic algorithm
  - Una única solución y hacer pequeñas soluciones en esa solución.
    - Simulated Annealing
    - Tabu Search


### Simulated Annealing
- Mostly random choices (random walk) at the begining (high temerature)
- Mostly deterterminisctic greedy search at the end (low temperature) (because local minima is probably the global minima)

> Property:
> If you give it enouh time and your neigborhood is connected you are guaranteed to converge to a global optimum.

### Tabu Search
All the past solution are TABU and you can't visit them again. This helps to scape local minima and serch for the global minima.

The list of visted solutions (nodes) (TABU list) can be really big. So improvements are:
- Keep only the last solutions in the TABU list
- Increase or decrease the size of the list dynamically
  - Decrease when the selected node degrades the objective
  - Increase when the selected node improves the objective
- Keep an abstraction of the nodes.

  
### Local Search Solvers

> #### Nota de Javier Lafuente
> Para Local Search **Optaplanner**.

| Library            | Languaje  | Price                      |
|--------------------|:---------:|----------------------------|
| OptaPlanner        | Java      | Open Source                |
| Local Solver       | Binary    | Free with academic license |
