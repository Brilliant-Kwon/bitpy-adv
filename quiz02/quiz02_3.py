msg = """
d:합산 w:차감 q:루프 탈출 나머지:?
    
method:"""
bal = 0
while True:
    x = input(msg)
    if x == "d":
        money = input("Amount:")
        bal += int(money)
        print("Balance:", bal)
    elif x == "w":
        money = input("Amount:")
        bal -= int(money)
        print("Balance:", bal)
    elif x == "q":
        break
    else:
        print("?")
