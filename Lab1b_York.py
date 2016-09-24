def createAPicture():

  #Gathering info from user
  fname = requestString("What is your first name?")
  myColor = pickAColor()
  side = requestInteger("How many pixels will be on the side of the picture?")

  #Making a picture with gathered info
  userPic = makeEmptyPicture(side, side, myColor)
  printNow("Hello, " + fname + ". Your colored picture is displayed on the screen!")
  show(userPic)