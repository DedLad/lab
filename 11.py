d={}
for i in range(1,1+(int(input('enter number of elements for dict ')))):
    x = eval(input(f'enter val {i} for key(use quotes if string) '))
    d[x]=str(type(x))
print(d)
for i,j in d.items():
    if j == '<class \'str\'>':
        print(i,end=' ')

