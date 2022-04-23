
def Solution():
    n = int(input())
    for i in range(n):
        currNum = int(input())

        possibleCombos = []
        sumCurrNum = sum([int(j) for j in str(currNum)])
        

        for k in range(len(str(currNum))):
            for j in range(10):
                strCurrNum = str(currNum)
                if int(strCurrNum + str(j)) % 9 == 0:
                    possibleCombos.append(int(strCurrNum + str(j)))
            for j in range(1, 10):
                strCurrNum = str(currNum)
                if int(str(j) + strCurrNum) % 9 == 0:
                    possibleCombos.append(int(str(j) + strCurrNum))

        print("Case #{}: {}".format(i+1, min(possibleCombos)))

Solution()