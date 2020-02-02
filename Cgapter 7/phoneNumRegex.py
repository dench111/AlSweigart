# Регулярное выражение, которому соответствуют числа с запятой в качестве разделителя между каждыми тремя цифрами
import re

expression = (r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.')
searchRegex = re.compile(expression, re.IGNORECASE)
mo = searchRegex.search('Alice eats apples. Bob pets cats. Carol throws baseballs. Alice throws Apples. BOB EATS CATS.'
                        'Robocop eats apples. ALICE THROWS FOOTBALLS. Carol eats 7 cats')
try:
    print('Результат методом search: ')
    print(mo.groups())
except AttributeError:
    print('Error: mo.group пуста')

findallRegex = re.compile(expression, re.IGNORECASE)
print('Результат методом findall:')
print(findallRegex.findall('Alice eats apples. Bob pets cats. Carol throws baseballs. Alice throws Apples. BOB EATS CATS.'
                        'Robocop eats apples. ALICE THROWS FOOTBALLS. Carol eats 7 cats'))
