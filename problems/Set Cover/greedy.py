from collections import namedtuple
import sys


Set = namedtuple("Set", ['index', 'cost', 'items'])


def read_file(file_path):

    # Read file
    input_data_file = open(file_path, 'r')
    input_data = ''.join(input_data_file.readlines())
    input_data_file.close()

    # parse the input
    lines = input_data.split('\n')

    parts = lines[0].split()
    n_items = int(parts[0])
    n_sets  = int(parts[1])
    
    sets = []
    for i in range(1, n_sets+1):
        parts = lines[i].split()
        sets.append(Set(i-1, float(parts[0]), set(map(int, parts[1:])) ))

    return n_items, n_sets, sets


# 1) SORT (ASCENDING) SETS BY THE COST
# 2) SELECT SETS IN ORDER UNTIL ALL ITEMS ARE COVERED
#
# Notese para esta solucion que los datos (los sets)
# por defecto ya estan ordenanos de menor a mayor coste.
def greedy1(n_items, n_sets, sets):

    solution = [0]*n_sets
    covered = set()
    
    sorted_sets = sorted(sets, key=lambda s: s.cost)
    for s in sorted_sets:
        solution[s.index] = 1
        covered |= s.items # Union of sets
        if len(covered) >= n_items:
            break

    return solution


# 1) SORT (ASCENDING) SETS BY THE (COST/N_ITEMS_OF_SET) RATIO
# 2) SELECT SETS IN ORDER UNTIL ALL ITEMS ARE COVERED
def greedy2(n_items, n_sets, sets):

    solution = [0]*n_sets
    covered = set()
    
    sorted_sets = sorted(sets, key=lambda s: s.cost/len(s.items) if len(s.items) > 0 else s.cost)
    for s in sorted_sets:
        solution[s.index] = 1
        covered |= s.items # Union of sets
        if len(covered) >= n_items:
            break

    return solution

# 1) SORT (ASCENDING) SETS BY THE (COST/N_ITEMS_OF_SET_NOT_COVERED_YET) RATIO
# 2) SELECT SETS IN ORDER UNTIL ALL ITEMS ARE COVERED
def greedy3(n_items, n_sets, sets):

    solution = [0]*n_sets
    covered = set()
    
    while len(covered) < n_items:
        sorted_sets = sorted(sets, key=lambda s: s.cost/len(s.items-covered) if len(s.items-covered) > 0 else 9999999999)
        #print([s.cost/len(s.items-covered) if len(s.items-covered) > 0 else 9999999999 for s in sets])
        for s in sorted_sets:
            if solution[s.index] < 1:
                #print("Cojo el", s.index)
                solution[s.index] = 1
                covered |= set(s.items)
                break;

    return solution

# THIS IS THE SAME AS GREEDY 3
# 1) SORT (ASCENDING) SETS BY THE (- N_ITEMS_OF_SET_NOT_COVERED_YET/COST) RATIO
# 2) SELECT SETS IN ORDER UNTIL ALL ITEMS ARE COVERED
def greedy4(n_items, n_sets, sets):

    solution = [0]*n_sets
    covered = set()
    
    while len(covered) < n_items:
        sorted_sets = sorted(sets, key=lambda s: -len(s.items-covered)/s.cost if len(s.items-covered) > 0 else s.cost)
        #print([-s.cost*len(s.items-covered) if len(s.items-covered) > 0 else s.cost for s in sets])
        for s in sorted_sets:
            if solution[s.index] < 1:
                #print("Cojo el", s.index)
                solution[s.index] = 1
                covered |= set(s.items)
                break;

    return solution


def print_solution(solution, print_only_the_cost=False):

    # calculate the cost
    obj = sum([s.cost*solution[s.index] for s in sets])
    print("COST:", str(obj))

    if(not print_only_the_cost):
        print(' '.join(map(str, solution)))



if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1].strip()
        print('Solving:', file_path)

        n_items, n_sets, sets = read_file(file_path) # 1. Read file & parse data

        print("\nLEGEND:")
        print("|  GREEDY 1:")
        print("|    1) SORT (ASCENDING) THE SETS BY THE COST")
        print("|    2) SELECT SETS IN ORDER UNTIL ALL ITEMS ARE COVERED")
        print("|  GREEDY 2:")
        print("|    1) SORT (ASCENDING) THE SETS BY THE (COST/N_ITEMS_OF_SET) RATIO")
        print("|    2) SELECT SETS IN ORDER UNTIL ALL ITEMS ARE COVERED")
        print("|  GREEDY 3:")
        print("|    1) SORT (ASCENDING) THE SETS BY THE (COST/N_ITEMS_OF_SET_NOT_COVERED_YET) RATIO")
        print("|    2) SELECT SETS IN ORDER UNTIL ALL ITEMS ARE COVERED")
        print("|  GREEDY 4:")
        print("|    REFORMULATION OF GREEDY 3")

        print("\n======================= GREEDY 1")
        solution = greedy1(n_items, n_sets, sets)    # 2. greedy solution
        print_solution(solution)                     # 3. Print solution & cost

        print("\n======================= GREEDY 2")
        solution = greedy2(n_items, n_sets, sets)    # 2. greedy solution
        print_solution(solution)                     # 3. Print solution & cost

        print("\n======================= GREEDY 3")
        solution = greedy3(n_items, n_sets, sets)    # 2. greedy solution
        print_solution(solution)                     # 3. Print solution & cost

        print("\n======================= GREEDY 4")
        solution = greedy4(n_items, n_sets, sets)    # 2. greedy solution
        print_solution(solution)                     # 3. Print solution & cost
        
    else:
        print('This program requires an input file. Please select one from the data directory. ( i.e. python greedy.py ./data/sc_157_0 )')

# python greedy.py ./data/sc_157_0