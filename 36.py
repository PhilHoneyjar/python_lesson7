def print_operation_table(operation, num_rows=7, num_columns=7):
    if operation(1, 1) == 2:
        print(1, end='\t')
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            if operation(1, 1) == 2:
                j -= 1
            print(operation(i, j), end='\t')
        print()


operation = lambda x, y: x * y
print_operation_table(operation)
