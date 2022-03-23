my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
i = 0
output = []
for key in my_dict:
    print(key)
    # key = 'a' when i =0 so i at 0 in the list is 1 then it
    output.append(my_dict[key][i])
    i += 1
print(output)

