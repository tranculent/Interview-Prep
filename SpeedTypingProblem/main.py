# I = string she is given to type
# P = string that she typed
# res = P - I = how many letters she needs to delete from P to get to I

# how many letters need to be deleted from P to get to I
# or
# if it's possible just by deletion of letters from P to get to I = IMPOSSIBLE

from re import I

with open('input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

nCases = int(input_lines[0])
res = []

for i in range(1, nCases+2, 2):
    I = input_lines[i]
    P = input_lines[i+1]

    res.append("Case #"+str(len(res)+1)+": ")

    
    def isPossibleToDelete(original, typed):
        if len(typed) < len(original): return (False, 0)

        charsToBeDeleted = 0
        mapOriginal = {}
        mapTyped = {}
        
        for i in range(len(original)):
            if original[i] in mapOriginal:
                mapOriginal[original[i]] += 1
            else:
                mapOriginal[original[i]] = 1

        for j in range(len(typed)):
            if typed[j] in mapTyped:
                mapTyped[typed[j]] += 1
            else:
                mapTyped[typed[j]] = 1
        
        for key in mapOriginal:
            if key in mapTyped:
                charsToBeDeleted += (mapTyped[key] - mapOriginal[key])
                if charsToBeDeleted < 0: return (False, 0)
            else: return (False, 0)

        if charsToBeDeleted == 0: return (False, 0)
        else: return (True, charsToBeDeleted)

    functionRes = isPossibleToDelete(I, P)

    if not functionRes[0]:
        res[-1] += "IMPOSSIBLE"
    else:
        res[-1] += str(functionRes[1])

for i in res:
    print(i)
