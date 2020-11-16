import numpy as np

grid = [
	[5,0,0,0,8,0,0,4,9],
	[0,0,0,5,0,0,0,3,0],
	[0,6,7,3,0,0,0,0,1],
	[1,5,0,0,0,0,0,0,0],
	[0,0,0,2,0,8,0,0,0],
	[0,0,0,0,0,0,0,1,8],
	[7,0,0,0,0,4,1,5,0],
	[0,3,0,0,0,2,0,0,0],
	[4,9,0,0,5,0,0,0,3]]


def possible (r,c,n): # row, col, num
	global grid

	# CHECK ROW
	for i in range (0,9):
		if grid[r][i] == n:
			return False

	# CHECK COLUMN
	for i in range(0,9):
		if grid[i][c] == n:
			return False

	# CHECK BLOCK
	block_r = (r//3)*3
	block_c = (c//3)*3
	for i in range(0,3):
		for j in range(0,3):
			if grid[block_r+i][block_c+j] == n:
				return False

	return True


##################### SOLUCION CON BACKTRACKING (Brute-force search)

# Backtracking is a depth-first search (in contrast to a breadth-first search),
# because it will completely explore one branch to a possible solution before
# moving to another branch. Although it has been established that approximately
# 5.96 x 1126 final grids exist, a brute force algorithm can be a practical method
# to solve Sudoku puzzles.

def solve():
	global grid
	for r in range(9):
		for c in range(9):
			if grid[r][c] == 0:
				for n in range(1,10): # probar del 1 al 9
					if possible(r,c,n):
						grid[r][c] = n # Hacer suposicion
						solve() # Resolver con la suposicion
						grid[r][c] = 0 # Desacer suposicion
				return # si no puedo poner, es que lo hice mal -> Volver 
	print(np.matrix(grid)) # Si completo los fors -> solucion correcta
	input("More?")

solve()
