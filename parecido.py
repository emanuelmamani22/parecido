def parecido (a): #funcion parecido
    lista=['Urien']
    cont=0
    cont2=0
    p1=0
    p2=0
    if a == lista[0] :
        print "Hola"
    elif a != lista[0] :
        b=lista[0]
        c=len(b)
        while cont < c :
            if a[cont] == b[cont2] :
                p1=p1+1
            elif a[cont] != b[cont2] :
                p2=p2+1
            cont=cont+1
            cont2=cont2+1
            
    if p1 >=3 :
        print "Quizas quiso decir "+b
    elif p2 >= 3 :
        print "Vuelva a escribir porfavor"
        menu() #fin de la funcion

def menu (): #menu principal
    a=raw_input('Escribe: ')
    parecido(a)




menu()