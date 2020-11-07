# Probelama de la mochila

## Descripción informal

Cada objeto tiene un peso (kg) y un valor ($). Objetivo meter el maximo valor en la mochila sin pasarnos del peso limite (por ejemplo 10kg).


## Descripción matematica

Input:
- Lista de pares [peso_i, valor_i] ara cada objeto
- Constante peso max mochila
Output:
- Lista binaria de "coge" o "no coje" para cada objeto 


### Soluciones Greedy 

- Solución 1: Ir meteiendo los objetos de menor a mayor peso
- Solución 2: Ir meteiendo los objetos de mayor a menor valor
- Solucion 3: Calcular valor/peso de cada objeto e ir metiendo de mayor a menor "valor/peso"

Estas soluciones no dan el optimo para el problema de la mochilas


## Soluciones [Dynamic Programming](https://es.wikipedia.org/wiki/Programaci%C3%B3n_din%C3%A1mica)

Tambien conocido como divide & conquer.

- Solución 1: Naive recurrente -> función recurrente (Se repiten calculos ya calculados) DA EL OPTIMO CREO
- Solución 2: Dynamic Programming (botton up) = tabla de resultados (memoización)
- Solucion 3: Dynamic Programming (top-down)  = función recurrente + tabla de resultados (memoización)

> #### Preguntas que hacerse:
> ¿Ocupa mucha memoria la tabla de resultados?



### Soluciones [Ramificación y poda](https://es.wikipedia.org/wiki/Ramificaci%C3%B3n_y_poda)

La ramificación y poda (branch and bound en ingles) consiste en no evaluar ramas del arbol que son innecesarias. Este criterio se hace con la Estimación optimista que nos da una idea de lo mejor que puede ofrecer esa rama.

- Para la poda debe estimar lo mejor que puede dar esa rama, si no es suficiente: podar.
  - Estimacion optimistia 1 = coger todo
  - Estimacion optimistia 2 (relaxation) = coger todlos que me caben y fraccionando (estimacion optimista un poco mas realista)

- Forma de recorrer la construccion del arbol:
  - Depht first
  - Best first
  - Least discrepancy

> #### Preguntas que hacerse:
> ¿Es rapida mi forma de calcular la estimación optimista? (Ya que la voy a calcuclar muchar veces)