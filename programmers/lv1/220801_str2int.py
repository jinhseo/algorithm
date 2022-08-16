def solution(s):
    answer = ''
    '''for n, ss in enumerate(s):
        if ss.isdigit():
            answer += ss
        else:
            if s[n] == 'z' and n + 3 < len(s):
                if s[n+3] == 'o':
                    answer += '0'
            if s[n] == 'o' and n + 2 < len(s):
                if s[n+2] == 'e':
                    answer += '1'
            if s[n] == 'e' and n + 4 < len(s):
                if s[n+4] == 't':
                    answer += '8'
            if s[n] == 'n' and n + 3 < len(s):
                if s[n+3] == 'e':
                    answer += '9'
            if s[n] == 't' and n + 2 < len(s):
                if s[n+1] == 'w':
                    answer += '2'
            if s[n] == 't' and n + 4 < len(s):
                if s[n+1] == 'h':
                    answer += '3'
            if s[n] == 'f' and n + 3 < len(s):
                if s[n+1] == 'o':
                    answer += '4'
            if s[n] == 'f' and n + 3 < len(s):
                if s[n+1] == 'i':
                    answer += '5'
            if s[n] == 's' and n + 2 < len(s):
                if s[n+1] == 'i':
                    answer += '6'
            if s[n] == 's' and n + 4 < len(s):
                if s[n+1] == 'e':
                    answer += '7'
    '''
    candidate = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for cand in candidate:
        if cand in s:
            s = s.replace(cand, str(candidate.index(cand)))
    answer = int(s)
    return answer
### 16:38 2nd try ###
### 220811 final solution ###
