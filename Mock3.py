#This is the code we run for Mock Competition 3
#It calls cruiseControl

#Headers
from threading import Timer
import cv
import thread
import sys
sys.path.append("../..")
import time
import arduino



#Camera part in code
#cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow("w1")
camera_index = 1
capture = cv.CaptureFromCAM(camera_index)

try:
    waitingForSignal = True
    while waitingForSignal:
        print(d2.getValue())
        if (d2.getValue()==0):
            Timer(170, timeout).start() #kills program in 2 minutes 50 seconds (170 seconds) 
            main()
            waitingForSignal = False
        else:
            time.sleep(0.020)

except:
    m0.setSpeed(0)
    m1.setSpeed(0)
    print("Exception: time's up?")

print("Program exited before time's uo")

def main(self):
    while True:

        c = cv.WaitKey(10)
        if c == 32: #ASCII number of spacebar
            m0.setSpeed(0)
            m1.setSpeed(0)
            print("Space pressed...stop engaged")
            break #exit "main" while loop

        bgrFrame = acquireSmoothFrame()
        hsvFrame = convert2HSV(bgrFrame)
        thresholded_grayscale_img = colorFilter(hsvFrame, green)
    
    
        #determine the objects moments 
        #and check that the area is large enough to be our object
        mat=cv.GetMat(thresholded_grayscale_img); 
        moments = cv.Moments(mat, 0) 
        area = cv.GetCentralMoment(moments, 0, 0) 
    
        #there can be noise in the video so ignore objects with small areas 
        if(area > 100000): 
            x = xCenter(moments)
            y = yCenter(moments)
            changeTrajectory(x)
            print(x)
            addTrackingPoint(x, y)
        
            #display the image  
        else: #First the robot keeps on rotating
            m0.setSpeed(50)
            m1.setSpeed(-40)
        
        cv.ShowImage("Ball Tracker",bgrFrame) 

def timeout():
    thread.interrupt_main()

def acquireSmoothFrame(self):
    outFrame = cv.QueryFrame(capture) #picks up a frame from camera
    cv.Smooth(bgrFrame, outFrame, cv.CV_BLUR, 10) #smooths out the frame
    return outFrame

def convert2HSV(self, bFrame):
    hFrame = cv.CreateImage(cv.GetSize(bFrame), 8, 3)
    cv.CvtColor(bFrame, hFrame, cv.CV_BGR2HSV)
    return hFrame

def colorFilter(self, inFrame, col):
    outFrame= cv.CreateImage(cv.GetSize(inFrame), 8, 1) #creates blank image having same size as inFrame but 8-bit and 1-channel
    if col == red:
        lowBound = (0,40,100)
        highBound = (10,255,255)
    elif col == green:
        lowBound = (60,40,100)
        highBound = (80,255,255)
    cv.InRangeS(inFrame, lowBound, highBound, outFrame)
    return outFrame

def xCenter(self, mom):
    #determine the x and y coordinates of the center of the object we are tracking 
    #by dividing the 1, 0 and 0, 1 moments by the area 
    xC = cv.GetSpatialMoment(mom, 1, 0)/area 
    #yC = cv.GetSpatialMoment(mom, 0, 1)/area 
    #l = int(xC);
    #m = int(yC);
    return int(xC)

def changeTrajectory(self, l):
    if (l < 120): #far left
        m0.setSpeed(-25)
        m1.setSpeed(-60)
    elif ((l >= 120) and (l < 240)): #left
        m0.setSpeed(-25)
        m1.setSpeed(-30)
    elif ((l > 240) and (l < 400)): #straight
        m0.setSpeed(-25)
        m1.setSpeed(-25)
    elif ((l >= 400) and (l < 520)): #right
        m0.setSpeed(-40)
        m1.setSpeed(-25)
    else: #far right
        m0.setSpeed(-60)
        m1.setSpeed(-25)

def addTrackingPoint(inFrame, xLoc, yLoc):
    overlay = cv.CreateImage(cv.GetSize(inFrame), 8, 3)    
    cv.Circle(overlay, (xLoc, yLoc), 2, (255, 255, 255), 20, 8, 0) 
    cv.Add(inFrame, overlay, inFrame)
    #add the thresholded image back to the img so we can see what was 
    #left after it was applied 
    cv.Merge(thresholded_grayscale_img, None, None, None, bgrFrame) 