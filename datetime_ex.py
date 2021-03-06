# datetime 예제
import datetime  # datetime, date, time, timedelta

# 현재 시간을 얻어오기
now = datetime.datetime.now()
print(now)

# 생성자 이용 시간 만들기
past = datetime.datetime(1999, 12, 31)
print(past)

# dt = datetime.datetime(1999, 13, 32)  # 없는날짜 -> ValueError오류 발생

# datetime의 속성들
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

# datetime의 메서드들
print("요일:", now.weekday())  # 요일 월(0)~일(6)

now_date = now.date()  # date 객체를 추출
print(now_date, type(now_date))
now_time = now.time()  # time객체를 추출
print(now_time, type(now_time))

# 날짜는 비교가 가능
print(now > past)  # 대소 비교가 가능, 날짜가 뒤쪽이면 크다.

# 날짜의 차이도 얻을 수 있습니다.
datediff = now - past
print(datediff, type(datediff))  # timedelta 객체

# timedelta의 속성
print(datediff.days, datediff.seconds, datediff.microseconds)
print(datediff.total_seconds())  # 시간차이를 초단위로 반환

# datetime과 timedelta를 합산, 새 시간을 만들어 낼 수 있음
diff = datetime.timedelta(days=365)  # 시간차 365일
print("365일 후 : ", now + diff)

import locale

locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')  # 한글 인코딩 설정 강제설정
# datetime 포매팅
print(now.strftime("%Y/%m/%d %H:%M"))
print(now.strftime("%Y년 %m월 %d일 %H시 %M분"))  # 한글 오류 발생

# 문자열로된 날짜 정보가 있을 경우 : strptime
str = "2019-12-24 23:59"
dt = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M")  # 해독문자 삽입
print(dt, type(dt))
