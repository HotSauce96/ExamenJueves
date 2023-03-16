#Programa que reciba 20 numeros enteros y muestre: multiplos de 2, multiplos de 3, multiplos de 2 y 3 al mismo tiempo

for i in range (0, 5):
    numeroIngresado = int(input("Ingrese un numero: "))
    
    if numeroIngresado %2 == 0 and numeroIngresado %3:
        print(numeroIngresado, "es múltiplo de 2 y de 3")
    elif numeroIngresado %3 == 0:
        print(numeroIngresado," El numero es múltiplo de 3")
    elif numeroIngresado %2 == 0:
        print(numeroIngresado,"es múltiplo de 2")
