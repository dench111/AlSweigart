import os, shelve
dir = os.getcwd()
print(dir)
hellofile = open('C:\\scripts\\python\\ElSveugart\\Chapter 8\\hellofile.txt')
hellocontent = hellofile.read()
print(hellocontent)

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()