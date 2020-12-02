




# Maximize 2x + 2y + 3z
# subject to the following constraints:
#
#   x + 7/2 y + 3/2 z ≤ 25
# 3 x -   5 y +   7 z ≤ 45
# 5 x +   2 y -   6 z ≤ 37
#
# x, y, z ≥ 0
# x, y, z integers




from ortools.sat.python import cp_model


def main():
	model = cp_model.CpModel()
	
	upper_bound = 50
	x = model.NewIntVar(0, upper_bound, 'x')
	y = model.NewIntVar(0, upper_bound, 'y')
	z = model.NewIntVar(0, upper_bound, 'z')

	model.Add(2*x + 7*y + 3*z <= 50)
	model.Add(3*x - 5*y + 7*z <= 45)
	model.Add(5*x + 2*y - 6*z <= 37)

	model.Maximize(2*x + 2*y + 3*z)

	solver = cp_model.CpSolver()
	status = solver.Solve(model)

	if status == cp_model.OPTIMAL:
		print('Maximum of objective function: %i' % solver.ObjectiveValue())
		print()
		print('x value: ', solver.Value(x))
		print('y value: ', solver.Value(y))
		print('z value: ', solver.Value(z))


if __name__ == '__main__':
	main()
