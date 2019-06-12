person_community = []

def findCommunitySize(person):
    return len(findCommunity(person))

def findCommunity(person):
    community = []
    global person_community
    for i in range(0, len(person_community)):
        if person_community[i] == person_community[person]:
           community.append(i)
    return community

def mergeCommunity(_personOne, _personTwo):
    global person_community
    if person_community[_personOne] == person_community[_personTwo]:
        return
    comm1 = findCommunity(_personOne)
    comm2 = findCommunity(_personTwo)

    if len(comm1) == 0 or len(comm2) == 0 :
        return
    commId = person_community[comm1[0]]
    for i in comm2:        
        person_community[i] = commId
    print(person_community) 
    
if __name__ == '__main__':

     
     inputVal = input()
     splitInputVal = inputVal.split(" ")
     for i in range(0,int(splitInputVal[0]) + 1):
         person_community.append(i)
     for j in range(0, int(splitInputVal[1])):
         _getInput = input().split(" ")
         print(_getInput)
         if(_getInput[0] == "M"):
            mergeCommunity(int(_getInput[1]), int(_getInput[2]))
         elif(_getInput[0] == 'Q'):
            print(findCommunitySize(int(_getInput[1])))
                  
