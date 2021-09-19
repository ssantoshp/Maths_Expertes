num = eval(input())
print("\n")
if num > 1:
 
    for i in range(2, int(num/2)+1):

        if (num % i) == 0:
            print(i)
            print(num, "est pas un nombre premier")
            break
    else:
        print(num, "est un nombre premier")
 
else:
    print(num, "est pas un nombre premier")
