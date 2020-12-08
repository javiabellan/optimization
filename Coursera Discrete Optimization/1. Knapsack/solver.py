"""
################################ INPUT FILE

============
n K
v_0 w_0
v_1 w_1
...
v_n-1 w_n-1
============

Where 
- n: the number of items.
- K: the capacity of the knapsack (the total weight available).
- v_0: Value of first item
- w_0: Weight of first item

Obejtive: Maximize the value


################################ OUTPUT FILE

============
obj opt
x_0 x_1 x_2 ... x_n-1
============

Where 
- obj: The total value achieved
- opt: Flag to indicate if the solution is optimal or not
- x_0 x_1 x_2 ... x_n-1: OneHot of selected items


################################ EXECUTION

python solver.py ./data/ks_4_0
"""




from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])


def read_file(input_data):

    lines      = input_data.split('\n')
    firstLine  = lines[0].split()
    item_count = int(firstLine[0])
    capacity   = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    return item_count, capacity, items



def solve_it(input_data):

    item_count, capacity, items = read_file(input_data)

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value  = 0
    weight = 0
    taken  = [0] * len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value  += item.value
            weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

