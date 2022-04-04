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
  personaje = 0
  espacio = 1
  caja = 2
  pared = 3
  meta = 4
  personaje_meta = 5
  caja_meta = 6
  
  mapa = []
  
  personaje_fila=0
  personaje_columna=0
  
    #def __init__(self):
     #pass
  def leerMapa(self):
      self.mapa = [
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
            [3,1,1,1,1,1,1,1,1,3,3,3,3,3,3],
            [3,1,1,1,1,1,1,0,1,1,1,3,3,4,3],
            [3,1,1,1,1,1,1,1,1,1,1,1,1,2,3],
            [3,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
            [3,3,3,3,3,3,3,1,3,3,3,3,3,3,3],
       ]
      self.personaje_columna=7
      self.personaje_fila=2
    
  def imprimirMapa(self):
     for fila in self.mapa:
       print(fila)
  def mover_derecha(self):
      print("Mover derecha")
    #personaje espacio
      if (self.mapa[self.personaje_fila][self.personaje_columna]== self.personaje 
      and self.mapa[self.personaje_fila][self.personaje_columna +1]==self.espacio):
     
          self.mapa[self.personaje_fila][self.personaje_columna]==self.espacio
          self.mapa[self.personaje_fila][self.personaje_columna +1]== self.personaje
          self.mapa[self.personaje_fila][self.personaje_columna]=0
          self.personaje_columna+=1
      #Muñeco meta  
      #elif (self.mapa[self.personaje_fila][self.personaje_columna]== 0 
      #and self.mapa[self.personaje_fila][self.personaje_columna +1]==4):
          #self.mapa[self.personaje_fila][self.personaje_columna]=1
          #self.mapa[self.personaje_fila][self.personaje_columna]=5
          #self.personaje_columna+=1
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
         self.mover_derecha()
        elif movimiento=="f":
          print("saliste del juego")
          break

juego=sokoban()
juego.jugar()

    

