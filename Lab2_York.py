from random import *
def main():

  # Creating picture
  width = randrange(200, 301)
  height = randrange(200, 301)
  pic = makeEmptyPicture(width, height)
  show(pic)
  showInformation("The picture\'s width is " + str(width) + ".\nThe picture\'s height is " + str(height) + ".")

  #Repainting picture to user selected color
  userColor = pickAColor()
  setAllPixelsToAColor(pic, userColor)
  repaint(pic)

  #Adding shapes to picture
  addRectFilled(pic, 0, 0, 60, 60, white)
  addRectFilled(pic, width-60, height-60, 60, 60, white)
  addOvalFilled(pic, (width-60)/2, (height-60)/2, 60, 60, yellow)
  repaint(pic)