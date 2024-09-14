import numpy as np
import matplotlib.pyplot as plt
import string
import time
import math
timestart=time.time()
alpha_dict = dict(enumerate(string.ascii_uppercase))
PointInput =  np.array([[50,50],[-30,40],[70,-20],[-60,-30],[30,-10],[-34,-10]])
# Unit Vector Function
def unitvec(vec1):
    return vec1/np.linalg.norm(vec1)

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
                print(x,y,x2,y2)
                DrawConnection(x,y,x2,y2)
# Calculate Angle between 2 Vectors    
def AngleCalc(vec1,vec2):
    return np.arccos(np.clip(np.dot(unitvec(vec1),unitvec(vec2)), -1.0,1.0))

# Generates Vectors for Each point to each point.
def genVectors(Dictionary):
    VecList=dict()
    for a in Dictionary:   
        v1 = Dictionary[a]
        for b in Dictionary:
            if a == b: continue
            else:
                v2 = Dictionary[b]
                name=a+b
                VecList[name]=[v1[0]-v2[0],v1[1]-v2[1]]
    return(VecList)

# Generate all Angles for every possible pair of vectors except XY <-> YX
def genAngles(Dictionary):
    angleList=dict()
    for a in Dictionary:   
        point1=a[:1]
        point2=a[1:2]
        for b in Dictionary:
            if a==b: continue
            elif a[:1] != b[:1]: continue
            else:
                point3=b[1:2]
                angle=round((AngleCalc(Dictionary[a],Dictionary[b])/math.pi)*180,2)
                name=a+"->"+b     
                print(name, " Angle: ",  angle,"°")
     
PList=PointPlotter(PointInput)
Connector(PList)
VList=genVectors(PList)
genAngles(VList)
timeend=time.time()
print(timeend-timestart)
plt.show()
