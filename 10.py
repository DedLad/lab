for i in (str(input('enter a sentence '))):
    if i=='z':
        print('a',end='')
    elif i == 'Z':
        print('A',end='')
    else:
        print(chr(ord(i)+1))