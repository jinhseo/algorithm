def solution(s):
    answer = True
    s = s.lower()
    no_p = 0
    no_y = 0
    if 'p' not in s and 'y' not in s:
        return True
    for spell in s:
        if spell == 'p':
            no_p +=1
        elif spell == 'y':
            no_y += 1

    if no_p == no_y:
        return True
    else:
        return False
    return True
