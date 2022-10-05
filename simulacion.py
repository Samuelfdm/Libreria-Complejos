import libClasicoCuantico as ctc

def probabilisticSimulator():
    unClick = ctc.multiplesRendijasClasicoProbabilistico(2, 3, 1)
    dosClicks = ctc.multiplesRendijasClasicoProbabilistico(2, 3, 2)
    tresClicks = ctc.multiplesRendijasClasicoProbabilistico(2, 3, 3)
    print(unClick)
    print(dosClicks)
    print(tresClicks)
    ctc.diagramaProbabilistico(unClick[1])
    ctc.diagramaProbabilistico(dosClicks[1])
    ctc.diagramaProbabilistico(tresClicks[1])

def quantumSimulator():
    unClick = ctc.multiplesRendijasCuantico(2, 3, 1)
    dosClicks = ctc.multiplesRendijasCuantico(2, 3, 2)
    tresClicks = ctc.multiplesRendijasCuantico(2, 3, 3)
    print(unClick)
    print(dosClicks)
    print(tresClicks)
    ctc.diagramaCuantico(unClick[1])
    ctc.diagramaCuantico(dosClicks[1])
    ctc.diagramaCuantico(tresClicks[1])

#probabilisticSimulator()
quantumSimulator()