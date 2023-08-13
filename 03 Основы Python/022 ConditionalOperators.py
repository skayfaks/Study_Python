# Условные операторы if elif else
# нужны для выполнения кода на основе результата какого-то Булин выражения

x = int(input())
if x>3:
    print('x>3')
elif x<3:
    print('x<3')
else:
    print('x=3')


# Можно использовать несколько elif
day_time='2'

if day_time == 'morning':
    print('Monster wakes up')
elif day_time == 'afternoon':
    print('Monster is walking')
elif day_time == 'evening':
    print('Monster is eating')
elif day_time == 'night':
    print('Monster is sleaping')
else:
    print("Monster is doing something")
# Monster is walking

# Если мы знаем, что есть всего 2 варианта. То можно использовать только if и else
# Если х --вычислить остаток от деления на 2-- равен 0 то (число четное even или не четное odd)
x=6
y = int(input("Введите на что делим, для проверки четности введите (2) "))
if x % y == 0:
    print('x is (четное) even')
else:
    print('x is (не четное) odd')

# !! МОЖНО ПОМЕСТИТЬ ТОЛЬКО ОДНО Else !! 

if 0:
    print('something')
#значение 0 - это всегда False
if "":
    print('something')
# если вместо значение пустой  пробел  - это всегда False
if None:
    print('something')
# если None  - это всегда False
if 1:
    print('something')
# something


lucky_number=input('введи число ')
print(type(lucky_number))
if lucky_number:
    print(lucky_number +' это твой счастливый номер!')
else:
    print('Введи число')