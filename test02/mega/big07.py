data = input("당신의 나이를 입력 ")

# 나이가 100세 이상이면, 어른이시군요!
# 나이가 100세 미만이면, 어른이 아니시군요!
# 숫자로 변환할 필요가 있다.

age = int(data)

# 조건문(비교연산자)의 결과는 True/False
if age >= 100 :  #콜론(:)
    print('어른이시군요!')  # 조건문의 결과가 True
else:
    print('어른이 아니시군요!')  # 조건문의 결과가 False

# >(초과), >=(이상), ==(동일), !=(다름) <-!는 not의 의미


# data는 ram의 저장공간을 말함.
# data의 저장공간을 나타내는 변수
# 변수들의 이름(변수명)은 다 달라야 한다.
# 변수명은 소문자로 시작하는 것이 일반적이다.
# 변수명의 시작을 숫자로 시작하면 안된다.
# 파이썬에서는 변수명을 만들 때, 스네이크 표기법을 쓰는 것을 권장
# 변수명은 한글, 일본어, 중국어를 사용 가능하나 지양해야 함.
# 유니코드를 지원
# 코딩은 기본적으로 영어를 원칙으로 한다.