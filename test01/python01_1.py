def odd_nums(list_org):
    lst = []
    for i in list_org:
        if i % 2 == 1:
            lst.append(i)
    lst.sort()
    print(lst)


odd_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
