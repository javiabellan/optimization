from ortools.sat.python import cp_model

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count



# Minimal CP-SAT example.
# - Three variables, x, y, and z, each of which can take on the values: 0, 1, or 2.
# - One constraint: x ≠ y
def SimpleCPmodel(solution, limit_time=False):

    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    x = model.NewIntVar(0, 2, 'x')
    y = model.NewIntVar(0, 2, 'y')
    z = model.NewIntVar(0, 2, 'z')

    # Creates the constraints.
    model.Add(x != y)

    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()

    # Sets a time limit of 10 seconds.
    if limit_time:
        solver.parameters.max_time_in_seconds = 10.0

    if solution=="first":
        status = solver.Solve(model)
        if status == cp_model.OPTIMAL:
            print('x = %i' % solver.Value(x))
            print('y = %i' % solver.Value(y))
            print('z = %i' % solver.Value(z))

    if solution=="all":
        solution_printer = SolutionPrinter([x, y, z])
        status = solver.SearchForAllSolutions(model, solution_printer)

        print()
        print('Statistics')
        print('  - status          : %s'   % solver.StatusName(status))
        print('  - conflicts       : %i'   % solver.NumConflicts())
        print('  - branches        : %i'   % solver.NumBranches())
        print('  - wall time       : %f s' % solver.WallTime())
        print('  - solutions found : %i'   % solution_printer.solution_count())




SimpleCPmodel(solution="all")