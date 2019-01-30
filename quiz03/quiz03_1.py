while True:
    x = input("수를 입력하세요:")
    try:
        x = int(x)
        sum = 0
        for i in range(1, x + 1):
            if i % 3 == 0:
                sum += i
        print("1부터 ", i, "까지 3의 배수의 합 : ", sum)
        break
    except Exception as e:
        print("정수가 아닙니다. 다시 입력하세요.")
