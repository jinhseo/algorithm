def solution(numbers):
    answer = -1
    z_to_n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in numbers:
        if num in z_to_n:
            z_to_n.remove(num)
    answer = sum(z_to_n)
    return answer
