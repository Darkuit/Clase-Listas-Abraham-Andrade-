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

x=[-22, 4, -3]
sustituir0(x)
y=[-1, -2, 788, 12, 45, 76, -21, 85, 123, 3, -2, 234, 746, 7346, 1234, 34, 7897,231,-34, 1]
sustituir0(y)
z=[-3,45, -2, 8]
sustituir0(z)
    
