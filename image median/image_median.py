from PIL import Image
import statistics
import time

startTime = time.time()*1000.0
im = []
for i in range(1,10):
    im.append(Image.open(str(i)+".png"))

size = im[0].size
width, height = im[0].size





pixel_values = []
for i in range(0,9):
    pixel_values.append(list(im[i].getdata()))
pixels = []
newImagePixels =[]
for x in range(0,len(pixel_values[0])-1):
    for i in range (0,9):
        pixels.append(pixel_values[i][x])
    pixels.sort()
    newImagePixels.append(statistics.median(pixels))
    del pixels[:]

myimage10 = Image.new(im[0].mode,im[0].size);
myimage10.putdata(newImagePixels)
finalTime = time.time() * 1000.0

print(str(finalTime-startTime))
myimage10.save("10.png","PNG")