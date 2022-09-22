from matplotlib import pyplot as plt
import libComplex as cpx

# PARA DETERMINAR LA MATRIZ BOOLEANA
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

# PARA DETERMINAR LOS CLICKS:
def click(matrix, vector, clicks):
    a = []
    for i in range(clicks):
        a = cpx.productMatrices(matrix, matrix)
    if clicks != 1:
        res = cpx.accionMatrizVectorComplex(a, vector)
    else:
        res = cpx.accionMatrizVectorComplex(matrix, vector)
    return res

# EJERCICIO DE PROGRAMACION 3.1.1:
def canicasConMatrizBooleana(matrix, vector, clicks):
    m = booleanMatrix(matrix)
    if not m:
        ans = "La matriz no cumple con los requerimientos"
    else:
        ans = click(m, vector, clicks)
    return ans

# EJERCICIO DE PROGRAMACIÓN 3.2.1:
def canicasConFracciones(matrix, vector, clicks):
    return click(matrix, vector, clicks)

# EJERCICIO DE PROGRAMACIÓN 3.2.2:
def multiplesRendijasClasicoProbabilistico(rendijas, blancos, clicks):
    tama = rendijas + (blancos * rendijas)
    matrix = [[(0, 0) for i in range(tama)] for j in range(tama)]
    for i in range(1, rendijas + 1):
        matrix[i][0] = (1/rendijas, 0)
    x = rendijas + 1
    for j in range(1, int(rendijas + 1)):
        matrix[x][j] = (1/blancos, 0)
        matrix[x+1][j] = (1/blancos, 0)
        matrix[x+2][j] = (1/blancos, 0)
        x += 2
    for k in range(rendijas+1, tama):
        matrix[k][k] = (1, 0)
    vector = [(0, 0) for i in range(tama)]
    vector[0] = (1, 0)
    return matrix, click(matrix, vector, clicks)

# EJERCICIO DE PROGRAMACIÓN 3.3.2:
def multiplesRendijasCuantico(rendijas, blancos, clicks):
    tama = rendijas + (blancos * rendijas)
    matrix = [[(0, 0) for i in range(tama)] for j in range(tama)]
    for i in range(1, rendijas+1):
        matrix[i][0] = (1/2**(1/2), 0)
    x = rendijas + 1
    for j in range(1, rendijas+1):
        matrix[x][j] = (-1 / (6 ** 0.5), 1 / (6 ** 0.5))
        matrix[x + 1][j] = (-1 / (6 ** 0.5), -1 / (6 ** 0.5))
        matrix[x + 2][j] = (1 / (6 ** 0.5), -1 / (6 ** 0.5))
        x += 2
    for k in range(rendijas+1, tama):
        matrix[k][k] = (1, 0)
    vector = [(0, 0) for i in range(tama)]
    vector[0] = (1, 0)
    return matrix, click(matrix, vector, clicks)

# DIAGRAMAS
def diagramaProbabilistico(vector):
    prob = [i for i in range(len(vector))]
    plt.bar(prob, vector, color="#FF0080")
    plt.show()

def diagramaCuantico(v):
    vector = [(cpx.moduloComplex(v[i]))**2 for i in range(len(v))]
    prob = [i for i in range(len(vector))]
    plt.bar(prob, vector, color="#FF0080")
    plt.show()