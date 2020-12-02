#
# Codigo sacado de Coursera -> Discrete optimization -> Week 3 -> CP 10
#
# https://www.coursera.org/learn/discrete-optimization/lecture/3xnnT/cp-10-value-variable-labeling-domain-splitting-symmetry-breaking-in-search
#



#################################### Data

sides  = [50,42,37,35,33,29,27,25,24,19,18,17,16,15,11,9,8,7,6,4,2]
s      = 122 # Side of bigger square
side   = [range(s)]
Square = [range(21)]



#################################### Decision variables 

# Coordenadas x,y de cada cuadrado (la esquina abajo-izquierda por ejemplo)
var{int} x[Square] in Side; # Empty array
var{int} y[Square] in Side; # Empty array



#################################### Constraints

# Constraint de cada cuadrado debe estar dentro del cuadrado grande

forall(i in Square) {
  x[i] <= s-side[i]+1;
  y[i] <= s-side[i]+1;
}

# Constraint de non-overlapping (los cuadrados no se pueden superponer)

forall(i in Square,j in Square: i<j)
  x[i]+side[i]<= x[j] || x[j]+side[j]<=x[i] || y[i]+side[i]<=y[j] || y[j]+side[j]<=y[i];


# Redundant constaint de que para una hipotetica linea vertical que cruza el side total debe ser igual a la suma de de los cuadrados que la linea cruce.

for p in range(s):
{
  sum(i in Square) side[i]*((x[i]<=p) && (x[i]>=p-side[i]+1)) = s;
  sum(i in Square) side[i]*((y[i]<=p) && (y[i]>=p-side[i]+1)) = s;
} 


