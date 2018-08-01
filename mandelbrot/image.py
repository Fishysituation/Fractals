from PIL import Image

#load in data
size = 10000    

filein = 'm' + str(size) + 'n.out'
fileout = "mb" + str(size) + ".bmp"

f = open(filein, 'r')

data = f.readlines()

# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.new( 'RGB', (size, size), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every col:
    for j in range(img.size[1]):    # For every row
        if data[j][i] == '*':
            pixels[i,j] = (255, 255, 255) # set the colour accordingly



img.show()
img.save(fileout)

