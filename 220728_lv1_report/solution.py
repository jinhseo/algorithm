def solution(id_list, report, k):
    answer = [0 for i in id_list]
    reported = {i:0 for i in id_list}
    reporter = {i:[] for i in id_list}
    final_reported = []

    for r in report:
        er, target = r.split(' ')
        reporter[er].append(target)

    for a in reporter:
        reporter[a] = set(reporter[a])

    for r in reporter:
        for rr in reporter[r]:
            reported[rr] += 1
    #for r in reporter:
    #    er, target = r.split(' ')
    #    reported[target] += 1

    for n, result in enumerate(reporter):
        for r in reporter[result]:
            if r in list(reported.keys()):
                if reported[r] >= k:
                    answer[n] += 1

    #print(reporter)
    #print(reported)
    return answer

### 31:53 2nd try ###
