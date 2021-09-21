def isLucky(n):
    digit = [int(i) for i in str(n)]
    print(digit)
    mid = len(digit)//2
    summ1= summ2 = 0
    for i in range(len(digit)):
        if i<mid:
            summ1 += digit[i]
        if i >=mid:
            summ2+= digit[i]
    return summ1==summ2

