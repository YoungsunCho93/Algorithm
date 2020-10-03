def solution(s):
    answer = []
    tupleArray = s[2 : len(s) - 2].split("},{")

    for idx in range(len(tupleArray)):
        tupleArray[idx] = list(map(int, tupleArray[idx].split(",")))

    tupleArray.sort(key=len)

    for tuple in tupleArray:
        for i in tuple:
            if i not in answer:
                answer.append(i)
                break

    return answer