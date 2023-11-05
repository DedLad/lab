
row_col = int(input("Enter the number of rows and columns: "))

input_lst1 = []
for _ in range(row_col):
    row = input("Enter row elements separated by space: ").split()
    row_int = [int(num) for num in row]
    input_lst1.append(row_int)

diagonal_sum = 0
for i in range(row_col):
    diagonal_sum += input_lst1[i][i]

average_diagonal = diagonal_sum / row_col

print("Average of elements along the main diagonal:", average_diagonal)
