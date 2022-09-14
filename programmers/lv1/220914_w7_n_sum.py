def solution(n):
    answer = 0
    str_n = str(n)
    for nn in str_n:
        answer += int(nn)
    return answer
