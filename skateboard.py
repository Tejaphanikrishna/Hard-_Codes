global c = []
def cnt(t,a,b):
    if t[a][b] == 'f':
        c += 1
        return
    elif t[a][b] == 'd':
        
    elif t[a][b] == 'se':
        cnt(t,a+1,b)
    elif t[a][b] == 'es':
        cnt(t,a,b+1)
    elif t[a][b] == 's':
        cnt(t,a+1,b)
    elif t[a][b] == 'e':
        cnt(t,a,b+1)
    elif t[a][b] == 'w':
        if b > 0:
            cnt(t,a,b-1)
    elif t[a][b] == 'n':
        if a > 0:
            cnt(t,a-1,b)
if __name__ == '__main__':
    n = int(input("enter the size : "))
    s = [[]*n]
    print("enter matrix elements : ")
    for i range(n):
         s[i].append(str(input()))
    for i in range(n):
        for j in range(n):
            print(s[i][j],end=" ")
        print()
    for i in range(n):
        cnt(s,i,0)
    for j in range(n):
        cnt(0,j)
    print(c)
