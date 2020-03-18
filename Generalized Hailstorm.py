# Assignment 1, Question 2:
# Generalized Hailstorm


def hailStorm1(aa=10, bb=10, number=100):
    converge = []
    for a in range(1,aa):
        for b in range(1,bb):
            count = 0
            pattern = []
            infinite = False
            repeatSeries = False
            for num in range(3, number):   # starting iteration from 3 as 1 & 2 does not made any sense.
                tempNum = num
                eachSequence = []
                iteration = 0
                while True:
                    if tempNum == 1:
                        eachSequence.append(1)
                        break
                    elif tempNum in eachSequence:
                        repeatSeries = True
                        break
                    else:
                        eachSequence.append(tempNum)
                        if tempNum % 2 == 0:
                            tempNum //= 2
                            iteration += 1
                        else:
                            tempNum = (a * tempNum) + b
                            if tempNum % 2 != 0:
                                infinite = True
                                break
                            elif iteration > 500:
                                infinite = True
                                break
                            else:
                                iteration += 1
                if infinite:
                    infinite = False
                    continue
                elif repeatSeries:
                    repeatSeries = False
                    for x in pattern:
                        found = 0
                        for y in eachSequence[:-1]:
                            if y in x:
                                found = 1
                                break
                        if found:
                            break
                    else:
                        pattern.append(eachSequence)
                        count += 1
                elif len(pattern) == 0:
                    pattern.append(eachSequence)
                    count += 1
                else:
                    for x in pattern:
                        if len(x) >= 3 and len(eachSequence)>= 3:
                            if x[-1] == eachSequence[-1] and x[-2] == eachSequence[-2] and x[-3] == eachSequence[-3]:
                                break
                    else:
                        pattern.append(eachSequence)
                        count += 1
            converge.append('For a = %d and b = %d, number of holding patterns = %d' % (a, b, count))
    return converge

# printing the actual output for all values of a & b.
result = hailStorm1()    # calling function with default values
for x in result:
    print(x)