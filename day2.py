__author__ = 'Walters954'

totalPaper = 0
dimensions = open("day2input.txt")

for line in dimensions:
    lwhArray = line.split('x')
    #print(lwhArray)
    lwhArray[2] = lwhArray[2].replace('\n','')
    #print(lwhArray)
    lwhArray = list(map(int,lwhArray))

    l = lwhArray[0]
    w = lwhArray[1]
    h = lwhArray[2]

    surfArea = (2*l*w + 2*w*h + 2*h*l)
    #print(surfArea)
    lwhArray.sort()
    #print(lwhArray)
    smallArea = lwhArray[0] * lwhArray[1]
    #print(smallArea)
    totalPaper += smallArea + surfArea
print(totalPaper)
print('1586300')
dimensions.close()



