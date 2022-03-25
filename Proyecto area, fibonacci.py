#Proyecto donde puedas sacar el area del circulo y los numeros de fibonacci
a=0
while a==0:
    print("elija la opcion que desea realizar")
    print ("1. Numeros fibonacci")
    print ("2. Area del circulo")
    b=int (input(""))
    #NUMERO FIBONACCI (MELANY)
    if b==1:
        num1=0
        num2=0
        num3=1
        num4=1
        e=0
        f=0

        print("Dame una cantidad de numeros fibonacci")
        num1= int(input(""))
        while (e<num1):
            e=e+1
            print(num2)
            f=num2+f
            num4= num2+num3
            num2=num3
            num3=num4
    #AREA DE UN CIRCULO (ALEJANDRO)
    #opcion incorrecta
    else:
        print("opcion no valida")
    print ("desea realizar otra operación?")
    print ("0. si")
    print ("1. no")
    a=int (input(""))

#despedida
print ("adios")

