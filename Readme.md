# LIBRERÍA DE NÚMEROS COMPLEJOS

## Versión #1: Operaciones Basicas con numeros complejos.

#### Operaciones con números complejos.
#### En esta primera versión de la librería encontramos una serie de operaciones basicas entre numeros complejos, tales como:
#### 1.- Multiplicación
#### 2.- Resta
#### 3.- Suma
#### 4.- División
#### 5.- Módulo
#### 6.- Conjugado 
#### 7.- Conversión entre representaciones polar y cartesiano
#### 8.- Fase

## Versión #2: Operaciones para vectores y Matrices.

#### En esta segunda versión de la librería encontramos operaciones más avanzadas que incluyen vectores y matrices, tales como:

#### 1.- Adición de vectores complejos.
#### 2.- Inverso (aditivo) de un vector complejo.
#### 3.- Multiplicación de un escalar por un vector complejo.
#### 4.- Adición de matrices complejas.
#### 5.- Inversa (aditiva) de una matriz compleja.
#### 6.- Multiplicación de un escalar por una matriz compleja.
#### 7.- Transpuesta de una matriz/vector
#### 8.- Conjugada de una matriz/vector
#### 9.- Adjunta (daga) de una matriz/vector
#### 10.- Producto de dos matrices (de tamaños compatibles)
#### 11.- Función para calcular la "acción" de una matriz sobre un vector.
#### 12.- Producto interno de dos vectores
#### 13.- Norma de un vector
#### 14.- Distancia entre dos vectores
#### 15.- Revisar si una matriz es unitaria
#### 16.- Revisar si una matriz es Hermitiana
#### 17.- Producto tensor de dos matrices/vectores

# PROGRAMA SIMULACIÓN DE LO CLÁSICO A LO CUÁNTICO

#### En esta primera versión del programa de simulación del salto de lo clásico a lo cuántico, encontramos la solución a los experimentos de:

#### 1.- Experimento de las canicas con coeficiente booleanos
#### 2.- Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
#### 3.- Experimento de las múltiples rendijas cuántico.
#### 4.- Función para graficar con un diagrama de barras que muestra las probabilidades de un vector de estados.

## Versión N°3: COMPETENCIA DE LA DOBLE RENDIJA
La versión N°3 es una simulación del experimento de la doble rendija. Donde se podrá ver el fenomeno de intererencia y su interpretación con matrices.
                                                 
### Presentado por
Samuel Felipe Díaz M, Andrea Camila Torres González y Andres Serrato

### Docente
Luis Daniel Benavidez Navarro

### Asignatura
CNYT (Ciencias Naturales y Tecnología)

### Experimento de la rendija.

El siguiente experimento se realizó por primera vez, utilizando luz por Thomas Young en 1801, que buscaba demostrar comportamiento ondulatorio de la luz y lo cual termino creando una nueva teoría completamente nueva, relacionada con la física cuántica y que muestra un fenómeno muy difícil de explicar.

### Como funciona:

Muchos explican este experimento como la interferencia entre las ondas que se generan al momento que la onda original pasa por la doble rendija, pero al momento en que se prueba con lanzar soltar de a un electrón a la doble rendija, nunca mandando más de uno a la vez, se vuelve a generar el mismo patrón, como sí se encontrara con algún tipo de interferencia al momento de pasar por las rendijas, la física cuántica explica esto como que el electrón interfiere consigo mismo en múltiples universos, entonces aun así se mande un único electrón se encontrar con interferencia propia y se creara el patrón de interferencia que conocemos y esperamos para este experimento.

### Experimento:
Para realizar el experimento se debe seguir un procedimiento relativamente sencillo:
Lo primero que se debe hacer es diseñar el número de rendijas que se quieran probar, esta puede ser de 1, 2, hasta el número que físicamente uno sea capaz de crear, el resultado en cada una de ellas debería ser muy parecido si no es que el mismo.

Al ya tener las rendijas se crea una maqueta que tenga al fondo una pantalla para apreciar las imágenes que se generen enfrente de la pantalla se coloca la rendija que se quiera probar para el experimento, esta debe ser capaz de cambiar entre las rejillas, y por último, a una distancia que, cuando se prenda el laser cubra completamente las rejillas, se pone el laser para que se genera la imagen en la pantalla.

La dificultad a la hora de desarrollar el experimento es de poder crear las rendijas y que den la imagen que se busca.

### Materiales:

Para el experimento se requieren los siguientes materiales:
      
1. Papel aluminio o hojas blancas para crear las rendijas.
2. Marcador negro.
3. Laser.
4. Tabla de madera.

### Desarrollo:

En nuestro caso realizamos el experimento con 3 rendijas diferentes, de 1, 2 y 3 ranuras, de las cuales se espera que experimentalmente nos den iguales o muy parecidos los resultados con cada una de ellas.

### Experimento con 1 rendija:

Para empezar, el primer montaje que se debe realizar es el de una rendija, en donde se busca ver el fenómeno físico que se produce cuando el láser atraviesa, teóricamente se espera:

En donde la dispersión del láser se disminuye, pero la trayectoria se mantiene constante, el primer montaje cuenta de la rendija única y el laser que genera la proyección otra forma de entender el experimento a través de grafos se podría ver de la siguiente manera:

![](imgs/9.png)

En donde la forma de matriz se aprecia de la siguiente manera:

![](imgs/10.png)

Esto nos demuestra que hay 100 % de probabilidad que entre por la rendija única y después un 25% de tocar cualquiera de lo siguientes blancos y cada uno de los receptores es reflexivo consigo mismo.

### Experimento con 2 rendijas:

![](imgs/4.jpeg)

![](imgs/2.jpeg)

![](imgs/3.jpeg)

![](imgs/5.jpeg)

![](imgs/1.jpeg)

![](imgs/8.jpeg)

Una manera de poder entender este experimento en forma de grafos sería la siguiente, suponiendo que tenemos 6 receptores:

![](imgs/11.png)

Donde la matriz que representa la dinámica del sistema (teoricamente) sería la siguiente:

![](imgs/12.png)

Que en la practica, en codigo se ve de la siguiente manera:

![](imgs/13.png)

De la cual la probabilidad de estado despues de dos clicks de tiempo sería:

![](imgs/dosClicks.png)

Es decir que tenemos un 50% de probabilidad de que el rayo láser se vaya por alguna de las dos rendijas. Luego de pasar por alguna de las dos rendijas que vendrían a ser los estados 1 y 2 vemos que hay una probabilidad de 1/6 o 16.66 % de que toque alguno de los receptores.

### Simulación con pruebas de doble rendija, con 1, 2 y 3 clicks de tiempo:

![](imgs/a.png)
![](imgs/b.png)
![](imgs/c.png)
![](imgs/d.png)
![](imgs/e.png)

### Resultados clásico probabilistico:
![](imgs/unclick.png)
![](imgs/dosClicks.png)
![](imgs/tresClicks.png)
### Resultados cuántico:
![](imgs/unclickCuantico.png)
![](imgs/dosClicksCuantico.png)
![](imgs/tresClicksCuantico.png)

## Desarrollado con:
- Python - Lenguaje de Programación
## Construido con:
- [PyCharm](https://www.jetbrains.com/pycharm/) - IDE de Python
## Autor:
- **Samuel Felipe Díaz** - [*Samuelfdm*](https://github.com/Samuelfdm)
## Agradecimientos:
- #### Profesor Luis Benavidez
- <https://gist.github.com/PurpleBooth/109311bb0361f32d87a2>
- <https://www.youtube.com/watch?v=SWYqp7iY_Tc>
- <https://www.markdownguide.org/>
