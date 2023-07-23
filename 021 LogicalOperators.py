# Логические операторы
# есть 2 переменные, нам надо узнать действительно ли оба этих сравнения являются истиной
x=1
y=2
print(x>y)
print(x<y)
#False
#True

#  Сущ-ют 3 логических оператора  and    or    not 
print(x>1 and y>1)
#False
print(x>1 or y>1)
#True
print(not x>1)
# Возвращает обратное Булевое значение
#True
print('---------------')
print(True and True)
print(True or True)
print(not True)

print(False and False)
print(False or False)
print(not False)

print(True and False)
#False
print(True or False)
#True

name = "Anton"
age = 21
is_married = False
if age > 18 and is_married == False:
    print('Привет {}! ты можешь найти девушку тут'.format(name))
#Привет Anton! ты можешь найти девушку тут