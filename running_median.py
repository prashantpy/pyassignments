#!/bin/python3

def findRunningMedian(a):
    
    a.sort()
    if len(a)%2 == 0 :
        x = ("{:.1f}".format((a[int(len(a)/2)] + a[int(len(a)/2) -1])/2 ))
        print(x)
    else:
        x = ("{:.1f}".format((a[int(len(a)/2)])))
        print(x)



if __name__ == '__main__':

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)
        findRunningMedian(a)
