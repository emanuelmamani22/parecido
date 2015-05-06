def letras (a,k):
    for f in a :
        cont=0
        cont2=0
        p1=0
        p2=0
        contl=0
        if k == f :
            print 'hola'
            print "Hola"
        elif k != f :
            b=f
            c=len(b)
            while cont < c :
                if k[cont] == b[cont2] :
                    p1=p1+1
                    if p1 >=3 :
                        print "Quizas quiso decir "+b
                        break
                elif k[cont] != b[cont2] :
                    p2=p2+1
                cont=cont+1
                cont2=cont2+1
    
    if p2 >= 3 :
        print "Funcion letras" #borrar
        print "1. La palabra es correcta"
        print "2. Vuelva a escribir porfavor"
        op=input('Ingrese la opcion deseada')
        if op == 1 :
            bb=[]
            bb.append(k)
            letras(bb,k)
        elif op == 2 :
            menu() #fin de la funcion

def parecido (a): #funcion parecido
    lista=['Miller','Urien','Canuelas','hoola','saluda']
    contl=0
    a=a
    b=[]
    while contl < len(lista) :
        if len(a) == len(lista[contl]) :
            b.append(lista[contl])
        contl=contl+1
        
    if len(b) == 0 :
        print "Funcion parecido" #borrar
        print "1. La palabra es correcta"
        print "2. Volver a escribir"
        op=input('Elija la opcion: ')
        
        if op == 1  :
            b.append(a)
        elif op == 2 :
            menu()
    letras(b,a)

def menu (): #menu principal
    a=raw_input('Escribe: ')
    parecido(a)




menu()