llist = ['тест1', 'тест2', 'тест3']
stroka = ', '.join(llist)
stroka = stroka.replace(',', '')
llist = stroka.split()
print(stroka)
print(llist)
