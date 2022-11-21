import csv
from scipy.signal import find_peaks
#python -m pip install scipy
import numpy as np
import matplotlib.pyplot as plt
 
# open the file in read mode
filename = open('SpinalCordSampleData.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
left = []
right = []
middle = []
 
# iterating over each row and append
# values to empty list
i = 0
for col in file:
    if(i < 531):
        left.append(int(col['left']))
        right.append(int(col['right']))
        middle.append(int(col['midline']))
    else:
        break
    i+=1

# print(len(left))
# print(left)
# print(len(right))

allData = []
allData.append(left)
allData.append(right)
allData.append(middle)
print(len(allData))

def sigprocess(data:list, thresh: 750)->list:

    averages = []
    j = 0 
    x = [x for x in range(len(left))]
    indDisp = []
    adj = []
    while j < len(data):
        dSet = data[j]
        dSet = dSet[1:]
        dSet = [int(x) for x in dSet]
        #dSet = int(dSet)
        temp = []
        editedData = np.convolve(dSet, np.ones(3)/3, mode='valid')

        thresData = editedData - thresh

        abval = abs(thresData)

        peaks,_ = find_peaks(abval,height = (7,100), distance = 26) #index of where peak is
        if len(peaks) != 0:
            for peak in peaks:
                temp.append(thresData[peak])
                print(thresData[peak])
        else:
            temp.append(0)
        # plt.plot(thresData)
        # plt.plot(peaks,thresData[peaks],"x")
        # plt.show()
        # plt.close()
        avg = np.average(temp)
        averages.append(avg)
        if (((j+1)%6) == 0):
            print(averages)
            lowest = np.argmin(np.abs(averages[j-4:j]))+1 #should be j-5,j+1m, without +1
            indDisp.append(lowest)
            #if lowest number is positive
            if(averages[lowest] >0):
                #if lowest index == 0
                if (lowest == 0):
                    #if adjacent index is neg
                    if (averages[lowest+1]<0):
                        #add it to adjacent list
                        adj.append(lowest+1)
                    else:
                        #else add lowest to adjacent list
                        adj.append(lowest)
                #if lowest index == 5
                elif (lowest == 5):
                    #if adjacent index is neg
                    if (averages[lowest-1]<0):
                        #add it to adjacent list
                        adj.append(lowest+1)
                    else:
                        #else add lowest to adjacent list
                        adj.append(lowest)
                #for all middle numbers, check both sides
                else: 
                    if (averages[lowest-1]<0):
                        adj.append(lowest-1)
                    elif(averages[lowest+1]<0):
                        adj.append(lowest+1)
                    else:
                        adj.append(lowest)
            #checking if lowest value produces neg number
            elif(averages[lowest] <0):
                if (lowest == 0):
                    #if adjacent index is neg
                    if (averages[lowest+1]>0):
                        #add it to adjacent list
                        adj.append(lowest+1)
                    else:
                        #else add lowest to adjacent list
                        adj.append(lowest)
                #if lowest index == 5
                elif (lowest == 5):
                    #if adjacent index is neg
                    if (averages[lowest-1]>0):
                        #add it to adjacent list
                        adj.append(lowest+1)
                    else:
                        #else add lowest to adjacent list
                        adj.append(lowest)
                else:
                    if (averages[lowest-1]>0):
                        adj.append(lowest-1)
                    elif(averages[lowest+1]>0):
                        adj.append(lowest+1)
                    else:
                        adj.append(lowest)
             # -> should give minimum avg of peak avgs
        j+=1
    # print(averages)

    print(indDisp)
    return [indDisp,adj]
# print(peaks)


def sigdebug(data:list, thresh: 750)->list:
    j=0
    d= []
    while j < len(data):
        dSet = data[j]
        dSet = dSet[1:]
        dSet = [int(x) for x in dSet]
        #dSet = int(dSet)
        d.extend(dSet)
        temp = []
        j+=1
    editedData = np.convolve(d, np.ones(3)/3, mode='valid')

    thresData = editedData -thresh
    abval = abs(thresData)
    peaks,_ = find_peaks(abval,height = (7,100), distance = 26) #index of where peak is
    print(type(peaks))
    print(peaks)
    print(type(d))
    # peaks = np.array([int(y) for y in peaks])
    thresData = np.asarray(thresData)
    
    
    return [thresData,peaks]