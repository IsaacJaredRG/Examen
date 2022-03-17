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
        def fibonacci(num):
            arr =[0,1]
            if num==1:
                print('0')
            elif num==2:
                print('[0','1]')
            else :
                while(len(arr)<num):
                    arr.append(0)
                if (num==0 or num==1):
                    return 1
                else:
                    arr[0]=0
                    arr[1]=1
                    for i in range(2,num):
                        arr[i]=arr[i-1]+arr[1-2]
                        print(arr)
        fibonacci(10)

    #AREA DE UN CIRCULO (ALEJANDRO)
    elif b==2:
        print("area circulo")
        print(" ")
		print("Ingrese el radio del circulo")
		radio=float(input("Ingrese aqui "))
		print(" ")

		total1= (radio*radio*3.1416)

		print("El area del circulo es = ", total1)
		print(" ")
    
    #opcion incorrecta
    else:
        print("opcion no valida")
    print ("desea realizar otra operación?")
    print ("0. si")
    print ("1. no")
    a=int (input(""))

#despedida
print ("adios")

