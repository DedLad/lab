n = int(input('enter rows '))
for i in range(1, n + 1):
        hash_count = n - i
        number_count = i
        pattern = '#' * hash_count + ''.join(str(j) for j in range(number_count, 0, -1))
        print(pattern)
        