# 람다 : 익명함수


def myfunc(x):
    return x ** 2


print(myfunc(5))

for i in range(10):
    print("{0}:{1}".format(i, myfunc(i)), end=" ")
else:
    print()

print((lambda x: x ** 2)(5))  # 일회성으로 사용하는 함수를 간단히 만들어 사용

for i in range(10):
    print("{0}:{1}".format(i, (lambda x: x ** 2)(i)), end=" ")
else:
    print()

strings = "Life is too short, you need Python" \
    .upper().replace(",", "").split()
print(strings)

strings.sort(key=lambda s: len(s))  # 길이를 기준으로 소트
print("SORT by length:", strings)
