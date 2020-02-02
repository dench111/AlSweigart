import random

messages = ['It is certain','It is decidely so','Yes definitely','Reply hazy try again',
            'Ask again later','Concentrate and ask again','My reply is no','Outlook not so good',
            'Very doubtful']

print(len(messages))
print(type(len(messages)))
for i in range(len(messages)):
    print(type(i))
    print('Element ' + str(i) + ' is ' + messages[i])
print(messages[random.randint(0,len(messages) - 1)])