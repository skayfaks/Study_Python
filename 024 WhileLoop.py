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


x=0
""" while x<10:
    print(str(x) + ' x - menshe 10')
    x += 1
else:
    print(str(x) + ' x - teper menshe 10') """

for x in range(10):
    print(str(x) + ' x - menshe 10')
else:
    x += 1
    print(str(x) + ' x - teper menshe 10')