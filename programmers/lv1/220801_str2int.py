def solution(s):
    answer = ''
    for n, ss in enumerate(s):
        if ss.isdigit():
            answer += ss
        else:
            if s[n] == 'z' and n + 3 < len(s):
                if s[n+3] == 'o':
                    answer += '0'
            elif s[n] == 'o' and n + 2 < len(s):
                if s[n+2] == 'e':
                    answer += '1'
            elif s[n] == 'e' and n + 4 < len(s):
                if s[n+4] == 't':
                    answer += '8'
            elif s[n] == 'n' and n + 3 < len(s):
                if s[n+3] == 'e':
                    answer += '9'
            elif s[n] == 't' and n + 4 < len(s):
                if s[n+4] == 'e':
                    answer += '3'
            elif s[n] == 't' and n + 2 < len(s):
                if s[n+2] == 'o':
                    answer += '2'
            elif s[n] == 'f' and n + 3 < len(s):
                if s[n+3] == 'r':
                    answer += '4'
                elif s[n+3] == 'e':
                    answer += '3'
            elif s[n] == 's' and n + 4 < len(s):
                if s[n+4] == 'n':
                    answer += '7'
            elif s[n] == 's' and n + 2 < len(s):
                if s[n+2] == 'x':
                    answer += '6'

    #print(answer)
    answer = int(answer)
    return answer

### 16:38 2nd try ###
