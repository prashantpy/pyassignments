def findStockSpan(l):
    olist = []
    for i in range(0, len(l)):
        counter = i
        q = 1
        if i == 0:
                olist.append(1)
        else:
                while counter != 0:
                        if l[i] <= l[counter-1] and counter == i:
                                olist.append(1)
                                break
                        elif l[i] >= l[counter - 1]:
                                q = q + 1
                        else:
                                olist.append(q)
                                break
                        counter = counter - 1
    return olist

if __name__ == '__main__':

    #inputList = int(input())
    _inputList = [100, 80, 60, 70, 60, 75, 85]
    _anotherList =  [100, 60,70,65, 80, 85]

    _oList = findStockSpan(_inputList)
    print(_oList)

    _oList = findStockSpan(_anotherList)
    print(_oList)
