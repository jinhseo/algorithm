def solution(absolutes, signs):
    answer = 0
    for (abs, sign) in zip(absolutes, signs):
        if sign:
            answer += abs
        else:
            answer -= abs
    return answer
