from matplotlib import pyplot as plt
import libComplex as cpx
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

def click(matrix,vector,clicks):
    a = []
    for i in range (clicks):
        a = cpx.productMatrices(matrix, matrix)
    if clicks != 1:
        res = cpx.accionMatrizVectorComplex(a,vector)
    else:
        res = cpx.accionMatrizVectorComplex(matrix,vector)
    return res

