class  sokoban:
  mapa=[]
  personaje_fila = 0
  personaje_columna =0
  def __init__(self): 
   pass
  def leerMapa(self):
      self.mapa =[
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,1,1,1,1,1,1,1,1,3,3,3,3,3,3],
          [3,1,1,1,1,1,1,0,1,1,1,3,3,4,3],
          [3,1,1,1,1,1,1,1,1,1,1,1,1,2,3],
          [3,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
          [3,3,3,3,3,3,3,1,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,1,3,3,3,3,3,3,3],
      ]
      self.personaje_fila = 2
      self.personaje_columna = 7
  def imprimeMapa(self):
    for fila in self.mapa:
      print(fila)
  def mover_derecha(self):
    print("Mover derecha") 
      