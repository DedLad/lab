

a= input('enter string ')
s=set()
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        s.add(a[i:j])
print(sorted(list(s)))