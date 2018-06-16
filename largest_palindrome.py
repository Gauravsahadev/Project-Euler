# Largest Palindrome from the product of two three digits number
num_list = []
i = 999
while i != 0:
    j = 999
    while j != 0:
        prod = str(int(i*j))
        rev = int(prod[::-1])
        if rev == int(prod):
            # print(i,j)
            num_list.append([i, j])
            break
        else:
            j -= 1
    i -= 1
# print(num_list)
# Printing the largest among the list
largest = int(num_list[0][0]+num_list[0][1])
total = len(num_list)
# finding the largest among the list
for k in range(1, total):
    if largest < num_list[k][0]+num_list[k][1]:
        largest = num_list[k][0]+num_list[k][1]
        index_num = k
# print the largest palindrome product numbers and its product
print(num_list[index_num], " ", num_list[index_num][0]*num_list[index_num][1])
