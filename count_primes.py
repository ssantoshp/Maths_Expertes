while True:
    n = eval(input())
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    final=[2] + [2*i+1 for i in range(1,n//2) if sieve[i]]
    print(final)
    print("Il y en a: "+ str(len(final)))
