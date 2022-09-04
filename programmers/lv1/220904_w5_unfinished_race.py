import collections
df solution(participant, completion):
    answer = ''
    p = collections.Counter(participant)
    c = collections.Counter(completion)
    answer = list((p-c).keys())[0]
    return answere
