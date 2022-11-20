
    
    
def main():
    print('Funcion para resolver ecuaciones de dos variables')
    numSystemEcuation = int(input('Ingrese cuantas variables tiene su sistema de ecuaciones: '))

    data = getData(numSystemEcuation)
    matrixs = matrix(data)
    
   # print(data)
    #print(matrixs)


def matrix(data):
    derecha = [] 
    left = []
    d = []
    for ecuations in data:
        x = 0
        for constantes in ecuations:
            x += 1
            if x != len(ecuations): 
                left.append(constantes)
            else:
                derecha.append(constantes)

    ds = arrayChunk(left, len(data))
    d.append(ds)
    t = []
    for i in range(len(ds)):
        t.append(ds[i][i - 1 ])
   # d.append(t)
    matrixs = [left, derecha]  
    print(d)    
    return ds

def sarrus(matrix):
    return

def determinat2x2(matrix):
    return


def getData(iterable):
    r = []
    for n in range(iterable): #TODO hacer un while  
        f = []
        for i in range(iterable):   
            f.append((input("Ingrese el valor "+  str(i + 1) +  ": ")))
        f.append(input("Ingrese la igualdad: "))
        r.append(f)
    return r


def arrayChunk(array, n):
    return [array[i:i + n] for i in range(0, len(array), n)]

    
    
    
if '__main__' == __name__:
    main()