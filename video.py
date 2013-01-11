import cv

#cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow("w1")
camera_index = 1
capture = cv.CaptureFromCAM(camera_index)

while True:
    frame = cv.QueryFrame(capture)

    #hsv_img = cv.CreateImage(cv.GetSize(frame), 8, 3)
    #thresholded_img= cv.CreateImage(cv.GetSize(hsv_img), 8, 1)
    #cv.CvtColor(frame, hsv_img, cv.CV_BGR2HSV)
    #v.InRangeS(hsv_img, (0,100,100), (25,255,120), thresholded_img)
    #cv.InRangeS(hsv_img, (0,200,100), (25,255,255), thresholded_img)
    
    cv.Smooth(frame, frame, cv.CV_BLUR, 10)	

    hsv_img = cv.CreateImage(cv.GetSize(frame), 8, 3)
    cv.CvtColor(frame, hsv_img, cv.CV_BGR2HSV)
    
    thresholded_img= cv.CreateImage(cv.GetSize(hsv_img), 8, 1)
    cv.InRangeS(hsv_img, (120,80,80), (140,255,255), thresholded_img)
    

#determine the objects moments and check that the area is large  
            #enough to be our object
    mat=cv.GetMat(thresholded_img); 
    moments = cv.Moments(mat, 0) 
    area = cv.GetCentralMoment(moments, 0, 0) 
            
            #there can be noise in the video so ignore objects with small areas 
    if(area > 100000): 
                #determine the x and y coordinates of the center of the object 
                #we are tracking by dividing the 1, 0 and 0, 1 moments by the area 

                x = cv.GetSpatialMoment(moments, 1, 0)/area 
                y = cv.GetSpatialMoment(moments, 0, 1)/area 
                l=int(x);
                m=int(y);
                #print 'x: ' + str(x) + ' y: ' + str(y) + ' area: ' + str(area) 
                
                #create an overlay to mark the center of the tracked object 
                overlay = cv.CreateImage(cv.GetSize(frame), 8, 3) 
                
                cv.Circle(overlay, (l,m), 2, (255, 255, 255), 20, 8, 0) 
                cv.Add(frame, overlay, frame) 
                #add the thresholded image back to the img so we can see what was  
                #left after it was applied 
                cv.Merge(thresholded_img, None, None, None, frame) 
                #display the image  
    cv.ShowImage("w1",frame) 
            
    
    c = cv.WaitKey(10)
    if c == 27:
	break
    

    
