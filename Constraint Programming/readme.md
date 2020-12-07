
# Constraint Programming (CP)
> - Discrete math
> - Like solving puzzles
> - Lots of logic


> ### REMEMBER: The more constraints you add to your model, the faster the computation will be.

Modela tu problema lo mejor posible (contraints) para que el solver lo resuleva

CP is branch and pruning: (visualizeing that is important)

Pruning: Reduce the search sapce as much as possible.

### 1. Decission Variables

Each decission variables have a **domain** (possible options).

### 2. Constraints

- **Global Constraints**: Gobal constraints make it possible to detect infeasibilities earlier.
  - **AllDifferent**(array_of_decision_variables): Indicates that all items of the list must be different.
- **Symmetry-breaking Constraints**: Eliminate symmetries and reduce the search space size.
  - Example: Days to record a scene in a movie
- **Reduntant constraints**:
- **Subrogate constraint**: Combine constraints to prune more. Because in the worst case I will prune the same as if I don't add it.
- **Dual modeling**: Se pueden poner dos modelos a la vez (las constraints de cada modelo) y unirlas por una conrtaint nueva. Ejemplo el problema de las 8 reinas
  - El modelo A resulve el problema mediante las filas
  - El modelo B resulve el problema mediante las columnas
  - Añadir la contraint dual de que si una reina aparece en una fila marcar tambien la columna (y viceversa).


### 3. Searching engine

Searching appreaches:
- variable/value labeling
  - Variable ordering: Choose the most constraint variable
- value/variable labeling
- domain splitting
- focusing on the objective
- symmetry breaking during search
- randomization and restarts


> - First Fail principle:
>   - Choose the variable with the smallest domain
>   - choose the most constraint variable

Propagation engine

```python
for c in contraints:
    if c_is_feasible:
        # apply the prunning associated with c
    else:
        return failure
return success
```