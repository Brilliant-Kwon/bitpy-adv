def create_home():
    dir = "C:\\Users\\k1212\\bitacademy\\bitpy-adv\\samples"

    import os
    if not os.path.exists(dir):
        os.makedirs(dir)  # 디렉터리 생성
        print("creadted : ", dir)
    else:
        print("이미 있습니다.")


def write_text():
    fname = "C:\\Users\\k1212\\bitacademy\\bitpy-adv\\samples\\test.txt"
    f = open(fname, "wt")  # t는 생략가능
    size = f.write("Life is too short, You need Python")
    print("written size:", size)
    f.close()

    # 여러 줄을 write
    f = open("C:\\Users\\k1212\\bitacademy\\bitpy-adv\\samples\\multiline.txt", "wt", encoding="utf-8")
    for i in range(100):
        f.write("Line %d\n" % i)
    f.close()


def read_text():
    f = open("C:\\Users\\k1212\\bitacademy\\bitpy-adv\\samples\\multiline.txt", "rt", encoding="utf-8")
    text = f.read()
    print(text)
    f.close()

    # 줄 단위로 불러오기
    f = open("C:\\Users\\k1212\\bitacademy\\bitpy-adv\\samples\\multiline.txt", "rt", encoding="utf-8")
    while True:
        line = f.readline()  # 파일로부터 한줄 읽기
        if not line:  # 읽어온 값이 없으면 루프 탈출
            break
        print(line)

    f.close()

    # 편의 : 내용을 불러와서 자동으로 줄단위 리스트로 변환
    # readlines
    f = open("C:\\Users\\k1212\\bitacademy\\bitpy-adv\\samples\\multiline.txt", "rt", encoding="utf-8")
    lines = f.readlines()
    print(lines)

    for line in lines:
        print(line.strip())

    f.close()


def practices():  # 응용
    """sangbuk.csv로부터 내용을 읽어와서 각 선수별 리스트로 만들어 출력"""

    f = open("C:\\Users\\k1212\\bitacademy\\bitpy-adv\\samples\\sangbuk.csv", "rt", encoding="utf-8")
    members = []  # 빈 리스트
    while True:
        line = f.readline()
        if not line:
            break
        # print(line)
        line = line.strip().replace(",", "")  # 공백 제거
        info = line.split()  # 문자열 - > 배열
        print(info)
        member = {"name": info[0], "number": info[1], "height": info[2], "position": info[3]}
        members.append(member)

    print(member)
    print(members)

    f.close()


create_home()
write_text()
read_text()
practices()
