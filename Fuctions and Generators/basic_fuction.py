def list_sort(l):
    for i in range(len(l)):
        print(l[i])
        for j in range(len(l)):
            print(l[j])
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
    return l

if __name__ == '__main__':
    l = [11, 23, 23, 4, 53, 6, 17, 8, 9, 10]
    print(list_sort(l))

