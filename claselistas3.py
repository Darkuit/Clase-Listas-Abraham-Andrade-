def delpar(x):
    z=0
    y=[]
    while z<len(x):
        
        if z%2!=0:
            y.append(x[z])
        else:
            print('Eliminando el elemento', x[z],' con indice: ', z)
        z+=1
        
    return y

