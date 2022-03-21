old_list = [1, 2, 3, 4]  # list
old_dict = {'a': 1, 'b': 2, 'c': 3}  # dict


def dict_to_list(d):
    new_list = []  # empty list
    for key, value in d:
        print(f'key: {key}, value: {value}')
        new_list.append(d[key])
        print(f'new_list: {new_list}')
    print(f'outside for loop new_list: {new_list}')
    return new_list


if __name__ == "__main__":
    print(f'old_dict: {old_dict}')
    new_list = dict_to_list(old_dict)
    print(f'new_list: {new_list}')
