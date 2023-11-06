l = []
for i in range (1,int(input('number of elements in list '))+1):
    l.append(int(input(f'enter value {i} ')))
print(l)
s = int(input('enter count for element to include '))
r=[]
for i in l:
    if l.count(i)==s:
        r.append(i)

print(r)