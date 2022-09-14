def solution(arr):
    answer = 0
    for v in arr:
        answer += v
    answer /= len(arr)
    return answer
