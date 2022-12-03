import sys
import random
import time
import fractions


def main(args):
    dimension = int(input('Ingrese cuantas variables tiene su sistema de ecuaciones: '))
    dataTime = {}
    if 'random' in args:
        start = time.time()
        data = randomData(dimension)
        end = time.time()
        dataTime['ramdon'] = start - end
    else:
        start = time.time()
        data = getData(dimension) 
        end = time.time()
        dataTime['getdata'] = abs(start - end) #no se por que esto me da negativo.
        
    start = time.time()
    matrixDeterminan = matrix(data)
    end = time.time()
    dataTime['matrix'] = start - end
    
    start = time.time()
    calcdeterminant = calcDeterminantByMatrixs(matrixDeterminan)
    start = time.time()
    dataTime['determinante'] = start - end
    
    start = time.time()
    result = calc(calcdeterminant)
    end = time.time()
    dataTime['calcular'] = start - end
    
    
    if 'debug' in args:
        start = time.time()
        debug(data, matrixDeterminan, calcdeterminant, result)
        start = time.time()
        dataTime['debug'] = start - end
        
    if 'time' in args:
        ptime(dataTime)
        
    printResult(result)
    return
    
def ptime(data):
    print("\n")
    suma = 0
    print(rowHr('Time'))
    for key in data:
        print("En hacer: '", key, "' se tardo: ", data[key], " segundos")
        suma = suma + data[key]
    print("El programa tardo: ", suma, " segundos en ejecutarse")
    print("\n")

def debug(data, matrixDeterminan, calcdeterminant,  result):
    ln()
    rigthAndLeft = pullApartData(data)
    print(rowHr('DEBUING')+'\n')
    print(rowHr('Vanilla data'))
    showMatrix(data)
    print(rowHr('Derecha y izquierda'))
    showMatrix(rigthAndLeft)
    print(rowHr('Matrices de determinantes'))
    showMatrix(matrixDeterminan)
    print(rowHr('determinantes'))
    print(calcdeterminant)
    print(rowHr('Resultado'))
    print(result)
    print('\n')
    
def calc(determinants):
    result = []
    Ds = determinants[0]
    if Ds != 0:
        for i in range(len(determinants) - 1):
            result.append(determinants[i + 1]/ Ds)
        return result
    else:
        print('La determinante del sistema es ' + str(Ds)+ " el sistema no tiene solucion")
        exit(1)

def printResult(result):
    print(rowHr('Resultado en decimales'))
    for i in range(len(result)):
        print('La incognita ' + str(i + 1 ) + ' es: ' + str(result[i]) )
    print(rowHr('Resultado en fracciones'))
    for i in range(len(result)):
        print('La incognita ' + str(i + 1 ) + ' es: ' + str(fractions.Fraction(result[i])) )
    ln()

def calcDeterminantByMatrix(matrix): # Teorema de Laplace
    Ma = [k[:] for k in matrix]
    dimension = len(matrix)
    suma = 0
    if dimension > 2:
        for i in range(dimension):
            factor = Ma[0][i]
            signo = -2 * (i % 2) + 1
            Ma.remove(Ma[0])
            for j in range(0, dimension - 1):
                Ma[j].pop(i)
            suma = suma + factor * signo * calcDeterminantByMatrix(Ma)
            Ma = [k[:] for k in matrix]
        return suma
    elif dimension == 2:
        return (Ma[0][0] * Ma[1][1]) - (Ma[0][1] * Ma[1][0])
    else:
        return Ma
    
    
def calcDeterminantByMatrixs(matrixs):
    determinanst = []
    for i in matrixs:
        determinanst.append(calcDeterminantByMatrix(i))
    return determinanst

def matrix(data):
    matrixs = []
    data = pullApartData(data)
    ds = arrayChunk(data[0], len(data[1])) #la variable ds contiene la matriz del sistema
    matrixs.append(ds)
    for i in range(len(ds)):
        matrix = insertColumn(arrayChunk(data[0], len(data[1])), data[1], i)
        matrix = deleteColumn(matrix, i + 1 )
        matrixs.append(matrix)
    return matrixs
def getData(iterable):
    r = []
    for n in range(iterable): #TODO hacer un while  
        f = []
        for i in range(iterable):   
            f.append(float(input("Ingrese el valor "+  str(i + 1) +  " de la encuacion "+str(n + 1)+": ")))
        f.append(float(input("Ingrese la igualdad de la encuacion " + str(n + 1) + ": ")))
        r.append(f)
    return r
def pullApartData(data):
    right = [] 
    left = []
    for equations in data:
        x = 0
        for constants in equations:
            x += 1
            if x != len(equations): 
                left.append(constants)
            else:
                right.append(constants)
    return [left, right]

def arrayChunk(array, n):
    return [array[i:i + n] for i in range(0, len(array), n)]
def getColumn(matrix,column): 
    result = []
    for val in matrix:
        result.append(val[column])
    return result
def deleteColumn(matrix,column):
    result = []
    for val in matrix:
        val.pop(column)
        result.append(val)
    return result        
def insertColumn(matrix,column_instert,column):
    result = []
    for val,listval in zip(matrix,column_instert):
        val.insert(column,listval)
        result.append(val)
    return result

#funciones de estetica
def rowHr(text):
    return '============== '+ str(text) +' =============='
def showMatrix(matrix):
    for fila in matrix:
        for valor in fila:
            try:
                print(f"{valor:<10}", end=" ")
            except:
                print("\t", valor, end=" ")
        print()
def ln():
    print("\n")
#Funcion de datos ramdons

def randomData(dimension):
    result = []
    for i in range(dimension):
        result.append(ramdonArray(dimension + 1, i))
    return result
def ramdonArray(t, fors = 1):
    result = []
    for i in range(t):
        result.append(random.randrange(100*(i+1)*t*(fors + 1)))
    return result

        
def simplificar(numerador, denominador):
    for i in range(2, numerador):
        if numerador % i == 0 and denominador % i == 0:
            numerador = numerador // i
            denominador = denominador // i
    return numerador, denominador  

 
if '__main__' == __name__:
    if 'debug' in sys.argv:
        print('debug on')
    if 'time' in sys.argv:
        print('time on')
    if 'random' in sys.argv:
        print('random on')
    ln()
    main(sys.argv)