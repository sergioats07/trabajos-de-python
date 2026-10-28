intento=0
secreto=9

while intento != secreto:
    intento=int(input("adivina el numero secreto: "))
    if intento < secreto:
        print ("el numero secreto es mayor")
        print(" intenta de nuevo")
    elif intento > secreto:
        print ("el numero secreto es menor")
        print ("intenta de nuevo")

print ("felicidades, adivinaste el numero secreto")

 