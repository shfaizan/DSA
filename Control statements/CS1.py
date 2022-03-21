old_list = ['a', 'b', 'c', 'd']  # list
old_dict = {'a': 1, 'b': 2, 'c': 3}  # dict


def dict_to_list(d):
    new_list = []  # empty list
    for key in d:
        new_list.append(d[key])
        print(f'new_list: {new_list}')
    print(f'outside for loop new_list: {new_list}')
    return new_list


def list_to_dict(l):
    new_dict = {}  # empty dict
    for i in range(len(l)):
        new_dict[i] = l[i]
    print(f'outside for loop new_dict: {new_dict}')
    return new_dict


if __name__ == "__main__":
    print(f'old_dict: {old_dict}')
    new_list = dict_to_list(old_dict)
    new_dict = list_to_dict(old_list)
    print(f'new_dict: {new_dict}')
    print(f'new_list: {new_list}')
