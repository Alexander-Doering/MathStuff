import numpy as np
import matplotlib.pyplot as plt
import string
import time
timestart=time.time()
alpha_dict = dict(enumerate(string.ascii_letters))
#n=10 for tests PointInput =  np.array([[50,50],[-30,40],[70,-20],[-60,-30],[10,24],[25,-20],[-30,35],[-5,-13],[-40,-12],[12,30]])
#n=52 (Currently limited by the alpha_dict size )
PointInput = np.array([[160,828],[243,988],[-573,829],[-166,504],[-860,991],[-911,-572],[-330,399],[524,965],[-792,274],[-508,124],[766,966],[-375,482],[550,904],[-657,744],[-154,662],[-373,765],[-677,-428],[839,864],[-626,-17],[58,568],[-967,-538],[-342,295],[-810,-585],[-441,948],[675,704],[-745,-280],[100,808],[-495,-46],[-823,574],[-597,668],[411,603],[-410,211],[-489,861],[-738,-661],[-71,414],[792,946],[-981,-458],[34,72],[-601,331],[503,807],[-298,-280],[-766,612],[466,849],[110,956],[93,950],[-84,54],[-841,-415],[-32,945],[330,976],[594,619],[-769,-621],[-694,866]])

# Defines which part of the Coordinate System the points are in, used for relation.
#TODO: Allow x,y=0 and add calc for that
def CoordinateQuarter(x,y):
    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0: 
        return 2
    elif x < 0 and y > 0:
        return 4
    elif x < 0 and y < 0:
        return 3
# Draw Line between 2 Points.
def DrawConnection(x1,y1,x2,y2):
    plt.plot([x1,x2],[y1,y2],'k-')

# Plot Points & Assign Alphabetical Name to them for further Use
def PointPlotter(PointArray):
    PointList = dict()
    count=0
    for e in PointArray: 
        plt.plot(e[0],e[1], 'o')
        name=alpha_dict[count]
        PointList[name]=[e[0],e[1]]
        plt.annotate(name, (e[0],e[1]))
        count=count+1
    return(PointList)
        
# Connect all Points:
def Connector(Dictionary):
    for a in Dictionary:
        x = Dictionary[a][0]
        y = Dictionary[a][1]
        for b in Dictionary:
            if(a == b):
                continue
            else:
                x2 = Dictionary[b][0]
                y2 = Dictionary[b][1]
                DrawConnection(x,y,x2,y2)
# Takes 3 Tuples and Computes function of the first two, and related the third to it
def functionRelation(p1,p2,p3):
    dx = p1[0]-p2[0]
    dy = p1[1]-p2[1]
    #Straight Line Check
    if dx != 0 and dy != 0:
        b = -(dy/dx * p1[0] - p1[1])
        fy = dy/dx * p3[0] + b
    else: #This means its a straight line.
        if dx == 0: #Straight Line where all y are in val. You can now calculate it directly
            if p3[0] > p1[0]:
                rel=-1
            elif p3[0] < p1[0]:
                rel=1
            else: 
                print("Stopping Now. Point:"+ p3 , +" is not linearly independant")
                return 0
            if p2[1] > p1[1]:
                return (rel*-1)
            else:
                return(rel)
        else: # This means it's a straight line paralel to the x-axis
            if p3[1] > p1[1]:
                rel=-1
            elif p3[1] < p1[1]:
                rel=1
            else:
                print("Stopping Now. Point:"+ p3 , +" is not linearly independant")
                return 0
            if p2[0] > p1[0]:
                return(rel*-1)
            else:
                return(rel)
    if fy > p3[1]:
        rel= -1
    elif fy == p3[1]:
        print("Stopping Now. Point:"+ p3 , +" is not linearly independant")
        return 0
    else:
        rel = 1
    # Makes the middle point of between p1 & p2 the middle of the coordinate system
    mx=(p1[0]+p2[0])/2
    my=(p1[1]+p2[1])/2
    # Defines which part of the Coordinate System the points are in 
    p1q = CoordinateQuarter(p1[0]-mx, p1[1]-my)
    p2q = CoordinateQuarter(p2[0]-mx, p2[1]-my)
    if ((p1q == 1 and p2q == 3) or (p1q == 2 and p2q == 4)):
        return(rel)
    elif ((p1q == 3 and p2q == 1) or (p1q == 4 and p2q == 2)):
        return(rel*-1)
    else:
        print(" Coord System Error, you done fucked up")
        print(p1,p2)
        print(mx,my)
        print((p1[0]-mx, p1[1]-my),(p2[0]-mx, p2[1]-my))
        print(p1q,p2q)
        exit(3)
   
def RelationGenerator(Dictionary):
    rellist=dict()
    for a in Dictionary:
        for b in Dictionary:
            if(a == b):
                continue
            else:
                for c in Dictionary:
                    if a == c or b == c:
                        continue
                    val=functionRelation(Dictionary[a],Dictionary[b],Dictionary[c])
                    rellist[a,b,c]=val
    return rellist

PList=PointPlotter(PointInput)
Connector(PList)
RList=RelationGenerator(PList)
#print("Ergebnis:")
#print(RList)
#TODO: Generate Tables for each Point {P_n:(a:(-1),b:(0),c:(1))}
print("Menge an ergebnissen:", len(RList) )
timeend=time.time()
print(timeend-timestart)
plt.show()