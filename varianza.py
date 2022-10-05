import libComplex as cpx
import math

def verifiMatrizCuadrada(m):
    if len(m) == len(m[0]):
        return True
    else:
        return False

def matrizUnitaria(longitud):
    matriz = [[(0, 0) for j in range(longitud)] for i in range(longitud)]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                matriz[i][j] = (1, 0)
    return matriz

def resta_matrices(m1, m2):
    matrizResta = [[(0, 0) for j in range(len(m1))] for i in range(len(m1[0]))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            matrizResta[i][j] = cpx.restaComplex(m1[i][j], m2[i][j])
    return matrizResta

def valorEsperado(observable, estado):
    verificar_hermitiana = cpx.hermitianaMatrizComplex(observable)
    verificar_cuadrada = verifiMatrizCuadrada(observable)
    if verificar_hermitiana and verificar_cuadrada:
        accion = cpx.accionMatrizVectorComplex(observable, estado)
        valor_esperado = cpx.innerProductVectorComplex(accion, estado)
        return valor_esperado

def varianza(observable, estado):
    valor_esperado = valorEsperado(observable, estado)
    print("VALOR ESPERADO", valor_esperado)
    long = len(observable)
    matriz_unitaria = matrizUnitaria(long)
    valor = cpx.escalarMatrizComplex(valor_esperado, matriz_unitaria)
    resta = resta_matrices(observable, valor)
    multi = cpx.productMatrices(resta, resta)
    varianza = valorEsperado(multi, estado)
    return varianza

#observable = [[(0, 0), (0, -1)], [(0, 1), (0, 0)]]

#estado = [(1/math.sqrt(2), 0), (0, 1/math.sqrt(2))]

observable = [[(3, 0), (1, 2)],
              [(1, -2), (-1, 0)]]

estado = [(math.sqrt(2)/2, 0), (-math.sqrt(2)/2, 0)]

print("VARIANZA", varianza(observable, estado))