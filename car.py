# ==============================================================================
"""BINO : compute the binomial coefficient C(n,p)"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # use 'for' loop to generate string
__date__    = "2015-09-01"
__usage__   = """
User input: <n>, <p> (where n:int > 0, p:int >=0)
App output: binomial coefficient C(n,p)"""
# ==============================================================================
from ezCLI import *
# ------------------------------------------------------------------------------
class Car:
  
  def __init__(self, dic, name):
    self.name = name
    #normalement c'est self.x = int(dic["x"]) mais x et y inversés dans fichier json donc à changer 
    self.x = int(dic["y"])
    self.y = int(dic["x"])
    
    if dic["direction"] == "v" :
      self.vertical = True
      self.height = int(dic["size"])
      self.width = 1
    else:
      self.vertical = False
      self.width = int(dic["size"])
      self.height = 1

  def canMove(self, direction):
    if self.vertical:
      return (direction == "U" or direction == "D")
    else :
      return (direction == "L" or direction == "R")

  def crashes(self, car):
    #compare les différents cas où on est sûr que les voitures ne se toucheront pas
    if car.x + car.width <= self.x or \
       car.x >= self.x + self.width or \
       car.y + car.height <= self.y or \
       car.y >= self.y + self.height :
         return False    # retourne faux s'il n'y a pas de crash donc si les voitures ne se touchent pas
    else:
      return True #retourne vrai s'il y a un crash

  def movement(self, direction, back = False):  #back à une valeur par défaut de false, si on le passe pas en param ce sera false
    """effectue le mouvement de la voiture ou inverse le mouvement si back = true, pour rétablir la grille si le mouvement demandé est impossible """
    movement = {"U" : [0,-1],
                "D" : [0, 1],
                "L" : [-1,0],
                "R" : [1,0] }
    if back:
      self.x -= movement[direction][0]
      self.y -= movement[direction][1]
    else:
      self.x += movement[direction][0]
      self.y += movement[direction][1]

# ------------------------------------------------------------------------------

# ==============================================================================

# ==============================================================================
