def main():

  # Creating picture
  picPath = pickAFile()
  pic = makePicture(picPath)

  # Gathering info on picture
  height = getHeight(pic)
  width = getWidth(pic)
  midPixel = getPixel(pic, height/2, width/2)
  redChannel = getRed(midPixel)
  blueChannel = getBlue(midPixel)
  greenChannel = getGreen(midPixel)
  pixelColor = makeColor(redChannel, blueChannel, greenChannel)
  intensity = (redChannel + blueChannel + greenChannel) / 3

  # Creating "zoom" effect by recoloring pixels the color of the center pixel
  addRectFilled(pic, (width-60)/2, (height-60)/2, 60, 60, pixelColor)
  show(pic)

  # Adding intensity message
  if intensity <= 127:
    addText(pic, width/2 - 12, height/2 + 5, "low", white)
  elif intensity >= 128:
    addText(pic, width/2 - 15, height/2 + 5, "high", black)
  repaint(pic)