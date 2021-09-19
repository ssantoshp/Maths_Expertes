import math

n=eval(input())
print("\n")
nsqrt=math.sqrt(n)
new_n=math.floor(nsqrt)

for i in range(1,new_n+1):
  if n%i==0:
    print(i)
    if i==int(n/i):
      pass
    else:
      print(int(n/i))
