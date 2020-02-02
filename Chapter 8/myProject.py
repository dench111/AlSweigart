import os, re, myRegExpr


def searchAndReplaceFunc(searchexpression, newWord):
    openmyFile = open('myFile.txt', 'r+')
    readmyFile = openmyFile.read()
    myFileRegex = re.compile(searchexpression)
    openmyFile.write(myFileRegex.sub(newWord, readmyFile))
    openmyFile.close()


searchPattern = myRegExpr.myDict['findWord']
print('Ищем слово: ' + searchPattern)

replacePattern = myRegExpr.myDict['replaceOn']
print("Заменяем " + searchPattern + ' на ' + replacePattern)

searchAndReplaceFunc(searchPattern, replacePattern)
