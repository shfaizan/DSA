def list_sort(my_list):
    my_list.sort()
    return len(my_list), my_list


if __name__ == '__main__':
    my_list = [4, 66, 3546, 2, 446, 243634, 22, 44, 0, 5]
    print(list_sort(my_list))
