a=input()
b=a.replace(",", " ")
b=b.split()
b=[int(x) for x in b]
print(b)