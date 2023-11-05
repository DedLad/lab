l = []
for i in range (1,int(input('number of elements in list '))+1):
    l.append(int(input(f'enter value {i} ')))
# print(l)
l=list(set(l))
# print(l)
k = int(input('enter position of smallest number you want '))
if len(l)>=k:
    for i in range(1,k):
        l.remove(min(l))
    print(min(l))
else:
    print(None)