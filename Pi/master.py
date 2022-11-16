import numpy as np
from OLED.display import display
from ATTINY.sendi2c import elecSend
from ATTINY.sendSerial import receive
import time
from scipy.signal import find_peaks # need to import scipy
#insert send stim signal to attiny code
allData = [] # -> all data will be 6*len(addresses) columns
tempD = []
# loop
i = 0
addresses =[4]
#need to find how many electrodes are attached
# for address in addresses:
#     while i < 6: # ----> looping through all electrode pins
#         #send signal to module
#         elecSend(address, i)
#         time.sleep(1.667)
#         # receive 
#         tempD = receive(5) #receiving data for 5 seconds
#         allData.append(tempD)
#         tempD =[]
#         i+=1

#insert signal processing info
#variables
j = 0
data = receive(tempD)
print(len(data))
allData.append(data)
averages = [] # 6*len(addresses long)
indDisp = []
threshold = 750
#iterating through all columns in list
while j < len(allData):
    dSet = allData[j]
    temp = []
    editedData = np.convolve(dSet, np.ones(3)/3, mode='valid')
    thresData = editedData - threshold
    abval = abs(thresData)
    peaks,_ = find_peaks(abval,height = (0,900), distance = 26) #index of where peak is
    for peak in peaks:
        temp.append(thresData[peak])
    avg = np.average(temp)
    averages.append(avg)
    if (((j+1) %6) == 0):
        midline = np.argmin(averages[j-5:j])
        indDisp.append(midline) # -> should give minimum avg of peak avgs
    j+=1
print(averages)





    # minVal = min(thresData)
    # maxVal = max(thresData)
    # if (abs(maxVal) > abs(minVal)):
    #     #indicates that there are regular peaks
    #     peaks,_ = find_peaks(find_peaks(dSet))
    #     pHeight = dSet[peaks]
    #     avg = np.average(pHeight)
    #     averages.append(avg)
    # elif(abs(maxVal) < abs(minVal)):
    #     #indicates that peaks are inverted
    #     dSet = dSet * -1
    #     peaks,_ = find_peaks(find_peaks(dSet))
    #     pHeight = dSet[peaks]
    #     avg = np.average(pHeight)
    #     averages.append(avg)
    
#display midline
display(indDisp,len(addresses))