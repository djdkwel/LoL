def LoL(n,e):
    totalEnemies = 1
    totalEnemies+=e
    count = 1
    y=[]
    y.append(totalEnemies)
    x=[]
    x.append(e)
    e+=1
    x.append(e)
    while(count<n):
        totalEnemies*=2
        y.append(totalEnemies)
        e*=2
        x.append(e)
        count+=1
    print(x)
    print(y)
    print(count)
