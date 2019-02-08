def cleaner(*args):
    lst_result = []

    for i in args:
        if isinstance(i, (int, float)):
            lst_result.append(i)
        elif isinstance(i, (tuple, list)):
            for item in i:
                if isinstance(item, (int, float)):
                    lst_result.append(item)

    # 여기에 코드를 작성하세요

    return lst_result


# BEGIN: 점검을 위한 코드이니 수정하지 마십시오
print(cleaner(3, 9, "Python", 2, 8, "Java"))
print(cleaner(3, 9, "Python", 2, 8, "Java") == [3, 9, 2, 8])
print(cleaner(2, 6, "Programming", (1, 3), [4, 4]))
print(cleaner(2, 6, "Programming", (1, 3), [4, 4]) == [2, 6, 1, 3, 4, 4])
# END: 점검을 위한 코드이니 수정하지 마십시오
