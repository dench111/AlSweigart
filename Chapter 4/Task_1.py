spam = []
while True:
    print('enter object #' + str(len(spam) + 1) + '(or nothing to stop.):')
    object = input()
    if object == '':
        break
    spam = spam + [object]
print(spam)

def MyFunc(spam):
    spam[-1] = 'and ' + spam[-1]
    for i in range(len(spam) - 1):
        print(spam[i] + ', ', end="")
    print(spam[-1])

MyFunc(spam)
