

a = float(input('Primer dato de la ecuacion 1: '))
b = float(input('Segundo dato de la ecuacion 1: '))
c = float(input('Tercero dato de la ecuacion 1: '))
d = float(input('La igualdad de la ecuacion 1: '))

e = float(input('Primer dato de la ecuacion 2: '))
f = float(input('Segundo dato de la ecuacion 2: '))
g = float(input('Primer dato de la ecuacion 2: '))
h = float(input('La igualdad de la ecuacion 2: '))

i = float(input('Primer dato de la ecuacion 3: '))
j = float(input('Segundo dato de la ecuacion 3: '))
k = float(input('Tercero dato de la ecuacion 3: '))
l = float(input('La igualdad de la ecuacion 3: '))


determinanteDelSistema = a*(f*k - g*j) - b*(e*k - i*g) + c*(e*j - f*i)
determinanteDeX =  d*(f*k - g*j) - b*(h*k - l*g) + c*(h*j - l*f)
determinanteDeY = a*(h*k - g*l) - d*(e*k - i*g) + c*(e*l - i*h) 
determinanteDeZ = a*(f*l - h*j) - b*(e*l - i*h) + d*(e*j - i*f)

if determinanteDelSistema != 0: 
    x = determinanteDeX/determinanteDelSistema
    y = determinanteDeY/determinanteDelSistema
    z = determinanteDeZ/determinanteDelSistema
    print('x = '+str(x))
    print('y = '+str(y))
    print('z = '+str(z))
else:
    print("La ecuacion no tiene solucion porque la determinante es " + str(determinanteDelSistema))