# 제어문 연습
def if_statement():
    """if문 예제"""
    # 금액을 입력 받고
    # 10000 이상이면 by taxi
    # 1000이상이면 by bus
    # 그 미만이면 on foot
    money = input("얼마 가지고 있어? ")
    money = int(money)

    message = ""

    if money >= 10000:
        message = "by taxi"
    elif money >= 1000:
        message = "by bus"
    else:
        message = "on foot"

    print("money : ", money, message)


def con_expr():
    """조건 표현식 예제"""

    money = int(input("얼마 가지고 있어? "))
    message = "by taxi" if money >= 10000 \
        else "by bus" if money > 1000 else "on foot"

    print("money : ", money, message)


def for_ex():
    """for loop 연습"""
    animals = ["dog", "cat", "cow", "tiger"]
    for animal in animals:
        print(animal, end=" ")
    else:  # for루프가 정상적으로 끝났을 때
        print()

    # 반복과 함께 인덱스도 받아와야 할 경우 enumerate
    for index, animal in enumerate(animals):
        print(index, animal)

    # 복합 자료형
    lst = [("홍길동", 90), ("전우치", 80), ("장길산", 95)]
    for item in lst:
        # print(item)
        print("이름:%s, 정수:%d" % item)

    lst = [{"name": "홍길동", "score": 90},
           {"name": "전우치", "score": 80},
           {"name": "장길산", "score": 75}]
    for item in lst:
        # print(item)
        print("이름:%(name)s, 점수:%(score)d" % item)

    # for문의 else 블록
    r1 = list(range(1, 12, 2))
    print(r1)
    r2 = r1 + [12, 13, 15]  # 문자열 이어줌

    # 내부에 짝수가 있으면 break
    for i in r1:
        if i % 2 == 0:
            print("짝수를 찾았습니다.")
            break
    else:  # 루프가 안전하게 종료되었을 때
        print("짝수는 없습니다.")

    for i in r2:
        if i % 2 == 0:
            print("짝수를 찾았습니다.")
            break
    else:  # 루프가 안전하게 종료되었을 때
        print("짝수는 없습니다.")

    print("삼각형 그리기")
    for i in range(1, 11):
        for j in range(1, i + 1):
            print("*", end="")
        else:
            print()

    # 파이썬 스타일
    for i in range(1, 11):
        print("*" * i)


# if_statement()
# con_expr()
for_ex()
