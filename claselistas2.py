def sustituir0(x):
    z=0
    y=[]
    while z<len(x):
        if x[z]<0:
            y.append(0)
        else:
            y.append(x[z])
        z+=1
    print('Lista original: ', x,' lista resultado: ', y)

    
