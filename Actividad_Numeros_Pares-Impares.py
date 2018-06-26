import random
i=int(input("Introduce cuántos números quieres en la lista: "))
k=int(input("Introduce el valor límite para estos números : "))
m=1
g=[]
#Aqui agrego a la lista números Brandom del 1 al número que se insertó
while (m<=i):
    x=random.randint(1,k)
    g.append(x)
    m+=1
a=len(g)
a-=1
m=0
c=[]
v=[]
#Aqui verifico cuáles son pares y cuales no ;)
while (m<=a):
    l=g[m]
    u=l%2
    if(u==0):
        c.append(l)
    else:
        v.append(l)
    m+=1
print("De la lista", g, "los numeros pares son", c, "y los impares son", v)
        