def rearrangeLastN(l, n):
    if l == None:
        return
    lList = []
    while l != None:
        lList.append(l.value)
        l = l.next
    # print(lList)
    return lList[-n:] + lList[:-n]
