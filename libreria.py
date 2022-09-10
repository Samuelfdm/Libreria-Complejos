import math
#------------PRIMERA VERSIÓN------------
# Realiza el producto entre dos números complejos:
def productComplex(a, b):
    return ((a[0]*b[0] - a[1]*b[1]), (a[0]*b[1] + a[1]*b[0]))

# Resta dos números complejos:
def restaComplex(a, b):
    return ((a[0]-b[0]), (a[1]-b[1]))

# Suma dos números complejos:
def sumComplex(a, b):
    return ((a[0]+b[0]), (a[1]+b[1]))

# Divide dos números complejos:
def diviComplex(a, b):
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

#------------SEGUNDA VERSIÓN------------
# Suma dos vectores complejos:
def sumVectorComplex(v1, v2):
    v3 = []
    for i in range(len(v1)):
        v3.append(sumComplex(v1[i], v2[i]))
    return v3

# Devuelve el inverso aditivo de un vector complejo:
def inversoVectorComplex(v):
    v2 = []
    for i in range(len(v)):
        v2.append(((v[i][0])*(-1), (v[i][1])*(-1)))
    return v2

# Multiplica un vector complejo por un escalar:
def escalarVectorComplex(c, v):
    v2 = []
    for i in range(len(v)):
        v2.append(productComplex(c, v[i]))
    return v2

# Suma dos matrices complejas:
def sumMatrizComplex(m1, m2):
    m3 = []
    for i in range(len(m1)):
        m3.append(sumVectorComplex(m1[i], m2[i]))
    return m3

# Devuelve la inversa aditiva de una matriz compleja:
def inversaMatrizComplex(m):
    m2 = []
    for i in range(len(m)):
        m2.append(inversoVectorComplex(m[i]))
    return m2

# Multiplica una matriz compleja por un escalar:
def escalarMatrizComplex(c, m):
    m2 = []
    for i in range(len(m)):
        m2.append(escalarVectorComplex(c,m[i]))
    return m2

# Devuelve la traspuesta de una matriz:
def traspuestaMatrizComplex(m):
    for i in range(len(m)):
        for k in range(i+1, len(m[i])):
            m[i][k], m[k][i] = m[k][i], m[i][k]
    return m

# Devuelve la traspuesta de un vector:
def traspuestaVectorComplex(v):
    return [[v[i]] for i in range(len(v))]

# Devuelve la conjugada de un vector:
def conjugadaVectorComplex(v):
    return [(v[i][0], (v[i][1])*-1) for i in range(len(v))]

# Devuelve la conjugada de una matriz:
def conjugadaMatrizComplex(m):
    return [conjugadaVectorComplex(m[i]) for i in range(len(m))]

# Devuelve la adjunta de un vector:
def adjuntaVectorComplex(v):
    return traspuestaVectorComplex(conjugadaVectorComplex(v))

# Devuelve la adjunta de una matriz:
def adjuntaMatrizComplex(m):
    return traspuestaMatrizComplex(conjugadaMatrizComplex(m))

# Realiza el producto entre dos matrices (de tamaños compatibles):
def productMatrices(m1, m2):
    a, b, c, d = len(m1), len(m1[0]), len(m2), len(m2[0])
    if b!=c:
        return "ES IMPOSIBLE REALIZAR LA OPERACIÓN, REVISE LA ENTRADA"
    else:
        m3 = []
        for i in range(a):
            filas_m3 = []
            for k in range(d):
                acum = (0, 0)
                for j in range(b):
                    c1 = m1[i][j]
                    c2 = m2[j][k]
                    acum = sumComplex(acum, productComplex(c1, c2))
                filas_m3.append(acum)
            m3.append(filas_m3)
    return m3

# Calcula la acción de una matriz sobre un vector:
def accionMatrizVectorComplex(m, v):
    a, b, c = len(m), len(v), len(m[0])
    if b != c:
        return "ES IMPOSIBLE REALIZAR LA OPERACIÓN, REVISE LA ENTRADA"
    else:
        v_new = []
        for i in range(a):
            acum = (0, 0)
            for k in range(b):
                c1 = m[i][k]
                c2 = v[k]
                acum = sumComplex(acum, productComplex(c1, c2))
            v_new.append(acum)
    return v_new

# Calcula el producto interno de dos vectores:
def innerProductVectorComplex(v1, v2):
    v_con = conjugadaVectorComplex(v1)
    acum = (0, 0)
    for i in range(len(v_con)):
        acum = sumComplex(acum, productComplex(v_con[i], v2[i]))
    return acum

# Calcula la norma de un vector:
def normaVectorComplex(v):
    return math.sqrt(innerProductVectorComplex(v,v)[0])

# Calcula la distancia entre dos vectores:
def distanciaVectorComplex(v1,v2):
    v3 = []
    for i in range(len(v1)):
        v3.append(restaComplex(v1[i], v2[i]))
    return normaVectorComplex(v3)

# Determina si una matriz es hermitiana:
def hermitianaMatrizComplex(m):
    return adjuntaMatrizComplex(m)==m

# Determina si una matriz es unitaria: