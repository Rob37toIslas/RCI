class sokoban: #creamos una clase para el juego
    #Componentes del juego:
    #0-personaje
    #1-Espacio
    #2-cajas
    #3-Paredes
    #4-Metas
    #5 personaje_meta
    #6 caja_meta
    #controles:
    #a-Izquierda
    #d-Derecha
    #w-arriba
    #s-abajo

    mapa = [] #variable para crear un mapa

    personaje_fila = 0 #pocicion del personaje
    personaje_columna = 0#pocicion del personaje 

    def __init__(self):
        pass

    def leerMapa(self):#metodo para leer mapa

        self.mapa = [
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 4, 3],
            [3, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 3, 3, 4, 3],
            [3, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 3, 3, 4, 3],
            [3, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 3, 3, 4, 3],
            [3, 1, 1, 4, 4, 6, 4, 0, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 3],
            [3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        ]
        self.personaje_fila = 6
        self.personaje_columna = 7

    def imprimirMapa(self):
        for fila in self.mapa:
            print(fila)

    def moverDerecha(self):  #movimientos ala derecha
        #personaje espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0
                and self.mapa[self.personaje_fila][self.personaje_columna + 1]== 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.personaje_columna += 1
        #personaje meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and
              self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.personaje_columna += 1
        #personaje_meta,espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 and
              self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.personaje_columna += 1

        #personaje,caja,espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and
              self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
              and self.mapa[self.personaje_fila][self.personaje_columna + 2]
              == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1

        #personaje,caja,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and
              self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
              and self.mapa[self.personaje_fila][self.personaje_columna + 2]
              == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1
        #personaje,caja_meta,espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 
              and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
              and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1
        #personaje_meta,caja y espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 
              and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
              and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1
        #personaje_meta,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.personaje_columna += 1
        #personaje,caja_meta,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and
              self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
              and self.mapa[self.personaje_fila][self.personaje_columna + 2]
              == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1
            #personaje_meta,caja_meta,espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
              and self.mapa[self.personaje_fila][self.personaje_columna + 2]== 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1
        #personaje_meta,caja,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 and
              self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
              and self.mapa[self.personaje_fila][self.personaje_columna + 2]
              == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1
        #personaje_meta,caja_meta,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 and
              self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
              and self.mapa[self.personaje_fila][self.personaje_columna + 2]
              == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1

    def moverIzquierda(self):  #movimientos ala izquierda
        #personaje,espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0
                and self.mapa[self.personaje_fila][self.personaje_columna - 1]== 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.personaje_columna -= 1
            #personaje,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 and
              self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.personaje_columna -= 1
        #personaje_meta,espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 
        and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.personaje_columna -= 1
        #personaje,caja,espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2
              and self.mapa[self.personaje_fila][self.personaje_columna] == 0
              and self.mapa[self.personaje_fila][self.personaje_columna - 2]
              == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.personaje_columna -= 1
        #personaje,caja,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4
              and self.mapa[self.personaje_fila][self.personaje_columna - 1]
              == 2
              and self.mapa[self.personaje_fila][self.personaje_columna] == 0):

            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.personaje_columna -= 1
            #personaje,caja_meta,espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1
              and self.mapa[self.personaje_fila][self.personaje_columna - 1]== 6
              and self.mapa[self.personaje_fila][self.personaje_columna] == 0):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2
            self.personaje_columna -= 1
        #personaje,caja_meta,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 
              and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6
              and self.mapa[self.personaje_fila][self.personaje_columna - 2]== 4):
                  
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1
        #personaje_meta,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna -1]==4
        and self.mapa[self.personaje_fila][self.personaje_columna]==5):

            self.mapa[self.personaje_fila][self.personaje_columna]=4
            self.mapa[self.personaje_fila][self.personaje_columna -1]=5
            self.personaje_columna -= 1
        #personaje_meta,caja,spacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 
              and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2
              and self.mapa[self.personaje_fila][self.personaje_columna - 2]== 1):
                  
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2
            self.personaje_columna -= 1    
        #personaje_meta,caja,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 
              and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2
              and self.mapa[self.personaje_fila][self.personaje_columna - 2]== 4):
                  
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1          
            #personaje_meta,caja_meta,espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 
              and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6
              and self.mapa[self.personaje_fila][self.personaje_columna - 2]== 1):
                  
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2
            self.personaje_columna -= 1  
           #personaje_meta,caja_meta,meta          
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 
              and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6
              and self.mapa[self.personaje_fila][self.personaje_columna - 2]== 4):
                  
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1   
    def moverarriba(self):  #movimientos ala derecha
        #personaje espacio
        if (self.mapa[self.personaje_fila -1 ][self.personaje_columna] == 1
        and self.mapa[self.personaje_fila ][self.personaje_columna]== 0):

            self.mapa[self.personaje_fila -1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.personaje_fila -= 1  
        #personaje,meta
        elif (self.mapa[self.personaje_fila -1][self.personaje_columna] == 4 
        and self.mapa[self.personaje_fila ][self.personaje_columna] == 0):

            self.mapa[self.personaje_fila -1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila ][self.personaje_columna] = 1
            self.personaje_fila -= 1
        #personaje_meta,espacio
        elif (self.mapa[self.personaje_fila -1][self.personaje_columna] == 1 
        and self.mapa[self.personaje_fila][self.personaje_columna ] == 5):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila -1][self.personaje_columna ] = 0
            self.personaje_fila -= 1
         #personaje,caja,espacio
        elif (self.mapa[self.personaje_fila-2][self.personaje_columna] == 1 
              and self.mapa[self.personaje_fila-1][self.personaje_columna ] == 2
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 0):

            self.mapa[self.personaje_fila-2][self.personaje_columna] = 2
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 1
            self.personaje_fila -= 1
        #meta,caja,personaje
        elif (self.mapa[self.personaje_fila-2][self.personaje_columna] == 4 
              and self.mapa[self.personaje_fila-1][self.personaje_columna ] == 2
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 0):

            self.mapa[self.personaje_fila-2][self.personaje_columna] = 6
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 1
            self.personaje_fila -= 1          

         #espacio,caja_meta,personaje
        elif (self.mapa[self.personaje_fila-2][self.personaje_columna] == 1 
              and self.mapa[self.personaje_fila-1][self.personaje_columna ] ==6 
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 0):

            self.mapa[self.personaje_fila-2][self.personaje_columna] = 2
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 1
            self.personaje_fila -= 1
        #meta,caja_meta,personaje
        elif (self.mapa[self.personaje_fila-2][self.personaje_columna] == 4 
              and self.mapa[self.personaje_fila-1][self.personaje_columna ] ==6 
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 0):

            self.mapa[self.personaje_fila-2][self.personaje_columna] = 6
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 1
            self.personaje_fila -= 1    
        #personaje_meta,meta
        elif (self.mapa[self.personaje_fila-1][self.personaje_columna] == 4 
         and self.mapa[self.personaje_fila][self.personaje_columna ] == 5):

            self.mapa[self.personaje_fila ][self.personaje_columna] = 4
            self.mapa[self.personaje_fila -1][self.personaje_columna ] = 5
            self.personaje_fila -= 1  
        #espacio,caja,personaje_meta
        elif (self.mapa[self.personaje_fila-2][self.personaje_columna] == 1 
              and self.mapa[self.personaje_fila-1][self.personaje_columna ] ==2 
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 5 ):

            self.mapa[self.personaje_fila-2][self.personaje_columna] = 2
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 4
            self.personaje_fila -= 1         
        #meta,caja,personaje_meta
        elif (self.mapa[self.personaje_fila-2][self.personaje_columna] == 4 
              and self.mapa[self.personaje_fila-1][self.personaje_columna ] == 2 
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 5 ):

            self.mapa[self.personaje_fila-2][self.personaje_columna] = 6
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 4
            self.personaje_fila -= 1  
        #espacio,caja_meta,personaje_meta          
        elif (self.mapa[self.personaje_fila-2][self.personaje_columna] == 1 
              and self.mapa[self.personaje_fila-1][self.personaje_columna ] == 6 
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 5 ):

            self.mapa[self.personaje_fila-2][self.personaje_columna] = 2
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 4
            self.personaje_fila -= 1     
        #meta,caja_meta,personaje_meta
        elif (self.mapa[self.personaje_fila-2][self.personaje_columna] == 4
              and self.mapa[self.personaje_fila-1][self.personaje_columna ] == 6 
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 5 ):

            self.mapa[self.personaje_fila -2][self.personaje_columna] = 6
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 4
            self.personaje_fila -= 1
    def moverabajo (self):
        #personaje espacio
        if (self.mapa[self.personaje_fila +1][self.personaje_columna] == 1
        and self.mapa[self.personaje_fila ][self.personaje_columna]== 0):

            self.mapa[self.personaje_fila +1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.personaje_fila += 1  
        #personaje,meta
        elif (self.mapa[self.personaje_fila +1][self.personaje_columna] == 4 
        and self.mapa[self.personaje_fila ][self.personaje_columna] == 0):

            self.mapa[self.personaje_fila +1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila ][self.personaje_columna] = 1
            self.personaje_fila += 1
        #personaje_meta,espacio
        elif (self.mapa[self.personaje_fila +1][self.personaje_columna] == 1 
        and self.mapa[self.personaje_fila][self.personaje_columna ] == 5):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila +1][self.personaje_columna ] = 0
            self.personaje_fila += 1
         #personaje,caja,espacio
        elif (self.mapa[self.personaje_fila +2][self.personaje_columna] == 1 
              and self.mapa[self.personaje_fila +1][self.personaje_columna ] == 2
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 0):

            self.mapa[self.personaje_fila +2][self.personaje_columna] = 2
            self.mapa[self.personaje_fila +1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 1
            self.personaje_fila += 1    


          


    def jugar(self):
        instrucciones = """
    a-izquierda
    d-derecha
    x-abajo
    w-arriba
    """
        print(instrucciones)
        self.leerMapa()
        while True:
            self.imprimirMapa()
            movimiento = input("mover hacia: ")
            if movimiento == "d":
                self.moverDerecha()
            elif movimiento == "a":
                self.moverIzquierda()
            elif movimiento == "w":
                self.moverarriba()
            elif movimiento == "x":
                self.moverabajo()
            elif movimiento == "f":
                print("saliste del juego")
                break


juego = sokoban()
juego.jugar()
