__author__ = 'Walters954'

totalPaper = 0

dim = open('day2input')
#print(dim)

for line in dim:
    #print(line)
    lwhList = line.split('x')
    #print(lwhList)
    lwhList[2] = lwhList[2].replace('\n','')
    #print(lwhList)
    lwhList = list(map(int,lwhList))

    l = lwhList[0]
    w = lwhList[1]
    h = lwhList[2]

    surfArea = 2*l*w + 2*w*h + 2*h*l
    lwhList.sort()
    #print(lwhList)
    smallArea = lwhList[0] * lwhList[1]
    totalPaper += smallArea + surfArea

print(totalPaper)
dim.close()

################### Part 2 ########################
totalPaper = 0
dim2 = open('day2input')
for line in dim2:
    lwhList = line.split('x')
    lwhList[2] = lwhList[2].replace('\n','')
    lwhList = list(map(int,lwhList))
    lwhList.sort()
    #print(lwhList)

    l = lwhList[0]
    w = lwhList[1]
    h = lwhList[2]

    calcBow = l * w * h
    calcRib = 2 * min(l+w, w+h, h+l) # same as lwhArray[0] * 2 + lwhArray[1] *2

    totalPaper += calcBow + calcRib
print(totalPaper)

dim2.close()