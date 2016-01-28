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
