tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(items):
    col = ''
    col0 = ''
    col1 = ''
    col2 = ''
    col3 = ''
    for i in range(len(items[0])):
        for j in range(len(items)):
            col = col + items[j][i] + ' '
    print(col)
    col = col.split()
    print(col)
    for i in col[0:3]:
        col0 = col0 + i + ' '
    print(col0, len(col0))
    for i in col[3:6]:
        col1 = col1 + i + ' '
    print(col1, len(col1))
    for i in col[6:9]:
        col2 = col2 + i + ' '
    print(col2, len(col2))
    for i in col[9:12]:
        col3 = col3 + i + ' '
    print(col3, len(col3))
    print()
    print(col0.rjust(21, '*'))
    print(col1.rjust(21, '*'))
    print(col2.rjust(21, '*'))
    print(col3.rjust(21, '*'))
printTable(tableData)