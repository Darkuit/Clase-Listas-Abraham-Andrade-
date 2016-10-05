def Maxlista(x):
    maxlista=0
    z=0
    while z<len(x):
        if x[z]>=maxlista:
            maxlista=x[z]
        z+=1
    print('El máximo número de la lista es: ',maxlista)
x=[1, 4, 3]
Maxlista(x)
z=[5, 8 , 16, 24, 9, 7, 18, 6, 25, 45, 164, 9, 20, 214, 87, 3014, 56, 24, 19, 22]
Maxlista(z)
y=[8, 42, 23, 25]
Maxlista(y)
