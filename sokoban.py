class Sokoban:
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
  personaje=0
  espacio=1
  caja=2
  pared=3
  meta=4
  personaje_meta=5
  caja_meta=6
  
  mapa=[]
  
  personaje_fila=0
  personaje_columna=0
  
  def __init__(self):
   pass
  def leerMapa(self):
      self.mapa[
          [1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    
      ]
      self.personaje_columna=1
      self.personaje_fila=1
  def imprimirmapa(self):
     for fila in self.mapa:
       print(fila)
  def moverderecha(self):
      print("Movder deecha")
    #muñeco espacio
      if (self.mapa[self.personaje_fila][self.personaje_columna]== 0 
      and self.mapa[self.personaje_fila][self.personaje_columna +1]==0):
          self.mapa[self.personaje_fila][self.personaje_columna]=1
          self.mapa[self.personaje_fila][self.personaje_columna]=0
          self.personaje_columna+=1
      #Muñeco meta  
      elif (self.mapa[self.personaje_fila][self.personaje_columna]== 0 
      and self.mapa[self.personaje_fila][self.personaje_columna +1]==4):
          self.mapa[self.personaje_fila][self.personaje_columna]=1
          self.mapa[self.personaje_fila][self.personaje_columna]=5
          self.personaje_columna+=1
  def jugar (self):
    instrcciones="a-izquierda...."
    print(instrcciones)
    self.leerMapa
    while true:
      self.imprimirmapa
      movimiento= input("a")
      if movimiento == "d":
      elif movimiento=="f":
        print("saliste del juego")
        

    

