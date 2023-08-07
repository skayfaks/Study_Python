# Так же мы можем использовать короткую форму записей для словарей

dict={'f':1,'s':2,'t':3}
# например мы хотим создать новый словарь в котором будут содержаться значения возв-е в 3ю степень
new_dict={key: value**3 for key,value in dict.items()} # читаем с for для key и value из dict мы помещаем в новый словарь key: value**3
print(new_dict)          # по умолчанию при обращению к словарю он возвращает только КЛЮЧИ! надо применить метод .items 


# так же мы можем получать значения и из списка
""" number_list=[6,2,11,-55,0,-12,3,345]
# например старое значение будет ключом а новое этот элемент в квадрате
num_dict={number:number**2 for number in number_list}
print(num_dict) """
#{6: 36, 2: 4, 11: 121, -55: 3025, -12: 144, 3: 9, 345: 119025}


# так же мы можем использовать логические операторы
# ключ старое значение, если значение положительное помещаем positiv, если отрицательное negotiv
""" number_list=[6,2,11,-55,0,-12,3,345]
num_dict2={number:'positive' if number>0 else 'negotive' if number<0 else 'zero' for number in number_list}
print(num_dict2) """
# {6: 'positive', 2: 'positive', 11: 'positive', -55: 'negotive', 0: 'zero', -12: 'negotive', 3: 'positive', 345: 'positive'}


# Множества
number_list=[6,2,11,-55,0,-12,3,345]
num_set={number**2 for number in number_list}
print(num_set)
#{0, 36, 4, 9, 144, 3025, 119025, 121}   - мы получаем не упорядоченные элементы ( Так как множество - это неупор элементы)

num_set={number**2 for number in range(3,10)}
print(num_set)
#{64, 36, 9, 16, 49, 81, 25} получаем не упорядоченную выборку элементос с 3 по 9 возв-е в квадрат

# можем создать множество
letter_set={letter.upper() for letter in 'hello'} # метод .upper() делает буквы заглавными
print(letter_set)
# {'l', 'e', 'o', 'h'} - получаем множество уникальных элементов ПОЭТОМУ l - всего одна