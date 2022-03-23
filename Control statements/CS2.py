my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(f'value of item is {item}')

for i, value in enumerate(my_list):
    print(f'index of item is {i} and value is {value}')

my_dict = {'a': 'eminem', 'b': 'enrique', 'c': 'akon'}
for i in my_dict:
    print(f'key is {i} and value is {my_dict[i]}')
