# Casey York
# INF120-004
# Project 4
# 10-27-16

from random import *
from time import sleep

def turtleRace():
  # creating turtle world
  backgroundImage = makePicture(pickAFile())
  width = getWidth(backgroundImage)
  height = getHeight(backgroundImage)
  turtleWorld = makeWorld(width, height)
  turtleWorld.setPicture(backgroundImage)
  
  # adding turtles, putting in position at start line
  lazyTurtle = makeTurtle(turtleWorld)
  steadyTurtle = makeTurtle(turtleWorld)
  penUp(lazyTurtle)
  moveTo(lazyTurtle, 0, height / 3)
  turnRight(lazyTurtle)
  penDown(lazyTurtle)
  penUp(steadyTurtle)
  moveTo(steadyTurtle, 0, height / 3 * 2)
  turnRight(steadyTurtle)
  penDown(steadyTurtle)
  
  # setting finish line and positions
  finishLine = width - 10
  lazyTurtlePos = 0
  steadyTurtlePos = 0
  
  # moving turtles forward
  while lazyTurtlePos <= finishLine and steadyTurtlePos <= finishLine: 
    forward(steadyTurtle, randrange(1, 4))         
    nap = randrange(1, 3)
    if nap == 1:
      forward(lazyTurtle, randrange(1, 9)) 
    lazyTurtlePos = getXPos(lazyTurtle)
    steadyTurtlePos = getXPos(steadyTurtle)
    sleep(0.125)
    
  # showing winning message
  if lazyTurtlePos > steadyTurtlePos:
    showInformation("The lazy turtle won!")
  elif steadyTurtlePos > lazyTurtlePos:
    showInformation("Slow and steady wins the race!")
  else:
    showInformation("It's a tie!")