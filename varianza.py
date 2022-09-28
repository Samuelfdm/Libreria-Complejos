import libComplex as cpx
import math

def verifiMatrizCuadrada(m):
    if len(m) == len(m[0]):
        return True
    else:
        return False

def valorEsperado(observable, estado):
    verificar_hermitiana = cpx.hermitianaMatrizComplex(observable)
    verificar_cuadrada = verifiMatrizCuadrada(observable)
    if verificar_hermitiana and verificar_cuadrada:
        accion = cpx.accionMatrizVectorComplex(observable, estado)
        valor_esperado = cpx.innerProductVectorComplex(accion, estado)
        return valor_esperado

def varianza(ket, matriz):
    valor_esperado = valorEsperado(ket, matriz)
    matrizUnitaria = hacer_unitaria(matriz, valor_esperado)
    resta = resta_matrices(matriz, matrizUnitaria)
    produto = cpx.productMatrices(resta, resta)
    produto1 = hacervector(cpx.accionMatrizVectorComplex(produto, ket), len(ket))
    conjugada = hacervector(cpx.conjugadaMatrizComplex(ket), len(ket))
    varian = producto_vectores(conjugada, produto1)
    return varian

observable = [[(0, 0), (0, -1)],
              [(0, 1), (0, 0)]]

estado = [(1/math.sqrt(2), 0), (0, 1/math.sqrt(2))]

print(valorEsperado(observable, estado))