import numpy as np

"""
Current set of functions are for use in integration problems.
Define equations by defining a function eq(var).

Variables start and end represent the range you want to analyze
on a function.  Subs represents how many sections you want to
divide the range into.
"""

def eq(var):
    return float(var)

def curveAreaMidPoint(start, end, subs):
    values = []
    xPoints = []
    intervalSize = float((end - start)/float(subs))
    #commented functions are for debugging
    #print intervalSize
    for i in range(subs + 1):
        xPoints.append((start + i * intervalSize))
        print(xPoints)
    for i in range(len(xPoints) - 1):
        values.append(eq((xPoints[i] + xPoints[i+1])/2))
    #print(values)
    return np.sum(values) * intervalSize

def curveAreaLeft(start, end, subs):
    values = []
    xPoints = []
    intervalSize = float((end - start)/float(subs))
    print(intervalSize)
    for i in range(subs):
        xPoints.append((start + i * intervalSize))
        print(xPoints)
    for i in range(len(xPoints)):
        values.append(eq(xPoints[i]))
    return np.sum(values) * intervalSize

def curveAreaRight(start, end, subs):
    values = []
    xPoints = []
    intervalSize = float((end - start)/float(subs))
    print(intervalSize)
    for i in range(1, subs + 1):
        xPoints.append((start + i * intervalSize))
        print(xPoints)
    for i in range(len(xPoints)):
        values.append(eq(xPoints[i]))
    return np.sum(values) * intervalSize
