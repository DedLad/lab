
row_col = int(input("Enter the number of rows and columns: "))

input_lst1 = []
for _ in range(row_col):
    row = input("Enter row elements separated by space: ").split()
    row_int = [int(num) for num in row]
    input_lst1.append(row_int)

transpose_lst = []
for i in range(row_col):
    transposed_row = []
    for j in range(row_col):
        transposed_row.append(input_lst1[j][i])
    transpose_lst.append(transposed_row)


print("Transpose of the 2D list:")
for row in transpose_lst:
    print(row)
