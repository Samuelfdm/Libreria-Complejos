def booleanMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[j][i]:
                matrix[j][i] = (1, 0)
            elif not matrix[j][i]:
                matrix[j][i] = (0, 0)
            else:
                matrix[j][i] = "not boolean"
    if "not boolean" in matrix:
        matrix = False
    else:
        matrix = matrix
    return matrix
