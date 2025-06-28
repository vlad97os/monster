import random

llist = ['тест1', 'тест2', 'тест3']
stroka = ', '.join(llist)
stroka = stroka.replace(',', '')
llist = stroka.split()
#print(stroka)
#print(llist)


text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris.'
list_text = text.split()
for i in list_text:
    if 'o' in i:
        print(i)
print(' '.join(list_text))

words = text.split()
fin_words = []
for word in words:
    if 'o' in word:
        print(word)
        # words.remove(word)
    else:
        fin_words.append(word)

print(' '.join(words))

pr = random.random()
print(f'Your price {int(pr * 100)}')