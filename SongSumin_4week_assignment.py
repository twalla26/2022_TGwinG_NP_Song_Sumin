# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 입력을 요구하는 문제가 없습니다.
# answer 변수를 사용하여 문제를 풀이하세요. 반환값은 answer 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 5일 23시 59분.
# 지각 제출 기한: 2022년 4월 6일 23시 59분. 주차 점수에서 20% 감점


# 문제 1번
def intervention(queue):
    answer = list()
    # your code
    if ("성은" in queue) and queue.index("성은") >= 4:
        queue.insert(queue.index("성은") + 1, "승호")

    elif ("성은" in queue) and (queue.index("성은")) < 4 or "성은" not in queue:
        queue.insert(10, "승호")

    answer = list(queue)
    return answer


# 문제 2번
def pascal(n):
    answer = list()
    # your code
    answer = [1, 1]
    iter = 1
    while(True):
        next = [1]
        for i in range(iter):
            next.append(answer[i] + answer[i + 1])
        next.append(1)
        iter += 1
        answer = next
        if len(answer) == n:
            return answer




# 문제 3번
def auto_complete(entry, searchWords):
    answer = list()
    # your code
    realanswer = []
    for i in searchWords:
        if entry in i:
            realanswer.append(i)

    realanswer.sort()
    answer = realanswer
    return answer




# 문제 4번
def stock_price(stockChart):
    answer = str()
    # your code
    price = 0
    priceList = []
    for i in stockChart:
        price += i
        priceList.append(price)
    priceList.reverse()
    n = min(priceList)
    k = priceList.index(n)
    if priceList[0] - min(priceList) > 0:
        answer = "%s일 전에 샀어야지 으이구" %k
        return answer
    else:
        answer = "아니야 조금만 더 기다려"
        return answer






# 문제 5번
# 이해하고 넘어가기

def decryption(letter):
    answer = str()
    # your code
    before = ["d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c"]
    after = ["a","b","c","d","e","f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    for i in letter:
        if i in before:
            answer += after[before.index(i)]
        else:
            answer += i
        
    return answer


'''
필기
1. += 는 문자열, append 는 리스트에 쓴다.
2. 리스트 매소드 중에서 index()는 리스트 중에서 특정한 원소가 몇 번째에 처음으로 등장했는지를 알려주는데, 
인덱스를 알려주기 때문에 index 라는 이름으로 되어 있다. 
그런데 만약에 두 번 이상 원소가 중복되어 존재하는 경우에는 맨 처음 등장한 순간의 인덱스를 출력해준다는 점을 기억하자. 


'''