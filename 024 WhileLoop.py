#Ц отличается от FOR - код выполняется до того пока код в теле циклы не будет TRUE

""" x=5
while x>=1:
    print(x)
    x=x-1
     """
""" 
5
4
3
2
1 
"""
""" x=5
while x<10:
    print(x)
    x += 1 # x = x+1
print ("следующий код") """


""" x=0
while x<10:
    print(str(x) + ' x - menshe 10')
    x += 1
else:
    print(str(x) + ' x - teper menshe 10')
for x in range(10):
    print(str(x) + ' x - menshe 10')
else:
    x += 1
    print(str(x) + ' x - teper menshe 10') """


# ----- Какой цикл использовать каждый решает сам
# У цикла While есть несколько ключевых слов - это
#        break     continue     pass

""" my_list=[1,2,3]
for item in my_list:
    pass # служит для заполнения пустот в коде (исп-ся в методах и функциях)
print('drugoy kod')
 """


""" my_list=[1,2,3]
for y in my_list:
    if y==2:
        break # произведен переход в конец цикла (при условии item=2)
    print(y)
print('Privet') """


my_list=[1,2,3]
for y in my_list:
    if y==2:
        continue # 2=2 ->  переход в начало цикла
    print(y)
print('Все элементы перебраны')
#1
#3
#Все элементы перебраны