a= int(input("a: "))
b=int(input("b: "))

while b!=0:
   q=int(a/b)
   r=a-b*q
   a=b
   b=r
print("man, le pgcd est "+str(a))

