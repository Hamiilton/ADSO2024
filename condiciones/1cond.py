n1=int(input('Ingrese el primer numero: '))
n2=int(input('Ingrese el segundo numero: '))
n3=int(input('Ingrese el tercer numero: '))

if n1 > n2 and n1 < n3:
    print(f'El primer numero ({n1}) es el de la mitad')
elif n1 < n2 and n1 > n3:
    print(f'El primer numero ({n1}) es el de la mitad')
elif n2 > n3 and n2 < n1:
    print(f'El segundo numero ({n2}) es el de la mitad')
elif n2 < n3 and n2 > n1:
    print(f'El segundo numero ({n2}) es el de la mitad')
elif n3 > n1 and n3 < n2:
    print(f'El tercer numero ({n3}) es el de la mitad')
elif n3 < n1 and n3 > n2:
    print(f'El tercer numero ({n3}) es el de la mitad')
    





        


