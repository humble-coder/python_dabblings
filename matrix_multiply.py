def square_matrix_multiply(A, B):
    n = len(A)
    result = []
    for i in range(0, n):
        new_row = []
        for j in range(0, n):
            current_sum = 0
            for k in range(0, n):
                current_sum += A[i][k]*B[k][j]
            new_row.append(current_sum)
        result.append(new_row)
    return result

##def recursive_matrix_multiply(A, B):
##    n = len(A)
##    c = []
##    for i in range(0, n):
##        row = [0]*n
##        c.append(row)
##    if n == 1:
##        c[0][0] = A[0][0] * B[0][0]
##    else:
##        print("recursion!")
##        c[0][0] = matrix_addition(recursive_matrix_multiply([A[0][0]], [B[0][0]]), recursive_matrix_multiply([A[0][1]], [B[1][0]]))
##        c[0][1] = matrix_addition(recursive_matrix_multiply([A[0][0]], [B[0][1]]), recursive_matrix_multiply([A[0][1]], [B[1][1]]))
##        c[0][1] = matrix_addition(recursive_matrix_multiply([A[1][0]], [B[0][0]]), recursive_matrix_multiply([A[1][1]], [B[1][0]]))
##        c[1][1] = matrix_addition(recursive_matrix_multiply([A[1][0]], [B[0][1]]), recursive_matrix_multiply([A[1][1]], [B[1][1]]))
##    return c
##
##def matrix_addition(A, B):
##    result = A
##    if len(A) == 1:
##        result[0][0] = A[0][0] + B[0][0]
##    else:
##        for i in range(0, len(A)):
##            for j in range(0, len(A)):
##                result[i][j] = A[i][j] + B[i][j]
##    return result
