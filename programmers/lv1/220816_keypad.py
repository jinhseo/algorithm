def solution(numbers, hand):
    answer = ''
    l_pos = '*'
    r_pos = '#'
    l_dist = 0
    r_dist = 0
    dist = {'13':[1,2,3,4], '46':[2,1,2,3], '79':[3,2,1,2], '*#':[4,3,2,1], '2':[0,1,2,3], '5':[1,0,1,2], '8':[2,1,0,1], '0':[3,2,1,0]}
    mid = [2,5,8,0]

    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            l_pos = num
        elif num in [3,6,9]:
            answer += 'R'
            r_pos = num
        else:
            for ks in dist.keys():
                if str(l_pos) in ks:
                    l_dist = dist[ks][mid.index(num)]
                if str(r_pos) in ks:
                    r_dist = dist[ks][mid.index(num)]
            if l_dist > r_dist:
                answer += 'R'
                r_pos = num
            elif l_dist < r_dist:
                answer += 'L'
                l_pos = num
            elif l_dist == r_dist:
                if hand == 'right':
                    answer += 'R'
                    r_pos = num
                elif hand == 'left':
                    answer += 'L'
                    l_pos = num
    return answer
### 2nd trial ### 30min
