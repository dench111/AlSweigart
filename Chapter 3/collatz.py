print('Введите number')
number = input()


def IsInt(number):
    try:
        return int(
            number)  # Если число в формате str можно преобразовать к int, оно целое. Проверяем и одновременно преобразуем
    except ValueError:
        print('Введите целое число!')


while not IsInt(number):  # Если IsInt(number) не True (число не целое),то повторить ввод числа
    number = input()


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


collatzresult = collatz(IsInt(number))  # Сохраняем в переменную результат выполнения функции collatz
print(collatzresult)

while collatzresult != 1:
    number = collatzresult
    collatzresult = collatz(IsInt(number))
    print(collatzresult)
