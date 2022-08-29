def solution(lottos, win_nums):
    answer = []
    correct = 0

    for win_num in win_nums:
        if win_num in lottos:
            correct += 1
    min_correct = correct

    for lotto in lottos:
        if lotto == 0:
            correct += 1
    max_correct = correct

    answer = [7-max_correct, 7-min_correct]

    if answer[-1] == 7:
        answer[-1] = 6
    if answer[0] >= 7:
        answer[0] = 6

    return answer

### 1st trial 12:50 ###
### test_case 14 -> length of max_correct ###
