# 이번 주차부터는 컴파일 에러 등으로 프로그램 자체가 실행되지 않을 시에는 과제 점수 0점 처리합니다.
# 문제에서 요구하는 입출력 외에는 절대 포함해서 제출하지 마세요. 0점 처리합니다.
# 문제에서 요구하는 출력 형식, 반환 형식을 "모두" 지켜주세요. 지키지 않으면 오답처리 됩니다.
# 한 파일에 모든 문제를 풀이해서 제출하세요. 분리 제출 시 채점자 PC기준 최상위에 정렬되는 파일만 채점합니다.
# 제출 마감일: 2022-03-29 23:59, 지각 제출 시 점수에서 20% 감점입니다.

# 문제 1번
def question1():
    # your code
    return "next"

    
# 문제 2번
def leapYear(year):
    # your code
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "윤년입니다."
    else:
        return "윤년이 아닙니다."



# 문제 3번
def alram(time):
    # your code
    time = int(time)
    a = time // 100
    b = time % 100
    if a <= 12 and b >= 45 :
        b = b - 45
        return "오전 " + str(a) + "시 " + str(b) + "분"
    
    elif a <= 12 and b < 45 :
        a = a - 1
        b = b + 15
        return "오전 " + str(a) + "시 " + str(b) + "분"

    elif a > 12 and b >= 45 :
        b = b - 45
        return "오후 " + str(a) + "시 " + str(b) + "분"

    elif a > 12 and b < 45 :
        a = a - 1
        b = b + 15
        return "오후 " + str(a) + "시 " + str(b) + "분"

    else: 
        return "오류입니다."



# 문제 4번
def findDaesun(x1,y1,r1,x2,y2,r2):
    # your code
    distance = pow(((x1-x2)**2+(y1-y2)**2),1/2)
    if distance == 0 and r1 == r2 :
        return "어딘지 모르겠다 오바"
    elif (distance == 0 and r1!=r2) or (r1 + r2 < distance) or (abs(r1-r2) > distance) :
        return int("0")
    elif r1 + r2 == distance or abs(r1-r2) == distance :
        return int("1")
    elif abs(r1-r2) < distance < r1+r2 :
        return int("2")
    else:
        return "오류입니다."

