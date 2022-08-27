import math

def sumComplex(a,b):
    return ((a[0]+b[0]),(a[1]+b[1]))

def multiComplex(a,b):
    return ((a[0]*b[0] - a[1]*b[1]), (a[0]*b[1] + a[1]*b[0]))

def restaComplex(a,b):
    return ((a[0]-b[0]),(a[1]-b[1]))

def diviComplex(a,b):
    denominador = b[0]**2 + b[1]**2
    numerador1 = a[0] * b[0] + a[1] * b[1]
    numerador2 = b[0] * a[1] - a[0] * b[1]
    return ((numerador1/denominador), (numerador2/denominador))

def moduloComplex(num):
    return (num[0]**2 + num[1]**2)**(1/2)

def conjugadoComplex(num):
    return (num[0], num[1]*-1)

def cartesian_to_polarComplex(num):
    p = moduloComplex(num)
    angulo = math.atan(num[1]/num[0])
    return (p, angulo)

def polar_to_cartesianComplex(num):
    r = cartesian_to_polarComplex(num)
    a = r[0]*math.cos(r[1])
    b = r[0]*math.sin(r[1])
    return (a, b)

def faseComplex(num):
    return math.atan(num[1]/num[0])


a = (1, 1)

b = (1, 2)