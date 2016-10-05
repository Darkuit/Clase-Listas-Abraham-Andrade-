def Maxlista(x):
    maxlista=0
    z=0
    while z<len(x):
        if x[z]>=maxlista:
            maxlista=x[z]
        z+=1
    print('El máximo número de la lista es: ',maxlista)
