from PIL import Image
from statistics import median


im = []
for i in range(1,10):
    im.append(Image.open(i+".png"))
# loop through all the pixles and gather the median for each pixle
temp = []
final
newimage = Image()
for i in range (im[0].size()[0]):
    for j in range (im[0].size()[1]):
        for i in range (0,9):
            temp.append(im.getpixel(i,j))
        final = median(temp)
        #sort the pixles and find the median
        temp.
        #store the median into the newimage
        #delete all the data in temp

#save newimage to 
