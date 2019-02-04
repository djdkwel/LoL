def findMinGameCycle(e, n, mini):
    count = 1
    totalMini = mini
    e+=1
    e*=2**(n-1)
    while(totalMini<e):
        mini+=1
        count+=1
        n+=count
        totalMini+=mini       
    return n
