def chakra(n):
    arr = [[0 for i in range(n)] for i in range(n)]
    t,b,l,r,p,k = 0,n,0,n,1,1
    while(t <= b and l <= r):
        for i in range(l,r):
            arr[t][i] = k
            k += 1
        t += 1
        for i in range(t,b):
            arr[i][r-1] = k
            k += 1
        r -= 1
        if t <= b:
            for i in range(r-1,l-1,-1):
                arr[b-1][i] = k
                k += 1
            b -= 1
        if l <= r:
            for i in range(b-1,t-1,-1):
                arr[i][l] = k
                k += 1
            l += 1
    for i in range(n):
        print(arr[i])
    for i in range(n):
        for j in range(n):
            if arr[i][j] % 11 == 0:
                p += 1
    print("power is : " , p)
    print("power coordinates are : \n")
    print("[0][0] \n")
    for i in range(n):
        for j in range(n):
            if arr[i][j] % 11 == 0:
                print("[{}][{}]".format(i,j))


if __name__ == "__main__":
    n = int(input("enter size : "))
    chakra(n)
