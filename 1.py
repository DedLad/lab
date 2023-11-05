n = int(input('enter positive integer'))
if n>0:
    print('it is a palindrome ') if str(n)==str(n)[::-1] else print('not a palindrome')
elif n ==0:
    print('the given integer is a 0 ')
else:
    print('enter postitive value only')