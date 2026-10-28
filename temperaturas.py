temperatura=float(input("ingrese la temperatura en grados fahrenheit: "))
deporte=""
if(temperatura>85):
    deporte="natacion"
elif(temperatura>70 and temperatura<=85):
    deporte="tenis"
elif(temperatura>=32 and temperatura<=70):
    deporte="golf"
elif(temperatura<32):
    deporte="esqui"

print("el deporte recomendando es ",deporte)
