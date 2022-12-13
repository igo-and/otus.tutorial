

a = {1, 3, 5, 7, 9, 11}

b = {
    'q' : {3, 33},
    'w' : {5, 55},
    'e' : {7},
    'r' : {9}
}
print('выводим ТОЛЬКО значения ')
for j in b.values():
    print( j, type(j) )

print('\nвыводим КЛЮЧ - Значение')
for j in b.items():
    print( j)

