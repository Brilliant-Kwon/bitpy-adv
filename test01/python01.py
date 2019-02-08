def odd_nums(lst_num):
    lst_result = []
    for i in lst_num:
        if i % 2 == 1:
            lst_result.append(i)
    lst_result.sort()
    # print(lst_result)
    # 여기에 추가 코드를 작성하세요

    return lst_result


# BEGIN: 점검을 위한 코드이니 수정하지 마십시오
print(odd_nums([1, 2, 4, 5, 6, 3, 10, 9, 7, 8]))
print(odd_nums([1, 2, 4, 5, 6, 3, 10, 9, 7, 8]) == [1, 3, 5, 7, 9])
print(odd_nums([9, 12, 3, 18, 6, 15, 21]))
print(odd_nums([9, 12, 3, 18, 6, 15, 21]) == [3, 9, 15, 21])
# END: 점검을 위한 코드이니 수정하지 마십시오

# 추가 테스트를 위해 아래 추석을 해제하시고 활용하셔도 좋습니다
# print(odd_nums([]))
