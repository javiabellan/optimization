import sys
from ortools.sat.python import cp_model


def main(board_size):

	model = cp_model.CpModel()

	########################### Decission variables
		
	# One queen per column (the value is the row).
	queens = [model.NewIntVar(0, board_size-1, 'x%i'%i)                for i in range(board_size)]
	
	# Aux variables for diagonals
	diag1  = [model.NewIntVar(0, 2*board_size, 'diag1_%i' % i)         for i in range(board_size)]
	diag2  = [model.NewIntVar(-board_size, board_size, 'diag2_%i' % i) for i in range(board_size)]
	

	########################### Constraints
	
	# All queens are in different rows.
	model.AddAllDifferent(queens)

	# Two queens can not be on the same diagonal.
	for i in range(board_size):
		model.Add(diag1[i] == queens[i] + i) # Create variable array for queens(i) + i.
		model.Add(diag2[i] == queens[i] - i) # Create variable array for queens(i) - i.
	model.AddAllDifferent(diag1)
	model.AddAllDifferent(diag2)

	########################### Solve model

	solver = cp_model.CpSolver()
	#solution_printer = SolutionPrinter(queens)
	solution_printer = DiagramPrinter(queens)
	status = solver.SearchForAllSolutions(model, solution_printer)
	print()
	print('Solutions found : %i' % solution_printer.SolutionCount())



class SolutionPrinter(cp_model.CpSolverSolutionCallback):
	"""Print intermediate solutions."""

	def __init__(self, variables):
		cp_model.CpSolverSolutionCallback.__init__(self)
		self.__variables = variables
		self.__solution_count = 0

	def OnSolutionCallback(self):
		self.__solution_count += 1
		for v in self.__variables:
			print('%s = %i' % (v, self.Value(v)), end = ' ')
		print()

	def SolutionCount(self):
		return self.__solution_count


class DiagramPrinter(cp_model.CpSolverSolutionCallback):
	
	def __init__(self, variables):
		cp_model.CpSolverSolutionCallback.__init__(self)
		self.__variables = variables
		self.__solution_count = 0

	def OnSolutionCallback(self):
		self.__solution_count += 1

		for v in self.__variables:
			queen_col = int(self.Value(v))
			board_size = len(self.__variables)
			# Print row with queen.
			for j in range(board_size):
				
				# There is a queen in column j, row i.
				if j==queen_col: print("Q", end=" ")
				else:            print("_", end=" ")
			print()
		print()

	def SolutionCount(self):
		return self.__solution_count


if __name__ == '__main__':
	
	board_size = 8 # By default, solve the 8x8 problem.
	if len(sys.argv) > 1:
		board_size = int(sys.argv[1]) # pass as argument
	main(board_size)