class sokoban:
 #Componentes del juego:
 #0-personaje
 #1-Espacio
 #2-cajas
 #3-Paredes
 #4-Metas
 #5 personaje_meta
 #6 caja meta
  #controles:
  #a-Izquierda
  #d-Derecha
  #w-arriba
  #s-abajo 

  mapa = []
  
  personaje_fila = 0
  personaje_columna = 0
  
  def __init__(self):
      pass
  def leerMapa(self):
    
       self.mapa = [
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
            [3,1,1,1,1,1,1,1,1,3,3,3,3,3,3],
            [3,1,1,1,1,1,1,1,1,1,1,3,3,4,3],
            [3,0,4,1,1,2,1,1,1,1,1,2,1,1,3],
            [3,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
            [3,3,3,3,3,3,3,1,3,3,3,3,3,3,3],
            [3,3,3,3,3,3,3,1,3,3,3,3,3,3,3],
            [3,3,3,3,3,3,3,1,3,3,3,3,3,3,3],
            [3,3,3,3,3,3,3,1,3,3,3,3,3,3,3],
       ]
       self.personaje_fila = 3
       self.personaje_columna = 1
      
    
  def imprimirMapa(self):
     for fila in self.mapa:
       print(fila)  
  def moverDerecha(self):  #personaje espacio
     if (self.mapa[self.personaje_fila][self.personaje_columna] == 0
     and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1):
     
         self.mapa[self.personaje_fila][self.personaje_columna] = 1
         self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
         self.personaje_columna += 1
      #personaje meta  
     elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 
     and self.mapa[self.personaje_fila][self.personaje_columna +1] == 4):
        
         self.mapa[self.personaje_fila][self.personaje_columna] = 1
         self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
         self.personaje_columna += 1
      #personaje_meta,espacio
     elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 
     and self.mapa[self.personaje_fila][self.personaje_columna +1] == 1):
         
          self.mapa[self.personaje_fila][self.personaje_columna] = 4
          self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
          self.personaje_columna += 1
        
      #personaje,caja,espacio
     elif(self.mapa[self.personaje_fila][self.personaje_columna] == 0
     and self.mapa[self.personaje_fila][self.personaje_columna +1 ] == 2
     and self.mapa[self.personaje_fila][self.personaje_columna +2] == 1):    
         
     
         self.mapa[self.personaje_fila][self.personaje_columna] = 1
         self.mapa[self.personaje_fila][self.personaje_columna+1] = 0
         self.mapa[self.personaje_fila][self.personaje_columna+2] = 2
         self.personaje_columna += 1
         
  def jugar (self):
    instrucciones="""
    a-izquierda
    d-derecha
    x-abajo
    w-arriba
    """
    print(instrucciones)
    self.leerMapa()
    while True:
        self.imprimirMapa()
        movimiento= input("mover hacia: ")
        if movimiento == "d":
         self.moverDerecha()   
        elif movimiento== "f":
          print("saliste del juego")
          break

juego=sokoban()
juego.jugar()

    

