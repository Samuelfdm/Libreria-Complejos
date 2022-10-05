import libClasicoCuantico as ctc

def imprimirMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def probabilisticSimulator():
    print("---------------SIMULADOR CLÁSICO PROBABILISTICO---------------")
    unClick = ctc.multiplesRendijasClasicoProbabilistico(2, 3, 1)
    dosClicks = ctc.multiplesRendijasClasicoProbabilistico(2, 3, 2)
    tresClicks = ctc.multiplesRendijasClasicoProbabilistico(2, 3, 3)
    print("RESULTADO DEL EXPERIMENTO DESPUÉS DE UN CLICK:")
    imprimirMatriz(unClick[0])
    print("ESTADO:", unClick[1])
    print("RESULTADO DEL EXPERIMENTO DESPUÉS DE DOS CLICKS:")
    imprimirMatriz(dosClicks[0])
    print("ESTADO:", dosClicks[1])
    print("RESULTADO DEL EXPERIMENTO DESPUÉS DE TRES CLICKS:")
    imprimirMatriz(tresClicks[0])
    print("ESTADO:", tresClicks[1])
    ctc.diagramaProbabilistico(unClick[1])
    ctc.diagramaProbabilistico(dosClicks[1])
    ctc.diagramaProbabilistico(tresClicks[1])

def quantumSimulator():
    print("---------------SIMULADOR CUÁNTICO---------------")
    unClick = ctc.multiplesRendijasCuantico(2, 3, 1)
    dosClicks = ctc.multiplesRendijasCuantico(2, 3, 2)
    tresClicks = ctc.multiplesRendijasCuantico(2, 3, 3)
    print("RESULTADO DEL EXPERIMENTO DESPUÉS DE UN CLICK:")
    imprimirMatriz(unClick[0])
    print("ESTADO:", unClick[1])
    print("RESULTADO DEL EXPERIMENTO DESPUÉS DE DOS CLICKS:")
    imprimirMatriz(dosClicks[0])
    print("ESTADO:", dosClicks[1])
    print("RESULTADO DEL EXPERIMENTO DESPUÉS DE TRES CLICKS:")
    imprimirMatriz(tresClicks[0])
    print("ESTADO:", tresClicks[1])
    ctc.diagramaCuantico(unClick[1])
    ctc.diagramaCuantico(dosClicks[1])
    ctc.diagramaCuantico(tresClicks[1])

probabilisticSimulator()
quantumSimulator()