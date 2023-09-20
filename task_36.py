def print_operation_table(num_rows, num_columns):
    comp = lambda x,y: x*y
    return [print([print(comp(i,j), end=" ") for j in range(1, num_columns + 1)]) for i in range(1, num_rows + 1)]

n = 3
m = 6

print_operation_table(n, m)
