number_list = [32,21,48,34.34]
print(number_list)
#[32, 21, 48, 34.34]

some_list =  [12,35.22, 'STROKA']
print(some_list)
#[12, 35.22, 'STROKA']

print(len(some_list)) #через функцию len узнаем длинну
#3

#индексация и слайсинг элементов списка
print(some_list[1])
#35.22

#слайсинг (например хотим скопировать первые два элемента)
slising_list = (some_list[:2])
print(slising_list)
#[12, 35.22]

# В списках можно менять значение сод-ся во внутренних данных заменим значение STROKA на NEW
some_list[2] = "NEW"
print(some_list)
#[12, 35.22, 'NEW']

# Применение канкатенации 2х списков
konkat = number_list + slising_list
print(konkat)
#[32, 21, 48, 34.34, 12, 35.22]

