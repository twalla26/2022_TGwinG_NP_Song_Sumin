# 문제 1번
def sum(a,b):
    # your code
    return a+b

# 문제 2번
def sub(a,b):
    # your code
    return a-b

# 문제 3번
def mul(a,b):
    # your code
    return a*b

# 문제 4번
def div(a,b):
    # your code
    return a/b

# 문제 5번
def distance(x1,y1,x2,y2):
    # your code
    return ((x1-x2)**2+(y1-y2)**2)**1/2

# 문제 6번
def short():
    lylic = "life is short art is long"
    # your code
    return lylic[8:13]

# 문제 7번
def myReverse(string):
    # your code
    return string[::-1]

# 문제 8번
def letMeIntroduceMyself():
    # your code
    이름=input("이름을 입력하시오: ")
    취미=input("취미를 입력하시오: ")
    재학_중인_대학=input("재학 중인 대학을 입력하시오: ")
    생일=input("생일을 입력하시오(예시: 020619): ")
    print('제 이름은',이름,'입니다. 제 취미는',취미,'이구요. 저는',재학_중인_대학,'를 다니고 있습니다. 제 생일은',생일[2:4],'월',생일[4:6],'일 입니다.')
    return '제 이름은',이름,'입니다. 제 취미는',취미,'이구요. 저는',재학_중인_대학,'를 다니고 있습니다. 제 생일은',생일[2:4],'월',생일[4:6],'일 입니다.'

# 문제 9번
def calcAI():
    # your code
    a=input("첫 번째 숫자를 입력하시오: ")
    x=int(a)
    b=input("두 번째 숫자를 입력하시오: ")
    y=int(b)
    print('두 수의 합은',x+y,'입니다.')
    return '두 수의 합은',x+y,'입니다.'