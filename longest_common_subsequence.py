def backtrace(c,i,j,x,y):
    if i == 0 and j == 0:
        return ""
    if x[i] == y[j]:
        return backtrace(c,i-1,j-1,x,y) + x[i]
    if c[i][j-1] > c[i-1][j]:
        return backtrace(c,i,j-1,x,y)
    return backtrace(c,i-1,j,x,y)
def commonChild(s1, s2):
    x = [0]
    for i in s1:
        x.append(i)
    y = [0]
    for i in s1:
        y.append(i)
    m = len(x)
    n = len(y)
    c = [[0] for i in range(m)]
    for i in range(n-1):
        c[0].append(0)
    for i in range(1,m):
        for j in range(1,n):
            if x[i] == y[j]:
                c[i].append(c[i-1][j-1] + 1)
            else:
                c[i].append(max(c[i-1][j],c[i][j-1]))
    r = backtrace(c,m-1,n-1,x,y)
    return len(r)
