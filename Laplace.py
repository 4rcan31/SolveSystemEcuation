
import sys


def main(args):
    dimension = int(input('Ingrese cuantas variables tiene su sistema de ecuaciones: '))
    data = getData(dimension)
    matrixDeterminan = matrix(data)
    calcdeterminant = calcDeterminantByMatrixs(matrixDeterminan)
    result = calc(calcdeterminant)
    if 'debug' in args:
        debug(data, matrixDeterminan, calcdeterminant, result)
    printResult(result)
    
    
    

def debug(data, matrixDeterminan, calcdeterminant,  result):
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
    for i in range(len(determinants) - 1):
        result.append(determinants[i + 1]/ Ds)
    return result

def printResult(result):
    for i in range(len(result)):
        print('La incognita ' + str(i + 1 ) + ' es: ' + str(result[i]) )

def calcDeterminantByMatrix(matrix): # Teorema de Laplace
    B = [k[:] for k in matrix]
    dimension = len(matrix)
    suma = 0.0
    if dimension > 2:
        for i in range(dimension):
            factor = B[0][i]
            signo = -2 * (i % 2) + 1
            B.remove(B[0])
            for j in range(0, dimension - 1):
                B[j].pop(i)
            suma = suma + factor * signo * calcDeterminantByMatrix(B)
            B = [k[:] for k in matrix]
        return suma
    elif dimension == 2:
        return (B[0][0] * B[1][1]) - (B[0][1] * B[1][0])
    else:
        return B
    
    
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
    for ecuations in data:
        x = 0
        for constantes in ecuations:
            x += 1
            if x != len(ecuations): 
                left.append(constantes)
            else:
                right.append(constantes)
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
            print("\t", valor, end=" ")
        print()

if '__main__' == __name__:
    main(sys.argv)