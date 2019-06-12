flag = False

def wordBreak(inputStr, inputDict, startIndex, lastIndex):
    sti = inputStr[startIndex : lastIndex]
    global flag
    for i in range(lastIndex, 0, -1):
        if flag != True:
            if sti[0:i] in inputDict:
                    if i == len(sti):
                        flag = True
                        return flag
                    sti = sti[i:len(sti)]
                    print("***********Calling recursion with : "+sti);
                    wordBreak(sti, inputDict, 0, len(sti))
    return flag

if __name__ == '__main__':

    #inputList = int(input())
    _inputDict =  { "i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
    _strToCheck =  "samsungandmango"
    _strToCheckTwo =  "ilikesamsung"
    print(wordBreak(_strToCheck, _inputDict, 0, len(_strToCheck)))
    print(wordBreak(_strToCheckTwo, _inputDict, 0, len(_strToCheckTwo)))
