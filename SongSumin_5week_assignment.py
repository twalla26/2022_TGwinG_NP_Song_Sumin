# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 입력을 요구하는 문제가 없습니다.
# result 변수를 사용하여 문제를 풀이하세요. 반환값은 result 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 12일 23시 59분.
# 지각 제출 기한: 2022년 4월 13일 23시 59분. 주차 점수에서 20% 감점
import math

def calcCircleArea(r):
    result = float()
    result = float("{:.2f}".format(result))
    return result

def calcLog(a, b):
    result = float()
    result = round(math.log(b,a),2)
    return result
    
def calcSin(x):
    result = float()
    result = round(math.sin(x),2)
    return result
def calcFactorial(x):
    result = int()
    result = math.factorial(x)
    return result
def calcCombination(n, r):
    result = int()
    result = math.comb(n, r)
    return result

def calculator(order):
    answer = 0
    orderList = order.split()
    if "원넓이:" == orderList[0]:
        answer = calcCircleArea(float(orderList[1]))
    elif "로그:" == orderList[0]:

        if orderList[1] == "e":
            answer = calcLog(math.e, float(orderList[2]))
        else:
            answer = calcLog(float(orderList[1]), float(orderList[2]))


    elif "사인:" == orderList[0]:
        answer = calcSin(float(orderList[1]))
    elif "팩토리얼:" == orderList[0]:
        answer = calcFactorial(int(orderList[1]))
    elif "조합:" == orderList[0]:
        answer = calcCombination(int(orderList[1]), int(orderList[2])) 
    return answer

print(calculator("원넓이: 10"))
print(calculator("로그: e 10"))
print(calculator("사인: 100"))
print(calculator("팩토리얼: 5"))
print(calculator("조합: 3 2"))