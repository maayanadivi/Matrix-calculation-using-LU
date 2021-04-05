# Analysis HomeWork2 by:
# Maayan Nadivi - 208207068
# Alice Aidlin - 206448326


def getlen(matrix):  # A function that calculates the size of the matrix
    return len(matrix)


def minor(matrix, row, col):  # A function that calculates the minor returns the 2X2 matrix
    mat = matrix
    mat = mat[:row] + mat[row + 1:]
    for i in range(0, len(mat)):
        mat[i] = mat[i][:col] + mat[i][col + 1:]
    return mat


def det(matrix, len):  # A function that calculates the determinant of the matrix
    if len == 1:  # First option
        return matrix[0][0]
    if len == 2:  # second option
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]  # Calculation of minor
    sum = 0
    for i in range(0, len):
        m = minor(matrix, 0, i)  # send to minor func
        sum = sum + ((-1) ** i) * matrix[0][i] * det(m, len - 1)
    return sum  # return det


def is_regular(matrix):  # A function that checks whether the determinant of the matrix is equal to 0 or not
    if det(matrix, getlen(matrix)) == 0:
        return False  # The determinant is not equal to 0 Solve using a reversible matrix
    return True  # The determinant is equal to 0 Solved using a UL calculation


def matrix_multiply(A, B):  # A function that calculates the multiplication of 2 matrices and returns the new matrix
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        print('Number of A columns must equal number of B rows.')
    new_matrix = []
    while len(new_matrix) < rowsA:  # while len small the len rows
        new_matrix.append([])  # add place
        while len(new_matrix[-1]) < colsB:
            new_matrix[-1].append(0.0)  # add value
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]  # mul mat
            new_matrix[i][j] = total
    return new_matrix  # return the A*B=new matrix


def create_I(matrix):  # A function that creates and returns the unit matrix
    I = list(range(len(matrix)))  # make it list
    for i in range(len(I)):
        I[i] = list(range(len(I)))

    for i in range(len(I)):
        for j in range(len(I[i])):
            I[i][j] = 0.0  # put the zero

    for i in range(len(I)):
        I[i][i] = 1.0  # put the pivot
    return I  # unit matrix


def inverse(matrix):  # A function that creates and returns the inverse matrix to matrix A
    new_matrix = create_I(matrix)  # Creating the unit matrix
    count = 0
    check = False  # flag
    while count <= len(matrix) and check == False:
        if matrix[count][0] != 0:  # if the val in place not 0
            check = True  # flag
        count = count + 1  # ++
    if check == False:
        print("ERROR")
    else:
        temp = matrix[count - 1]
        matrix[count - 1] = matrix[0]  # put zero
        matrix[0] = temp
        temp = new_matrix[count - 1]
        new_matrix[count - 1] = new_matrix[0]
        new_matrix[0] = temp

        for x in range(len(matrix)):
            divider = matrix[x][x]# find the div val
            if divider==0:
                divider=1
            for i in range(len(matrix)):
                matrix[x][i] = matrix[x][i] / divider  # find the new index
                new_matrix[x][i] = new_matrix[x][i] / divider
            for row in range(len(matrix)):
                if row != x:
                    divider = matrix[row][x]
                    for i in range(len(matrix)):
                        matrix[row][i] = matrix[row][i] - divider * matrix[x][i]
                        new_matrix[row][i] = new_matrix[row][i] - divider * new_matrix[x][i]
    return new_matrix  # Return of the inverse matrix


def e_matrix(matrix, col):  # A function that receives a matrix and a number of columns and returns the appropriate
    # elementary matrix
    e = create_I(matrix)  # unit matrix
    pivot = matrix[col][col]  # pivot val
    for row in range(col + 1, len(matrix)):
        e[row][col] = (-1) * (matrix[row][col] / pivot)
    return e  # elementary matrix


def U(matrix):  # A function that accepts a matrix and returns the matrix U by calculations
    temp = matrix  # creat copy
    for col in range(len(matrix) - 1):
        u = matrix_multiply(e_matrix(temp, col), temp)  # send to mul func
        temp = u
    return u  # return U matrix


def L(matrix):  # A function that accepts a matrix and returns the matrix L by calculations
    temp = matrix
    l = create_I(matrix)  # unit matrix
    for col in range(len(matrix) - 1):
        elementary = e_matrix(temp, col)  # send to func to creat elementary matrix
        m = inverse(elementary)  # create inverse elementary matrix
        for row in range(col + 1, len(matrix)):
            l[row][col] = m[row][col]
        elementary = matrix_multiply(e_matrix(temp, col), temp)  # make elementary matrix and then mul with other matrix
        temp = elementary
    return l


def LU(matrix):  # A function that receives a matrix and returns the product between U and L.
    return matrix_multiply(L(matrix), U(matrix))  # send to mul func


def main():

    A = [[1, -1, -2, 3], [2, -3, -5, 6], [-1, 3, 5, 6], [1, -1, 5, 9]]
    b = [[13], [19], [78], [96]]

    if is_regular(A):
        x = matrix_multiply(inverse(A), b)
        print(x)
    else:
        y = matrix_multiply(inverse(L(A)), b)
        x = matrix_multiply(inverse(U(A)), y)
        print(x)

main()

