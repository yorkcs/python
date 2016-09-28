# INF 120-004
# Project 2
# Casey York
# September 27, 2016

from random import *
def main():
  
  # making a random color
  showInformation("I will now create a randomly colored window.")
  redRandom = randrange(0, 256)
  greenRandom = randrange(0, 256)
  blueRandom = randrange(0, 256)
  randomColor = makeColor(redRandom, greenRandom, blueRandom)
  
  # creating a picture using random color, displaying picture
  randomPicture = makeEmptyPicture(300, 150, randomColor)
  show(randomPicture)
  
  # asking user to guess random color
  showInformation("Can you guess the RGB values of this random color?")
  redGuess = requestInteger("Guess the red value.")
  greenGuess = requestInteger("Guess the green value.")
  blueGuess = requestInteger("Guess the blue value.")
    
  # making a color from user guess, showing on screen
  userGuess = makeColor(redGuess, greenGuess, blueGuess)
  addRectFilled(randomPicture, 150, 0, 150, 150, userGuess)
  
  # calculating distance between two colors
  colorOff = distance(randomColor, userGuess)
  colorDistance = (colorOff / 766) * 100
  
  # displaying message for correct/incorrect guesses
  if colorDistance != 100:
    textStyle = makeStyle(sansSerif, bold, 16)
    addTextWithStyle(randomPicture, 5, 80, "Off by " + str(colorDistance) + "%", textStyle)
  else:
    textStyle = makeStyle(sansSerif, bold, 16)
    addTextWithStyle(randomPicture, 5, 80, "You guessed correctly!", textStyle)
  repaint(randomPicture)