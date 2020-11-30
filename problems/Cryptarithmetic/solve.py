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


def Solve():

    # Constraint programming engine
    model = cp_model.CpModel()

    base = 10

    s = model.NewIntVar(1, base - 1, 'S')
    e = model.NewIntVar(0, base - 1, 'E')
    n = model.NewIntVar(0, base - 1, 'N')
    d = model.NewIntVar(0, base - 1, 'D')
    m = model.NewIntVar(1, base - 1, 'M')
    o = model.NewIntVar(0, base - 1, 'O')
    r = model.NewIntVar(0, base - 1, 'R')
    y = model.NewIntVar(0, base - 1, 'Y')

    # We need to group variables in a list to use the constraint AllDifferent.
    letters = [s, e, n, d, m, o, r, y]

    # Verify that we have enough digits.
    assert base >= len(letters)

    # Define constraints.
    model.AddAllDifferent(letters)

    # SEND + MORE = MONEY
    model.Add(              s*base*base*base + e*base*base + n*base + d +
                            m*base*base*base + o*base*base + r*base + e ==
    m*base*base*base*base + o*base*base*base + n*base*base + e*base + y)

    ### Solve model.
    solver = cp_model.CpSolver()
    solution_printer = SolutionPrinter(letters)
    status = solver.SearchForAllSolutions(model, solution_printer)

    print()
    print('Statistics')
    print('  - status          : %s' % solver.StatusName(status))
    print('  - conflicts       : %i' % solver.NumConflicts())
    print('  - branches        : %i' % solver.NumBranches())
    print('  - wall time       : %f s' % solver.WallTime())
    print('  - solutions found : %i' % solution_printer.solution_count())


if __name__ == '__main__':
    Solve()