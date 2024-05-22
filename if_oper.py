# (1)
x = 38
print('дратути!')
if x < 0:
    print('Меньше нуля')
print('дотвидания!')

# (2)
a, b = 10, 5
if a > b: # True
    print('a > b')
if a > b and a > 0: # True
    print('успех1')
if (a > b) and (a > 0 or b < 1000): # True
    print ('успех2')
if 5 < b and b < 10: # условие False на первой части выражения
    print('успех3')

# (3)
if '34' > '123':
    print('успех4')
if '123' > '12':
    print('успех5')
if [1, 2] > [1, 1]:
    print('успех6')

# (4)
if '6' > 5: # TypeError: '>' not supported between instances of 'str' and 'int'
    print('успех7')
if [5, 6] > 5: # TypeError: '>' not supported between instances of 'list' and 'int'
    print('успех8')
if '6' != 5:
    print('успех9')

