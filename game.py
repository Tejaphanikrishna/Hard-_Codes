def toword(num):
    assert (0 <= num)
    d = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
        6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
        15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
        19: 'Nineteen', 20: 'Twenty',
        30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
        70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
    }
    h = [100, 'Hundred', 'Hundred']
    k = [h[0] * 10, 'Thousand', 'Thousand']
    m = [k[0] * 1000, 'Million', 'Million']
    b = [m[0] * 1000, 'Billion', 'Billion']
    t = [b[0] * 1000, 'Trillion', 'Trillion']
    if num < 20:
        return d[num]
    if num < 100:
        div_, mod_ = divmod(num, 10)
        return d[num] if mod_ == 0 else d[div_ * 10] + ' ' + d[mod_]
    else:
        if num < k[0]:
            divisor, word1, word2 = h
        elif num < m[0]:
            divisor, word1, word2 = k
        elif num < b[0]:
            divisor, word1, word2 = m
        elif num < t[0]:
            divisor, word1, word2 = b
        else:
            divisor, word1, word2 = t
        div_, mod_ = divmod(num, divisor)
        if mod_ == 0:
            return '{} {}'.format(toword(div_), word1)
        else:
            return '{} {} {}'.format(toword(div_), word2, toword(mod_))
if __name__ == '__main__':
    s = input().split(' ')
    n,m = int(s[0]),int(s[1])
    arr = [[0,''],[0,'']]
    if n < m:
        arr[0][0],arr[0][1] = n,toword(n)
        arr[1][0],arr[1][1] = m,toword(m)
    elif m < n:
        arr[0][0],arr[0][1] = m,toword(m)
        arr[1][0],arr[1][1] = n,toword(n)
    else:
        print(n)
    while arr[0][0] != arr[1][0] and arr[0][0] <= 99999 and arr[1][0] <= 99999:
            if arr[0][1] < arr[1][1]:
                arr[0][0] = arr[0][0] + arr[0][0]
                arr[0][1] = toword(arr[0][0])
                arr[1][0] = 2*arr[1][0]
                arr[1][1] = toword(arr[1][0])
            elif arr[0][1] > arr[1][1]:
                temp = arr[0][0]
                arr[0][0] = arr[0][0] + arr[1][0]
                arr[0][1] = toword(arr[0][0])
                arr[1][0] = arr[1][0] + temp
                arr[1][1] = toword(arr[1][0])
    if arr[0][0] > 99999 or arr[1][0] > 99999:
        print("Out of bounds")
    elif arr[0][0] == arr[1][0] and arr[0][0] > 0:
        print(arr[0][0])        
