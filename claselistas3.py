def delpar(x):
    z=0
    y=[]
    while z<len(x):
        
        if z%2!=0:
            y.append(x[z])
        else:
            print('Eliminando el elemento', x[z],' con indice: ', z)
        z+=1
        
x= [235, 346, 12, 765,87, 97]
delpar(x)
y=[978, 5, 8998 , 97, 654, 64, 97, 4659, -89, 123, 45, 234, 76, 235, 87, 253, 765, 23, 76, 25]
delpar(y)
z=[2, 134, 123, 34, 87, 9]
delpar(z)
