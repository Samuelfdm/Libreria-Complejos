import math

# Multiplica dos números complejos:
def multiComplex(a,b):
    return ((a[0]*b[0] - a[1]*b[1]), (a[0]*b[1] + a[1]*b[0]))

# Resta dos números complejos:
def restaComplex(a,b):
    return ((a[0]-b[0]),(a[1]-b[1]))

# Suma dos números complejos:
def sumComplex(a,b):
    return ((a[0]+b[0]),(a[1]+b[1]))

# Divide dos números complejos:
def diviComplex(a,b):
    denominador = b[0]**2 + b[1]**2
    numerador1 = a[0] * b[0] + a[1] * b[1]
    numerador2 = b[0] * a[1] - a[0] * b[1]
    return ((numerador1/denominador), (numerador2/denominador))

# Devuelve el módulo de un número complejo:
def moduloComplex(num):
    return (num[0]**2 + num[1]**2)**(1/2)

# Devuelve el conjugado de un número complejo:
def conjugadoComplex(num):
    return (num[0], num[1]*-1)

# Convierte un número complejo de forma cartesiana a forma polar:
def cartesian_to_polarComplex(num):
    p = moduloComplex(num)
    angulo = math.atan(num[1]/num[0])
    return (p, angulo)

# Convierte un número complejo de forma polar a forma cartesiana:
def polar_to_cartesianComplex(num):
    r = cartesian_to_polarComplex(num)
    a = r[0]*math.cos(r[1])
    b = r[0]*math.sin(r[1])
    return (a, b)

# Devuelve la fase de un número complejo:
def faseComplex(num):
    return math.atan(num[1]/num[0])

# Suma dos vectores complejos:
