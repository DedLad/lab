# # Get input from the user
# input_string = input("Enter a string: ")

# # Find unique substrings and print them in lexicographical order
# substrings = sorted({input_string[i:j] for i in range(len(input_string)) for j in range(i + 1, len(input_string) + 1)})
# print("Unique substrings in lexicographical order:", substrings)

a= input('enter string ')
s=set()
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        s.add(a[i:j])
print(sorted(list(s)))