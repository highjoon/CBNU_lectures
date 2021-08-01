"""
실습 1) 윤년 판별 프로그램

연도를 입력 받고, 해당 연도가 윤년인지 아닌지 판단하는 프로그램을 작성하여라.

윤년 조건
4의 배수인 해는 윤년
100의 배수인 해는 윤년이 아님
400의 배수인 해는 윤년

연도 입력: 2021
2021년은 윤년이 아닙니다.

연도 입력: 2100
2100년은 윤년이 아닙니다.

연도 입력: 2020
2020년은 윤년입니다.

연도 입력: 2000
2100년은 윤년입니다.
"""

year = int(input("년도 : "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("윤년")
else:
    print("아님")