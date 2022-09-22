from fractions import Fraction
import math
import numpy as np

def simulacion():
    x = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    h = [[((1/2**(1/2)), 0), ((1/2**(1/2)), 0)], [((1/2**(1/2)), 0), ((-1/2**(1/2)), 0)]]
    o = [(1, 0), (0, 0)]
    n = len(x[0]) * len(h[0])
    tensor_o = producto_Tensor(o, o, 1)
    m1 = producto_Tensor(x, h, 2)
    m2 = producto_Tensor(h, h, 2)
    matriz1 = hacermatriz(m1, n)
    matriz2 = hacermatriz(m2, n)
    gamma1 = matriz_Producto(matriz1, matriz2)
    gammafinal = matriz_sobre_Vector(gamma1, tensor_o)
    prettyprintingsVectores(gammafinal, 1)


def posibilidad_posicion(vector, posicion):
    posicion_vector = [[None, None]]
    posicion_vector[0][0] = vector[posicion][0]
    posicion_vector[0][1] = vector[posicion][1]
    posicion_vector = (posicion_vector[0][0]**2+posicion_vector[0][1]**2)
    v2 = list(vector)
    vector = matriz_Conjugada(vector, 2)
    norma = productoI_Interno(vector, v2)
    norma = (norma[0]+norma[1]) ** (1/2)
    probabilidad = posicion_vector/norma**2
    probabilidad = round(probabilidad, 6)
    return probabilidad


def amplitud_de_transicion(v1, v2):
    v1, v2 = v2, v1
    v11 = list(v1)
    v1 = matriz_Conjugada(v1, 2)
    norma = productoI_Interno(v1, v11)
    norma = (norma[0]+norma[1]) ** (1/2)
    v22 = list(v2)
    x = len(v22)
    v2 = matriz_Conjugada(v2, 2)
    norma2 = productoI_Interno(v2, v22)
    norma2 = (norma2[0]+norma2[1]) ** (1/2)
    v2 = hacervector(v2, x)
    v2 = matriz_Conjugada(v2, 2)
    v1 = matriz_Transpuesta(v1)
    producto = matriz_Producto(v1, v2)
    noma_Total = norma * norma2
    for i in range(len(producto[0][0])):
        for j in range(1):
            producto[0][0][i] = round(producto[0][0][i] / noma_Total, 2)
    return producto


def varianza(matriz, vector):
    x = matriz_Hermitiana(matriz, matriz)
    if x:
        print("Es hermitiana.")
    else:
        print("No es hermitiana.")


def mirar_hermitiana(matriz):
    x = matriz_Hermitiana(matriz, matriz)
    if x:
        return True
    else:
        return False


def valorEsperado(v, m):
    v2 = matriz_sobre_Vector(m, v)
    v2 = hacervector(v2, len(v))
    v2 = matriz_Conjugada(v2, 2)
    v2 = hacervector(v2, len(v))
    valor_esperado = producto_vetores(v2, v)
    return valor_esperado


def varianza(ket, matriz):
    valor_esperado = valorEsperado(ket, matriz)
    matrizUnitaria = hacer_unitaria(matriz, valor_esperado)
    resta = resta_matrices(matriz, matrizUnitaria)
    produto = matriz_Producto(resta, resta)
    produto1 = hacervector(matriz_sobre_Vector(produto, ket), len(ket))
    conjugada = hacervector(matriz_Conjugada(ket, 2), len(ket))
    varian = producto_vetores(conjugada, produto1)
    return(varian)


def valores_esperados(matriz, parametro):
    valor = []
    valores, vectores = np.linalg.eig(matriz)
    vecto = [[] for i in range(len(vectores))]
    for i in range(len(valores)):
        valor.append(round(valores[i], 1))
    for i in range(len(vectores)):
        for j in range(len(vectores)):
            vecto[i].append(vectores[i][j])
    if parametro == 1:
        return valor
    else:
        return vecto


def probabilidad(vector_estado1, vector_estado2, matriz, valor):
    if matriz == [[0, -1j], [1j, 0]]:
        vector1 = [[0, 1], [1, 0]]
        vector2 = [[0, -1], [1, 0]]
    else:
        vectores_propios = valores_esperados(matriz, 2)
        vector1 = [[0, 0] for i in range(len(vectores_propios[0]))]
        vector2 = [[0, 0] for i in range(len(vectores_propios[0]))]
        if vectores_propios[0][0] != complex:
            vector1[0][0] = vectores_propios[0][0]
        else:
            vector1[0][1] = vectores_propios[0][0]
        if vectores_propios[0][1] != complex:
            vector1[1][0] = vectores_propios[0][1]
        else:
            vector1[1][1] = vectores_propios[0][1]
        #2
        if vectores_propios[1][0] != complex:
            vector2[0][0] = vectores_propios[1][0]
        else:
            vector2[0][1] = vectores_propios[1][0]
        if vectores_propios[1][1] != complex:
            vector2[1][0] = vectores_propios[1][1]
        else:
            vector2[1][1] = vectores_propios[1][1]
    amplitud1 = amplitud_de_transicion(vector_estado1, vector1)
    amplitud2 = amplitud_de_transicion(vector_estado1, vector2)
    amplitud3 = amplitud_de_transicion(vector_estado2, vector1)
    amplitud4 = amplitud_de_transicion(vector_estado2, vector2)
    if valor == 1:
        return amplitud1
    elif valor == 2:
        return amplitud2
    elif valor == 3:
        return amplitud3
    elif valor == 4:
        return amplitud4


def comprobar_producto(m1, m2):
    m3 = m1
    m4 = m2
    bandera1 = matriz_Hermitiana(m1, m3)
    bandera2 = matriz_Hermitiana(m2, m4)
    if bandera1 and bandera2:
        producto = matriz_Producto(m1, m2)
        m5 = producto
        bandera3 = matriz_Hermitiana(producto, m5)
        if bandera3:
            return bandera3
        else:
            return bandera3
    else:
        return False


def probabilidad_3_clic(m, v):
    x = len(v)
    for i in range(3):
        vector = matriz_sobre_Vector(m, v)
        vector = hacervector(vector, x)
        v = vector
    probabilidad = round(v[2][0] ** 2 + v[2][1] ** 2, 4)
    return probabilidad