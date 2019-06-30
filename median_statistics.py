import statistics

def findRunningMedian(a):
    
    for i in range(1,len(a)+1):
        lst = a[0:i]
        print(statistics.median(map(float,lst)))



if __name__ == '__main__':

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)
    findRunningMedian(a)
