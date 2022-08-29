def solution(array, commands):
    answer = []
    for c in commands:
        #first_array = array[c[0]-1:c[1]]
        #sorted_array = sorted(first_array)
        #final = sorted_array[c[2]-1]
        #answer.append(final)
        a = array[c[0]-1:c[1]]
        answer.append(sorted(a)[c[2]-1])
    return answer
