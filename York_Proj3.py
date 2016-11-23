# INF120-004
# Casey York
# Oct 11, 2016

from random import *

def spaceInvader():

  # setting a background for the alien invaders
  showInformation("Select a photo to send your alien invaders.")
  path = pickAFile()
  invasionPic = makePicture(path)
  show(invasionPic)
  
  # setting ship placement parameters
  width = getWidth(invasionPic)
  height = getHeight(invasionPic)
  quadrant = randrange(1, 5)
  
  # getting user guess on ship location
  userGuess = requestString("Are the aliens hidden in the upper space (U) or lower space (L)?")
  
  # adding spaceship to pic
  if quadrant == 1:
    drawSpaceship(invasionPic, width / 4, height / 4)
  elif quadrant == 2:
    drawSpaceship(invasionPic, width / 4 * 3, height / 4)
  elif quadrant == 3:
    drawSpaceship(invasionPic, width / 4, height / 4 * 3)
  else:
    drawSpaceship(invasionPic, width / 4 * 3, height / 4)
    
  # comparing user guess to random quadrant
  if (userGuess == "U" or userGuess == "u") and (quadrant == 1 or quadrant == 2):
    showInformation("Correct!")
  elif (userGuess == "L" or userGuess == "l") and (quadrant == 3 or quadrant == 4):
    showInformation("Correct!")    
  else:
    showInformation("Wrong!")
  repaint(invasionPic)  
  
def drawSpaceship(pic, xc, yc):
  w = 100
  h = 100
  addOvalFilled(pic, xc - 20, yc + h/6 , 40, 20, red)
  addOvalFilled(pic, xc - 30, yc, 60, 30, white)
  addOval(pic, xc - 30, yc , 60, 30, black)
  addOvalFilled(pic, xc - 50, yc - 14, 100, 36, white)
  addOval(pic, xc - 50, yc - 14, 100, 36, black)
  addOvalFilled(pic, xc - 50, yc -16 , 100, 30, white)
  addOval(pic, xc - 50, yc -16, 100, 30, black)
  addOval(pic, xc - 30, yc -6, 60, 10, black)
  addOvalFilled(pic, xc - 45, yc - 3, 10, 5, red)
  addOvalFilled(pic, xc + 35, yc - 3, 10, 5, red)
  addOvalFilled(pic, xc - 5 , yc + 6, 10, 5, red)
  addArc(pic, xc - 30, yc - h/2 , 60, 100, 0, 180, green)