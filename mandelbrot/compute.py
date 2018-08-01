import math

startx = -2
starty = 1.3

endx = 0.6
endy = -1.3

logicalw = 10000
difference = 2.6/logicalw

grid = []

pathout = 'm10000n.out'


def generate():
    for y in range(0, logicalw):
        line = []
        for x in range(0, logicalw):
            line.append('.')
        grid.append(line)


def draw():
    for y in range(0, logicalw):
        for x in range(0, logicalw):
            print(' ' + grid[y][x], end = '')
        print()

def writeout():
    f = open(pathout, 'w')

    for y in range(0, logicalw):
        strout = ''
        for x in range(0, logicalw):
            strout += grid[y][x]
        f.write(strout + '\n')

###
#for all the following complex number functions, cnum is a tuple of x, (i)y

#add two complex numbers
def add(cnum1, cnum2):
    return (cnum1[0]+cnum2[0], cnum1[1]+cnum2[1])

#get square of complex number
def square(cnum):
    #(x + iy)^2 = x^2 - y^2 + 2ixy
    return (math.pow(cnum[0], 2) - math.pow(cnum[1], 2), 2 * cnum[0] * cnum[1])

#compute modulus of complex number
def modulus(cnum):
    return math.pow(math.pow(cnum[0], 2) + math.pow(cnum[1], 2), 0.5)

#see if item is in m-set, return bool
def compute(cnum):
    #iterate set number of times, if passes, return true else break
    go = True
    x = (0, 0)
    for i in range(0, 50):
        result = add(square(x), cnum)
        if modulus(result) > 2:
            go = False
            break
        else:
            x = result
    return go


def main():
    #create the grid
    generate()

    #compute the result for each element
    for y in range(0, logicalw):
        for x in range(0, logicalw):
            actualx = startx + difference * x
            actualy = starty - difference * y
            #print(str(actualx) + ', i' + str(actualy))
            #if member of m-set
            if compute((actualx, actualy)):
                #change grid val
                grid[y][x] = '*'
    
    #display to console
    #draw()

    #draw the grid out to file 
    writeout()


main()

