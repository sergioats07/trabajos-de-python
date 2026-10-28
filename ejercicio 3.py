def es_primo(numero):
    if numero <=1:
        return False
        
    
    limite = int(numero**0.5)+1    
    for i in range (2,limite):
        if numero % i==0:
            return False 

    return True 

try:
    numero = int(input( "ingrese un numero entero positivo mayor a 1:"))
    if numero<=1:
        print ("el numero debe ser mayor a 1")
    else: 
        if es_primo(numero):
            print (numero, "es primo")
        else: print (numero, "no es primo")

except ValueError:
    print ("debe ingresar un numero entero positivo mayor a 1")

    