if __name__ == '__main__':
    r,c = input().split(',')
    r,c = int(r),int(c)
    chutes = [[] for i in range(r)]
    l = []
    print("enter chutes values")
    for i in range(r):
        val = list(input().split(','))
        for j in range(c):
            chutes[i].append(int(val[j]))
    for i in range(0,r*c):
        m = 0
        for j in range(r):
            if chutes[j][c-1] > m:
                m = chutes[j][c-1]
                ind = j
        l.append(str(chutes[ind][c-1]))
        #print(temp)
        chutes[ind][1:c] = chutes[ind][0:c-1]
        chutes[ind][0] = 0
        print(chutes)
    res = ''.join(l)
    print(res)
