import sys
def letras (a,k):
     y=False
     for f in a :
        if y == True :
            break
        cont=0
        cont2=0
        p1=0
        p2=0
        contl=0
        if k != f :
            b=f
            c=len(b)
            while cont < c :
                if k[cont] == b[cont2] :
                    p1=p1+1
                    if p1 >=3 :
                        print "Quizas quiso decir "+b
                        y=True
                        break
                elif k[cont] != b[cont2] :
                    p2=p2+1
                cont=cont+1
                cont2=cont2+1
                
     if p2 >= 3 :
        print "Funcion letras" #borrar
        print "1. La palabra es correcta"
        print "2. Vuelva a escribir porfavor"
        op=input('Ingrese la opcion deseada:  ')
        if op == 1 :
            bb=[]
            bb.append(k)
            letras(bb,k)
        else:
            menu() #fin de la funcion

def buscar (a,k):
    a=a
    for f in a :
        if k == f :
            print "Hola" #aqui va el bloque de instrucciones a seguir cuando se encuentra la palabra en la lista
            del(a) #temporal
            sys.exit() #temporal
    if len(a) > 0 :
        letras(a,k)        

def parecido (k): #funcion parecido
    lista=['Miller','Urien','Canuelas','hoola','saluda']
    contl=0
    k=k
    a=[]
    while contl < len(lista) :
        if len(k) == len(lista[contl]) :
            a.append(lista[contl])
        contl=contl+1
        
    if len(a) == 0 :
        print "Funcion parecido" #borrar
        print "1. La palabra es correcta"
        print "2. Volver a escribir"
        op=input('Elija la opcion: ')
        
        if op == 1  :
            a.append(k)
        else:
            menu()
    buscar(a,k)

def menu (): #menu principal
    k=raw_input('Escribe: ')
    parecido(k)




menu()