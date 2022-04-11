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
            [3, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 3],
            [3, 3, 1, 1, 3, 3, 1, 6, 4, 3, 1, 1, 1, 3, 3],
            [3, 3, 1, 1, 1, 1, 1, 4, 6, 1, 1, 1, 1, 1, 3],
            [3, 3, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        ]
        self.personaje_fila = 6#define la pocicion del personaje en fila
        self.personaje_columna = 7#define la posicion del personaje en columnna   
    def imprimirMapa(self):#metodo para imprimir mapa
        for fila in self.mapa: 
             print(fila)    
    def moverDerecha(self):  #movimientos ala derecha
        #personaje espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0
                and self.mapa[self.personaje_fila][self.personaje_columna + 1]== 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.personaje_columna += 1
        #personaje,meta
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
        #Personaje,caja,meta
        elif (self.mapa[self.personaje_fila+2][self.personaje_columna] == 4 
              and self.mapa[self.personaje_fila+1][self.personaje_columna ] == 2
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 0):

            self.mapa[self.personaje_fila+2][self.personaje_columna] = 6
            self.mapa[self.personaje_fila+1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 1
            self.personaje_fila += 1          

         #personaje,caja_meta,espacio
        elif (self.mapa[self.personaje_fila +2][self.personaje_columna] == 1 
              and self.mapa[self.personaje_fila+1][self.personaje_columna ] ==6 
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 0):

            self.mapa[self.personaje_fila+2][self.personaje_columna] = 2
            self.mapa[self.personaje_fila+1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 1
            self.personaje_fila += 1
        #personaje,caja_meta,meta
        elif (self.mapa[self.personaje_fila +2][self.personaje_columna] == 4 
              and self.mapa[self.personaje_fila +1][self.personaje_columna ] ==6 
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 0):

            self.mapa[self.personaje_fila +2][self.personaje_columna] = 6
            self.mapa[self.personaje_fila +1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 1
            self.personaje_fila += 1    
        #personaje_meta,meta
        elif (self.mapa[self.personaje_fila +1][self.personaje_columna] == 4 
         and self.mapa[self.personaje_fila][self.personaje_columna ] == 5):

            self.mapa[self.personaje_fila ][self.personaje_columna] = 4
            self.mapa[self.personaje_fila +1][self.personaje_columna ] = 5
            self.personaje_fila += 1  
        #personaje_meta,caja,espacio
        elif (self.mapa[self.personaje_fila+2][self.personaje_columna] == 1 
              and self.mapa[self.personaje_fila +1][self.personaje_columna ] ==2 
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 5 ):

            self.mapa[self.personaje_fila +2][self.personaje_columna] = 2
            self.mapa[self.personaje_fila +1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 4
            self.personaje_fila += 1         
        #personaje_meta,caja,meta
        elif (self.mapa[self.personaje_fila +2][self.personaje_columna] == 4 
              and self.mapa[self.personaje_fila +1][self.personaje_columna ] == 2 
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 5 ):

            self.mapa[self.personaje_fila +2][self.personaje_columna] = 6
            self.mapa[self.personaje_fila +1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 4
            self.personaje_fila += 1  
       #personaje_meta,caja_meta,espacio          
        elif (self.mapa[self.personaje_fila+2][self.personaje_columna] == 1 
              and self.mapa[self.personaje_fila+1][self.personaje_columna ] == 6 
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 5 ):

            self.mapa[self.personaje_fila+2][self.personaje_columna] = 2
            self.mapa[self.personaje_fila+1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 4
            self.personaje_fila += 1     
        #personaje_meta,caja_meta,meta
        elif (self.mapa[self.personaje_fila +2][self.personaje_columna] == 4
              and self.mapa[self.personaje_fila +1][self.personaje_columna ] == 6 
              and self.mapa[self.personaje_fila][self.personaje_columna ] == 5 ):

            self.mapa[self.personaje_fila +2][self.personaje_columna] = 6
            self.mapa[self.personaje_fila +1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila ][self.personaje_columna ] = 4
            self.personaje_fila += 1

          


    def jugar(self):#Variable para definir los controles del juego
        instrucciones = """ 
    a-izquierda
    d-derecha
    x-abajo
    w-arriba
    """
        print(instrucciones)#imprimimos las instrucciones 
        self.leerMapa()
        while True:#bucle para jugar varias veces
            self.imprimirMapa()#imprime el mapa
            movimiento = input("mover hacia: ") #el movimiento es igual a un caracter ingresado por el ususario
            if movimiento == "d" or movimiento =="D": #tecla "d" minuscula o mayuscula mueve al personaje ala derecha
                self.moverDerecha()#llamamos al metodo "mover ala derecha"
            elif movimiento == "a" or movimiento =="A":#tecla "a" minuscula o mayuscula mueve al personaje ala izquierda
                self.moverIzquierda()#llama al metodo "mover ala izquierda"
            elif movimiento == "w" or movimiento=="W":#tecla "w" minuscula o mayuscula mueve personaje asia arriba
                self.moverarriba()#llamamos al metodo  mover asia arriba
            elif movimiento == "x" or movimiento=="X":#tecla "x" mayuscula o minuscula mueve el personaje asia abajo
                self.moverabajo()#llamamos al metodo mover asia abajo      
            elif movimiento == "f" or movimiento== "F":#Tecla para detener el juego
                print("saliste del juego")#imprime el mensaje de salida
                break#detiene el bucle


juego = sokoban()
juego.jugar()
