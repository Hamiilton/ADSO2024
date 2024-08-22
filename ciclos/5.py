from functools import reduce
conj1=set({1,2,3,4,5,6})
conj2=set({7,8,9,10})
c1c2=conj1.union(conj2)
print(c1c2)
resultado=1
for valor in c1c2:
    resultado *=valor
print(resultado)