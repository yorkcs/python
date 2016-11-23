# INF 120-004
# Project 5
# Casey York
# November 15, 2016

from time import sleep

def flipbook():
  
  # setting folder path for pictures, making empty list to contain files
  path = setMediaPath()
  frameList = []
  
  # requesting info for building file path
  fileNum1 = requestIntegerInRange("Frame numbering begins at:", 1, 15)
  fileNum2 = requestIntegerInRange("Frame numbering ends at:", 1, 15)
  extension = requestString("Enter the file extension (ex: jpg, png)")
  
  # setting loop count
  count = 0
  countRequest = requestInteger("How many times should the animation run?")
  
  # adding frames to list
  for frame in range(fileNum1, fileNum2 + 1):
    shot = makePicture(path + "frame" + str(frame) + "." + extension)
    frameList += [shot]
    
  # making empty frame for copying
  pic = makeEmptyPicture(getWidth(shot), getHeight(shot))
  show(pic)
  
  # copying frames to empty picture while count is below user input
  while count <= countRequest:
    for still in frameList:
      copyInto(still, pic, 0, 0)
      repaint(pic)
      sleep(0.01)
    count += 1