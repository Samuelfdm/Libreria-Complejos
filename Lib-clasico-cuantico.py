from matplotlib import pyplot as plt
import Lib-complex as cpx
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
        a = cM.productMatrix(matrix, matrix)
    if clicks != 1:
        res = cM.accionMatrixVector(a,vector)
    else:
        res = cM.accionMatrixVector(matrix,vector)
    return res