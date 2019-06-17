def is_prime(n):
    c = 0
    if n < 2 :
        return False
    elif n == 2 :
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3,n-1):
            if n % i == 0 :
                c += 1
            if c == 1:
                return False
                break
        return True
if __name__ == "__main__":
    print("enter the position : ")
    n = int(input())
    primes = []
    if n % 2 == 0:
        for i in range(10000):
            if is_prime(i):
                primes.append(i)
            if len(primes) == n//2:
                break
        print(primes[n//2 - 1])
    else :
        a,b = 1,1
        c = 0
        for i in range(3,(n//2)+2):
            c = a + b
            a = b
            b = c
        print(c)
    
