# 1년 만기 정기 예금을 얼마나 예치하시겠습니까? 20000
# 원금이 20000원이시군요
# 이자는 2000원입니다.
# 원리합계는 22000원 입니다.


money = int(input("1년 만기 정기 예금을 얼마나 예치하시겠습니까? "))
if money >= 20000:
    rest = money//10
    print("이자는", str(rest) + "원입니다.")
    print("원리합계는", str(money+rest) + "원 입니다.")
