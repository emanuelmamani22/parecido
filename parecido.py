lista=['urien']
a=raw_input('Escribe: ')
cont=0
cont2=0
if a == lista[0] :
    print "Hola"
elif a != lista[0] :
    b=lista[0]
    c=len(b)
    while cont < c :
        if a[cont] == b[cont2] :
            print "Son iguales "+a[cont]+" y "+b[cont2]
        elif a[cont] != b[cont2] :
            print "No son iguales "+a[cont]+" y "+b[cont2]
        cont=cont+1
        cont2=cont2+1