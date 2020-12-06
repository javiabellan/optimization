#
# BASED ON
# https://developers.google.com/optimization/scheduling/employee_scheduling
#
# This program tries to find an optimal assignment of 5 employees to shifts
# (3 shifts per day, for 7 days), subject to some constraints (see below).
# Each employee can request to be assigned to specific shifts.
# The optimal assignment maximizes the number of fulfilled shift requests.


import numpy as np
from ortools.sat.python import cp_model


################################################################## Data
n_empl   = 5
n_days   = 7
n_shifts = 3

shift_requests = np.array([
    # Monday    Tuesday    Wednesday  Thursday   Friday     Saturday   Sunday
    [[0, 0, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 1]], # Employee 1
    [[0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0], [0, 0, 0], [0, 0, 1]], # Employee 2
    [[0, 1, 0], [0, 1, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0]], # Employee 3
    [[0, 0, 1], [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], # Employee 4
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 0]]] # Employee 5
)

################################################################## Decission variables

# Creates the model.
model = cp_model.CpModel()

# shifts[e, d, s]: employee 'e' works shift 's' on day 'd'.
shifts = np.empty([n_empl, n_days, n_shifts], dtype=cp_model.IntVar)

for e in range(n_empl):
    for d in range(n_days):
        for s in range(n_shifts):
            shifts[e,d,s] = model.NewBoolVar('shift_%i%i%i' % (e, d, s))


 ################################################################## Constraints

# Each shift is assigned to one employee per day.
for d in range(n_days):
    for s in range(n_shifts):
        model.Add(sum(shifts[e, d, s] for e in range(n_empl)) == 1)

# Each employee works at most one shift per day.
for e in range(n_empl):
    for d in range(n_days):
        model.Add(sum(shifts[e, d, s] for s in range(n_shifts)) <= 1)

# Try to distribute the shifts evenly, so that each employee works
# min_shifts_per_employee shifts. If this is not possible, because the total
# number of shifts is not divisible by the number of employees, some employees will
# be assigned one more shift.
min_shifts_per_employee = (n_shifts * n_days) // n_empl
if n_shifts * n_days % n_empl == 0:
    max_shifts_per_employee = min_shifts_per_employee
else:
    max_shifts_per_employee = min_shifts_per_employee + 1
for e in range(n_empl):
    n_shifts_worked = 0
    for d in range(n_days):
        for s in range(n_shifts):
            n_shifts_worked += shifts[e, d, s]
    model.Add(min_shifts_per_employee <= n_shifts_worked)
    model.Add(n_shifts_worked <= max_shifts_per_employee)


################################################################## Objective

model.Maximize(sum(shift_requests[e,d,s] * shifts[e,d,s] for e in range(n_empl)
                                                         for d in range(n_days)
                                                         for s in range(n_shifts)))

################################################################## Solve

# Creates the solver and solve.
solver = cp_model.CpSolver()
solver.Solve(model)

for d in range(n_days):
    print('Day', d)
    for s in range(n_shifts):
        for e in range(n_empl):
            if solver.Value(shifts[e, d, s]) == 1:
                if shift_requests[e, d, s] == 1:
                    print('  Shift', s+1, '-> Employee', e+1, '(requested).')
                else:
                    print('  Shift', s+1, '-> Employee', e+1, '(not requested).')
    print()

# Statistics.
print()
print('Statistics')
print('  - Number of shift requests met = %i' % solver.ObjectiveValue(),
      '(out of', n_empl * min_shifts_per_employee, ')')
print('  - wall time       : %f s' % solver.WallTime())