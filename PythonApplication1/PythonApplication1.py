import os
import os.path

def findHeadFile(pathList):
    result = {}
    for path in pathList:
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith('.h'):
                    fullName = root + '/' + name
                    result[fullName] = [name, findAString(fullName)]
    return result

def findAString(fullName):
    fileObject = open(fullName, 'r')
    count = 0
    while count < 100:
        aline = fileObject.readline(count)
        if aline.startswith('#ifndef'):
            splitResult = aline.split(' ')
            fileObject.close()
            return splitResult[1]
        count += 1
    return ''

def writeFile(dicts):
    for fullName, valuePair in dicts.iteritems():
        fileObject = open(fullName, 'r')
        allLines = fileObject.readlines()
        allwriteLines = []
        curLineIndex = -1
        for aline in allLines:
            curLineIndex += 1
            if not aline.startswith('#include'):
                allwriteLines.append(aline)
            else:
                if not allLines[curLineIndex - 1].startswith('#ifndef'):
                    allwriteLines.append('#ifndef ' + valuePair[1])
                    allwriteLines.append(aline)
                    allwriteLines.append('#endif')
                else:
                    allwriteLines.append(aline)
        fileObject.close()
        fileObject = open(fullName, 'w')
        fileObject.writelines(allwriteLines)
        fileObject.close()


            

        

