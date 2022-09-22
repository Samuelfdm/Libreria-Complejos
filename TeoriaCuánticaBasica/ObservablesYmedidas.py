from fractions import Fraction
import math
import numpy as np
import libComplex as cpx

def hacermatriz(m1,n):
    matriz = [[[0,0] for j in range(n)] for i in range(n)]
    cont = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            for m in range(len(matriz)):
                matriz[j][m][0] = m1[cont][0]
                matriz[j][m][1] = m1[cont][1]
                cont += 1
        break
    cont = 0
    return(matriz)

def hacervector(v1,x):
    cont = 0
    vector = [[0,0] for i in range(x)]
    for i in range(len(vector)):
        if cont <= 2:
            cont += 1
            for j in range(len(vector)):
                if cont <= 2:
                    vector[j][i] = v1[j][0][i]
    return vector


def hacer_unitaria(m,valor):
    unitaria = [[[0,0] for j in range(len(m))]for i in range(len(m[0]))]
    for i in range(len(unitaria)):
        for j in range(len(unitaria[0])):
            if i == j:
                unitaria[i][i][0] = valor
    return(unitaria)

def normalizarVector(v):
    norma = cpx.normaVectorComplex(v)
    return cpx.escalarVectorComplex((1/norma, 0), v)


def probabilidad_pos(vector, pos):
    #vector = normalizarVector(vector)
    pos_new = (cpx.moduloComplex(vector[pos]))**2
    #print("Como el vector ya esta normalizado, pos_new ya es en si la probabilidad", pos_new)
    v_new = cpx.normaVectorComplex(vector)
    #print("norma",v_new)
    probabilidad = pos_new/(v_new**2)
    return probabilidad

def amplitud_de_transicion(v1, v2):
    v1 = normalizarVector(v1)
    v2 = normalizarVector(v2)
    product = cpx.innerProductVectorComplex(v2, v1)
    return product


def varianza(matriz, vector):
    x = cpx.hermitianaMatrizComplex(matriz)
    if x:
        print("Es hermitiana.")
    else:
        print("No es hermitiana.")


def mirar_hermitiana(matriz):
    x = matriz_Hermitiana(matriz)
    if x:
        return True
    else:
        return False

def producto_vectores(v1,v2):
    valor_esperado = 0
    for i in range(len(v1)):
        for j in range(len(v2[0])):
            x = cpx.productComplex(v2[j], v1[j])
            valor_esperado = valor_esperado + round(x[0]+ x[1], 1)
        break
    return valor_esperado

def valorEsperado(v, m):
    v2 = cpx.accionMatrizVectorComplex(m, v)
    v2 = cpx.conjugadaVectorComplex(v2)
    valor_esperado = producto_vectores(v2, v)
    return valor_esperado

def resta_matrices(m1,m2):
    matrizResta = [[[0,0] for j in range(len(m1))] for i in range(len(m1[0]))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            matrizResta[i][j][0] = m1[i][j][0] - m2[i][j][0]
            matrizResta[i][j][1] = m1[i][j][1] - m2[i][j][1]
    return matrizResta

def varianza(ket, matriz):
    valor_esperado = valorEsperado(ket, matriz)
    matrizUnitaria = hacer_unitaria(matriz, valor_esperado)
    resta = resta_matrices(matriz, matrizUnitaria)
    produto = cpx.productMatrices(resta, resta)
    produto1 = hacervector(cpx.accionMatrizVectorComplex(produto, ket), len(ket))
    conjugada = hacervector(cpx.conjugadaMatrizComplex(ket), len(ket))
    varian = producto_vectores(conjugada, produto1)
    return varian


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
    bandera1 = cpx.hermitianaMatrizComplex(m1, m3)
    bandera2 = cpx.hermitianaMatrizComplex(m2, m4)
    if bandera1 and bandera2:
        producto = cpx.productMatrices(m1, m2)
        bandera3 = cpx.hermitianaMatrizComplex(producto)
        if bandera3:
            return bandera3
        else:
            return bandera3
    else:
        return False


def probabilidad_3_clic(m, v):
    x = len(v)
    for i in range(3):
        vector = cpx.accionMatrizVectorComplex(m, v)
        vector = hacervector(vector, x)
        v = vector
    probabilidad = round(v[2][0] ** 2 + v[2][1] ** 2, 4)
    return probabilidad

def simulacion():
    x = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    h = [[((1/2**(1/2)), 0), ((1/2**(1/2)), 0)], [((1/2**(1/2)), 0), ((-1/2**(1/2)), 0)]]
    o = [(1, 0), (0, 0)]
    n = len(x[0]) * len(h[0])
    tensor_o = cpx.productTensorVectorComplex(o, o)
    m1 = cpx.productTensorMatrizComplex(x, h)
    m2 = cpx.productTensorMatrizComplex(h, h)
    matriz1 = hacermatriz(m1, n)
    matriz2 = hacermatriz(m2, n)
    gamma1 = cpx.productMatrices(matriz1, matriz2)
    gammafinal = cpx.accionMatrizVectorComplex(gamma1, tensor_o)
    return gammafinal