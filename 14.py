x= input('enter message ')
a = int(input('enter shift value '))
for i in x:
    if i == ' ':
        print(' ',end='')
    else:
        print(chr(ord(i)+a),end='')