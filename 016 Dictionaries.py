#Словари - структуры данных содержащие не упоряд-ю послед-ть различных объектов (в отличии от листов или списков)
#В словарях данные хр-ся в формате ключ-значение и доступ к значению можно получить по ключу

""" car_prices = {'opel':5000, 'toyota':7000, 'bmv':10000}
print(car_prices)
#{'opel': 5000, 'toyota': 7000, 'bmv': 10000}

print(car_prices['opel']) #указываем ключ
#5000

car_prices['mazda']=4000
print(car_prices)
#{'opel': 5000, 'toyota': 7000, 'bmv': 10000, 'mazda': 4000}

#если присвоить значение имеющемуся ключу, то оно поменяется
car_prices['opel']=1111
print(car_prices)
#{'opel': 1111, 'toyota': 7000, 'bmv': 10000, 'mazda': 4000}

# Удаление значения. !! ЕСЛИ указать команду del car_prices - без ключа, удаляется весь словарь !!
del car_prices['opel']
print(car_prices)
#{'toyota': 7000, 'bmv': 10000, 'mazda': 4000}

# Если надо очистить 
car_prices.clear()
print(car_prices)
#{} """

# В словарях возможна вложенность (Другой список, или словарь) Часто использ-ся для описания объектов
# ОБРАТИТЕ внимание на форматирование и запятые (перевод на новую строку)
person = {
    'first name': 'Anton',
    'last name': 'Kriv',
    'age': 30,
    'hobbies': ['football', 'singing', 'photo'],      # вложенный список
    'children': {'son': 'Viktor', 'wife': 'Nadya'}   # можно вложить другой словарь
}

# выведем возраст
print(person['age'])
#30
print(person['hobbies'])
#['football', 'singing', 'photo']

# Выводим из вложенного списка в словаре Хобби с индексом 2
hobbies = person['hobbies']
print(hobbies[2])
#photo

print(person['hobbies'][2]) # Можно сделать короче. Обратившись сразу к значнию
#photo

print(person['children']['son'])
#Viktor

# Добавим данные
person['car'] = 'Mazda'
print(person)
#{'first name': 'Anton', ............ , 'car': 'Mazda'}

# Заменим элемент - поменяем хобби football ['football', 'singing', 'photo'] на driving
person['hobbies'][0] = 'driving'
print(person['hobbies'])
#['driving', 'singing', 'photo']

# ! Получаем список ключей словаря ! 
print(person.keys())
#dict_keys(['first name', 'last name', 'age', 'hobbies', 'children', 'car'])

# ! Получаем все значения по всем  ключам
print(person.values())
#dict_values(['Anton', 'Kriv', 30, ['driving', 'singing', 'photo'], {'son': 'Viktor', 'wife': 'Nadya'}, 'Mazda'])

# Можем получить все элементы. Структура называется КОРТЭЖ
print(person.items())
# dict_items([('first name', 'Anton'), ('last name', 'Kriv'), ('age', 30), ('hobbies',
# ['driving', 'singing', 'photo']), ('children', {'son': 'Viktor', 'wife': 'Nadya'}), ('car', 'Mazda')])