import copy
arrOfBuilding = [[[4,0],[4,-5],[7,-5],[7,0]]]
# arrOfBuilding = [[[4,0],[4,-5],[7,-5],[7,0]],[[0,-2],[0,-5],[2,-5],[2,-2]]]
arrOfSun = [-3,1]
visibleArea = -1
buildingPoints = []

print("number of building is/are: ",len(arrOfBuilding))

# functions for the use

def comp(list1, list2):
    for val in list1:
        if val in list2:
            return True
    return False

def line(p1,p2):
    temp1 = copy.deepcopy(p1)
    temp2 = copy.deepcopy(p2)
    while(temp1 != temp2):
        if(temp1[0] > temp2[0]):#temp1 temp2 x comparison
            temp1[0] = temp1[0] - 1
        if(temp1[0] < temp2[0]):
            temp1[0] = temp1[0] + 1
        if(temp1[1] > temp2[1]):#temp1 temp2 y comparison
            temp1[1] = temp1[1] - 1
        if(temp1[1] < temp2[1]):
            temp1[1] = temp1[1] + 1
        if([temp1[0],temp1[1]] not in buildingPoints):
            buildingPoints.append([temp1[0],temp1[1]])
def lineReturnmiddlepoints(p1,p2):
    temp1 = copy.deepcopy(p1)
    temp2 = copy.deepcopy(p2)
    midPoints = []
    while(temp1 != temp2):
        if(temp1[0] > temp2[0]):#temp1 temp2 x comparison
            temp1[0] = temp1[0] - 1
        if(temp1[0] < temp2[0]):
            temp1[0] = temp1[0] + 1
        if(temp1[1] > temp2[1]):#temp1 temp2 y comparison
            temp1[1] = temp1[1] - 1
        if(temp1[1] < temp2[1]):
            temp1[1] = temp1[1] + 1
        midPoints.append([temp1[0],temp1[1]])
    return midPoints


# driver code

# for buildingcount in range(len(arrOfBuilding)):
for buildingCount in range(len(arrOfBuilding)):
    p1 = copy.deepcopy(arrOfBuilding[buildingCount][0])
    p2 = copy.deepcopy(arrOfBuilding[buildingCount][1])
    p3 = copy.deepcopy(arrOfBuilding[buildingCount][2])
    p4 = copy.deepcopy(arrOfBuilding[buildingCount][3])


    # print(p1,p2,p3,p4)
    # p1 -> p2, p1 -> p4
    # p2 -> p3, p2 -> p1
    # p3 -> p2, p3 -> p4
    # p4 -> p1, p4 -> p3

    line(p1,p2)
    line(p1,p4)
    line(p2,p2)
    line(p3,p4)

    if(p1 not in buildingPoints):
        buildingPoints.append([p1[0],p1[1]])
    if(p2 not in buildingPoints):
        buildingPoints.append([p2[0],p2[1]])
    if(p3 not in buildingPoints):
        buildingPoints.append([p3[0],p3[1]])
    if(p4 not in buildingPoints):
        buildingPoints.append([p4[0],p4[1]])

    #we get all the points in the building

    for i in buildingPoints:
        tempPoints = lineReturnmiddlepoints(i,arrOfSun)
        if(comp(buildingPoints,tempPoints) == False):
            visibleArea += 1
            print(i," : ",visibleArea," : ",tempPoints," : ",i not in tempPoints)


    print(visibleArea)
            

