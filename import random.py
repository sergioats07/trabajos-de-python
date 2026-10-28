import random


tablero = []
for i in range(8):
    fila = ["X", "X", "X", "X", "X", "X", "X", "X"]
    tablero.append(fila)


minas = []
while len(minas) < 10:
    f = random.randint(0, 7)
    c = random.randint(0, 7)
    
    if (f, c) not in minas:
        minas.append((f, c))


en_juego = True

while en_juego:
    
    print("\n    0 1 2 3 4 5 6 7")
    print("  -----------------")
    for i in range(8):
       
        linea = str(i) + " |"
        for j in range(8):
            linea += " " + tablero[i][j]
        print(linea)
    
    print("\n¿Qué quieres hacer?")
    print("1. Destapar casilla")
    print("2. Marcar casilla (P)")
    print("3. Desmarcar casilla")
    
    accion = input("Elige 1, 2 o 3: ")
    fila = int(input("Elige la fila (0 a 7): "))
    columna = int(input("Elige la columna (0 a 7): "))
    
    
    if accion == "1":
        if (fila, columna) in minas:
            print("\n¡BOOM! ¡Había una mina! Perdiste el juego 😢")
            en_juego = False
        else:
            tablero[fila][columna] = " "  
            print("¡Bien! Casilla segura.")
            
    
    elif accion == "2":
        tablero[fila][columna] = "P"
        print("Casilla marcada.")
        
    
    elif accion == "3":
        tablero[fila][columna] = "X"
        print("Casilla desmarcada.")