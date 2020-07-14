def menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    print("Your choice: ", end='')
    return input()


def add_matrices():
    matrix1 = []
    matrix2 = []

    print("Enter size of first matrix: ", end='')
    rows1, columns1 = [int(x) for x in input("").split()]

    print("Enter first matrix:")
    for n in range(rows1):
        line = input().split()
        matrix1.append(line)

    print("Enter size of second matrix: ", end='')
    rows2, columns2 = [int(x) for x in input().split()]

    print("Enter second matrix:")
    for n in range(rows2):
        line = input().split()
        matrix2.append(line)

    matrix_sum = matrix1

    print("The result is:")
    if rows1 == rows2 and columns1 == columns2:
        for n in range(rows1):
            for m in range(columns1):
                matrix_sum[n][m] = float(matrix1[n][m]) + float(matrix2[n][m])
                matrix_sum[n][m] = str(matrix_sum[n][m])

        for line in matrix_sum:
            print(' '.join(line))
    else:
        print("The operation cannot be performed")


def multiply_constant():
    matrix = []

    print("Enter size of matrix: ", end='')
    rows1, columns1 = [int(x) for x in input().split()]

    print("Enter matrix:")
    for n in range(rows1):
        line = input().split()
        matrix.append(line)

    print("Enter constant: ", end='')
    constant = int(input())

    for n in range(rows1):
        for m in range(columns1):
            matrix[n][m] = str(int(matrix[n][m]) * constant)

    print("The result is:")
    for line in matrix:
        print(' '.join(line))


def multiply_matrix():
    matrix1 = []
    matrix2 = []

    print("Enter size of first matrix: ", end='')
    rows1, columns1 = [int(x) for x in input("").split()]

    print("Enter first matrix:")
    for n in range(rows1):
        line = input().split()
        matrix1.append(line)

    print("Enter size of second matrix: ", end='')
    rows2, columns2 = [int(x) for x in input().split()]

    print("Enter second matrix:")
    for n in range(rows2):
        line = input().split()
        matrix2.append(line)

    if columns1 == rows2:
        matrix_final = []
        line = []
        dot_product = 0

        for final_matrix_row in range(rows1):
            for final_matrix_column in range(columns2):
                for shared_element in range(columns1):
                    dot_product += float(matrix1[final_matrix_row][shared_element]) * float(matrix2[shared_element][final_matrix_column])
                line.append(str(dot_product))
                dot_product = 0
            matrix_final.append(line)
            line = []

        for line in matrix_final:
            print(' '.join(line))
    else:
        print("The operation cannot be performed")


def transpose_matrix_menu():
    transpose_menu = 0
    while transpose_menu < 1 or transpose_menu > 4:
        print()
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        print("Your choice: ", end='')
        transpose_menu = int(input())

    if transpose_menu == 1:
        transpose_matrix_main()
    elif transpose_menu == 2:
        transpose_matrix_side()
    elif transpose_menu == 3:
        transpose_matrix_vertical()
    else:
        transpose_matrix_horizontal()


def transpose_matrix_main():
    matrix = []

    print("Enter size of matrix: ", end='')
    rows, columns = [int(x) for x in input().split()]

    print("Enter matrix:")
    for n in range(rows):
        line = input().split()
        matrix.append(line)

    print("The result is:")
    for i in range(columns):
        line = []
        for j in range(rows):
            line.append(matrix[j][i])
        print(' '.join(line))


def transpose_matrix_side():
    matrix = []

    print("Enter size of matrix: ", end='')
    rows, columns = [int(x) for x in input().split()]

    print("Enter matrix:")
    for n in range(rows):
        line = input().split()
        matrix.append(line)

    print("The result is:")
    for i in range(columns):
        line = []
        for j in range(rows):
            line.append(str(matrix[rows - j - 1][columns - i - 1]))
        print(' '.join(line))


def transpose_matrix_vertical():
    matrix = []

    print("Enter size of matrix: ", end='')
    rows, columns = [int(x) for x in input().split()]

    print("Enter matrix:")
    for n in range(rows):
        line = input().split()
        matrix.append(line)

    print("The result is:")
    for i in range(rows):
        line = []
        for j in range(columns):
            line.append(matrix[i][columns - j - 1])
        print(' '.join(line))


def transpose_matrix_horizontal():
    matrix = []

    print("Enter size of matrix: ", end='')
    rows, columns = [int(x) for x in input().split()]

    print("Enter matrix:")
    for n in range(rows):
        line = input().split()
        matrix.append(line)

    print("The result is:")
    for i in range(rows):
        line = []
        for j in range(columns):
            line.append(matrix[rows - i - 1][j])
        print(' '.join(line))


def get_determinant():
    matrix = []
    print("Enter matrix size: ", end='')
    rows, columns = [int(x) for x in input().split()]

    print("Enter matrix:")
    for n in range(rows):
        line = input().split()
        matrix.append(line)

    print("The result is:")
    print(calculate_determinant(matrix))


def calculate_determinant(matrix):
    result = 0

    if len(matrix) == 1:
        result = matrix[0][0]

    if len(matrix) == 2:
        minor = float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])
        result = minor

    if len(matrix) > 2:
        for i in range(len(matrix)):
            result += float(matrix[0][i]) * ((-1) ** (1 + i + 1)) * calculate_determinant(reduce_matrix(matrix, 0, i))

    return result


def reduce_matrix(matrix, rows, columns):
    og_matrix = matrix
    new_matrix = []
    line = []

    for i in range(len(og_matrix)):
        line = []
        for j in range(len(og_matrix)):
            if j != columns and i != rows:
                line.append(og_matrix[i][j])
        if line:
            new_matrix.append(line)

    return new_matrix


def inverse_matrix():
    matrix = []
    adjoint_matrix = []
    inversed = matrix
    line = []
    determinent = 0
    cofactor = 0

    print("Enter matrix size: ", end='')
    rows, columns = [int(x) for x in input().split()]

    print("Enter matrix:")
    for n in range(rows):
        line = input().split()
        matrix.append(line)

    determinent = calculate_determinant(matrix)

    if determinent == 0:
        print("This matrix doesn't have an inverse.")
    else:
        for i in range(rows):
            line = []
            for j in range(columns):
                cofactor = ((-1) ** (i + j + 2)) * calculate_determinant(reduce_matrix(matrix, i, j))
                line.append(cofactor)
            adjoint_matrix.append(line)

        for i in range(rows):
            for j in range(columns):
                inversed[i][j] = adjoint_matrix[j][i]

        for i in range(rows):
            for j in range(columns):
                inversed[i][j] = str(1 / determinent * float(inversed[i][j]))

        for i in range(rows):
            for j in range(columns):
                inversed[i][j] = str(round(float(inversed[i][j]), 3))

        print("The result is:")
        for line in inversed:
            print(' '.join(line))


menu_option = menu()
while menu_option != '0':
    if menu_option == '1':
        add_matrices()
    elif menu_option == '2':
        multiply_constant()
    elif menu_option == '3':
        multiply_matrix()
    elif menu_option == '4':
        transpose_matrix_menu()
    elif menu_option == '5':
        get_determinant()
    elif menu_option == '6':
        inverse_matrix()

    print()
    menu_option = menu()
