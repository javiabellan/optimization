
from ortools.sat.python import cp_model


def solve_sudoku():
    """Solves the sudoku problem with the CP-SAT solver."""
    # Create the model.
    model = cp_model.CpModel()

    block_size = 3
    line_size  = block_size**2     # 9
    line  = list(range(line_size)) # [0..8]
    block = list(range(block_size)) # [0..2]

    initial_grid = [
        [0, 6, 0, 0, 5, 0, 0, 2, 0],
        [0, 0, 0, 3, 0, 0, 0, 9, 0],
        [7, 0, 0, 6, 0, 0, 0, 1, 0],
        [0, 0, 6, 0, 3, 0, 4, 0, 0],
        [0, 0, 4, 0, 7, 0, 1, 0, 0],
        [0, 0, 5, 0, 9, 0, 8, 0, 0],
        [0, 4, 0, 0, 0, 1, 0, 0, 6],
        [0, 3, 0, 0, 0, 8, 0, 0, 0],
        [0, 2, 0, 0, 4, 0, 0, 5, 0]]


    ######################################## Decission Variables

    grid = {}
    for i in line:
        for j in line:
            grid[(i, j)] = model.NewIntVar(1, line_size, 'grid %i %i' % (i, j))

    ######################################## Constraints

    # AllDifferent on rows.
    for i in line:
        model.AddAllDifferent([grid[(i, j)] for j in line])

    # AllDifferent on columns.
    for j in line:
        model.AddAllDifferent([grid[(i, j)] for i in line])

    # AllDifferent on blocks.
    for i in block:
        for j in block:
            one_block = []
            for di in block:
                for dj in block:
                    one_block.append(grid[(i * block_size + di,
                                          j * block_size + dj)])

            model.AddAllDifferent(one_block)

    # Initial values.
    for i in line:
        for j in line:
            if initial_grid[i][j]:
                model.Add(grid[(i, j)] == initial_grid[i][j])

    ######################################## Solve.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL:
        for i in line:
            output = ''
            for j in line:
                output += str(int(solver.Value(grid[(i, j)]))) + ' '
                if j == 2 or j == 5:
                    output += '| '
            print(output)
            if i == 2 or i == 5:
                print('------|-------|-------')

    print('\nAdvanced usage:')
    print(solver.ResponseStats())


solve_sudoku()