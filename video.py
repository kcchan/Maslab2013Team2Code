import cv

cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 1
capture = cv.CaptureFromCAM(camera_index)

while True:
    frame = cv.QueryFrame(capture)

    hsv_img = cv.CreateImage(cv.GetSize(frame), 8, 3)
    thresholded_img= cv.CreateImage(cv.GetSize(hsv_img), 8, 1)
    cv.CvtColor(frame, hsv_img, cv.CV_BGR2HSV)
    #v.InRangeS(hsv_img, (0,100,100), (25,255,120), thresholded_img)
    cv.InRangeS(hsv_img, (0,200,100), (25,255,255), thresholded_img)
    
    
    cv.ShowImage("w1", thresholded_img)
    c = cv.WaitKey(10)
    if c == 27:
	break
    

    
