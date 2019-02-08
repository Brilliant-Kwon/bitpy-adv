def statistics(*args):
    lst_result = []

    # 여기에 코드를 작성하십시오
    for i in args:  # 수치계싼이 필요한 자료형만 빼서 lst_result에 저장
        if isinstance(i, (int, float)):
            lst_result.append(i)

    return max(lst_result), min(lst_result), sum(lst_result), sum(lst_result) / len(lst_result)


# BEGIN: 점검을 위한 코드이니 수정하지 마십시오
print(statistics(80, 90, 70, 80))
print(statistics(80, 90, 70, 80) == (90, 70, 320, 80.0))
print(statistics(75, 80, 90, 100, 85))
print(statistics(75, 80, 90, 100, 85) == (100, 75, 430, 86.0))
# END: 점검을 위한 코드이니 수정하지 마십시오
