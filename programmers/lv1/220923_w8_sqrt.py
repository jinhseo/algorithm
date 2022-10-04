import math

def solution(n):
    answer = 0
    str_n = str(math.sqrt(n))
    if str_n.split('.')[-1] != '0':
        answer = -1
    else:
        answer = (int(str_n.split('.')[0])+1)**2
    return answer
