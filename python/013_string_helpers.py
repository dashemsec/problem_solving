
word = 'Banana'

# str.islower()
if word.islower() is True:
    print('word is lower')
else:
    print('word is Upper')

# str.upper()
word2 = word.upper()
print(word2)

# str.find()
word = 'HELLO WORLD. WELCOME. NAMASTE'
print(word.find('NAMASTE'))
print(word.find('HI'))

if word.find('HI') is -1:
    print('sub-word not found!!!')
