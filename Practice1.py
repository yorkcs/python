from random import *
def main():
  # making pink picture
  width = randrange(200, 301)
  height = randrange(200, 301)
  pinkSquare = makeEmptyPicture(width, height, pink)
  show(pinkSquare)
  
  # requesting mood from user
  happySad = requestString("Are you happy or sad?")
  
  # drawing face based on input
  addLine(pinkSquare, width / 3, 0, width / 3, height, black)
  addLine(pinkSquare, width / 3 * 2, 0, width / 3 * 2, height, black)
  addLine(pinkSquare, 0, height / 3, width, height / 3, black)
  addLine(pinkSquare, 0, height / 3 * 2, width, height / 3 * 2, black)
  repaint(pinkSquare)
  addOvalFilled(pinkSquare, (width-45) / 3, (height-45) / 3, 30, 30, blue)
  addOvalFilled(pinkSquare, width - (width / 3) - 15, (height - 45) / 3, 30, 30, blue)
  if happySad == "happy":
    addLine(pinkSquare, width / 3, height / 3 * 2, width / 2, (height / 3 * 2) + 20, red)
    addLine(pinkSquare, width / 2, (height / 3 * 2) + 20, width / 3 * 2, height / 3 * 2, red)
  elif happySad == "sad":
    addLine(pinkSquare, width / 3, height / 3 * 2 + 20, width / 2, (height / 3 * 2), red)
    addLine(pinkSquare, width / 2, (height / 3 * 2), width / 3 * 2, height / 3 * 2 + 20, red)
  else:
    showInformation("Please choose 'happy' or 'sad'.")
  repaint(pinkSquare)
