if __name__ == '__main__':
    n = int(input("enter the nth number : "))
    l = 0
    for i in range(1,n+1):
        l += i
    seq = ['00006']
    for i in range(0,l-1):
        seq.append(str(int(seq[i])+(22+(16*i))))
        ln = len(seq[i+1])
        if ln < 5:
            seq[i+1] = ('0'*(5 - ln)) + seq[i+1]

    #print(seq)
  #  leq = []
    #for i in range(l):
     #   leq.append(len(seq[i]))
    for i in range(1,n+1):
        s = ((5*n) - i*5)//2
        print(" "*s,end=" ")
        for j in range(i):
            print(seq[j+i-1],end=" ")
        print()
