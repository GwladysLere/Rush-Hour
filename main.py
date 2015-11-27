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
from grid import *
import json
# ------------------------------------------------------------------------------
def error_msg(code):
#methode d'affichage des messages d'erreur
  if code == "outofstreet":
    print("Il faut rester sur la route !")
  elif code == "occupied":
    print("Deja une voiture ici !")
  elif code == "wrongdir":
    print("Cette voiture ne peut pas rouler lateralement")

def parser(grid):
  
  command = input("Enter move : ")
  carName = command[0]
  direc = command[1]
  car = grid.cars[carName]
  result = grid.move(car, direc)
  error_msg(result)
  
  return result == "win"
  #retourne vrai si result vaut "win"


def main():
  
  gdicts = json.load(open('grilles.json'))

  num = input("rentrez le numéro de la grille sur laquelle vous souhaitez jouer (de 1 à 41)")
  
  gdict = gdicts[num]
  gameGrid = Grid(gdict)
  
  trials = 0              #trials iterator
  while(True):
    print(grid(gameGrid.toArray(), size=3))
    if parser(gameGrid):      #parser renvoie faux tant que la voiture Z n'es pas sortie
      break               #du coup si il renvoie vrai, c'est qu'on a gagné, donc on sort de la boucle
    trials +=1            #à chaque tour de boucle, un essai supplémentaire
        
  print("WINNER !! \nNombre de coups :", trials) 
    

    
#ToDo :
   
    #- fonction UI chargement des grilles (diviser en deux fonctions) 
    #faire des tests sur les entrées de l'utilisateur

# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
