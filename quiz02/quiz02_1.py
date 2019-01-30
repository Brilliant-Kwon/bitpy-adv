scope1 = input("과목 1 :")
scope1 = int(scope1)
scope2 = input("과목 2 :")
scope2 = int(scope2)
if scope1 >= 50 and scope2 >= 50:
    if (scope1 + scope2) / 2:
        print("합격")
    else:
        print("불합격")
else:
    print("불합격")
