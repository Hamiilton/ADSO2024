n1=int(input('Señor usuario digite el primer numero:'))
n2=int(input('Señor usuario digite el segundo numero: '))
n3=int(input('Señor usuario digite el tercer numero:'))

if n1==n2:
    if n2==n3:
        print('Señor usuario los 3 numeros son iguales')
    else:
        print('Señor usuario solo el primer y segundo numero son iguales')
elif n3 == n2:
    print('Señor usuario el segundo numero y el tercer numero son iguales')
else:
    if n1 == n3:
        print('Señor usuario solo el primer y el tercer nnumero son iguales')
    else:
        print('Señor usuario ningun numero es igual')
