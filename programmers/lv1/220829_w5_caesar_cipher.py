def solution(s, n):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    capital = alphabet.capitalize()
    for ss in s:
        if ss == ' ':
            answer += ss
        elif ss.islower():
            if alphabet.index(ss) + n > len(alphabet):
                lower_ind = len(alphabet) - alphabet.index(ss) + n -1
                cipher = alphabet[lower_ind]
            else:
                cipher = alphabet[alphabet.index(ss) + n]
        elif ss.isupper():
            if capital.index(ss) + n > len(capital):
                upper_ind = len(capital) - capital.index(ss) + n-1
                cipher = capital[upper_ind]
            else:
                cipher = capital[capital.index(ss) + n]

        answer += cipher

    return answer
### TODO test_case ###
