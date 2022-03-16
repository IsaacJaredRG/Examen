#Proyecto donde puedas sacar el area del circulo y los numeros de fibonacci
a=0
while a==0:
    print("elija la opcion que desea realizar")
    print ("1. Numeros fibonacci")
    print ("2. Area del circulo")
    b=int (input(""))
    #NUMERO FIBONACCI (MELANY)
    if b==1:
        print("numeros fibonacci")

    #AREA DE UN CIRCULO (ALEJANDRO)
    elif b==2:
        print("area circulo")
    
    #opcion incorrecta
    else:
        print("opcion no valida")
    print ("desea realizar otra operación?")
    print ("0. si")
    print ("1. no")
    a=int (input(""))

#despedida
print ("adios")

