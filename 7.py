
n = int(input("Enter the number of elements: "))


lst1 = []
for _ in range(n):
    element = int(input("Enter an element: "))
    lst1.append(element)


m = []
for i in range(n):
    next_index1 = (i + 1) % n
    next_index2 = (i + 2) % n
    e = lst1[next_index1] + lst1[next_index2]
    m.append(e)

print("Modified list:", m)
