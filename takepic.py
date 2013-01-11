import cv

cv.NamedWindow("w2", cv.CV_WINDOW_AUTOSIZE)
camera_index = 1
capture = cv.CaptureFromCAM(camera_index)

while True:
    frame = cv.QueryFrame(capture)

    cv.ShowImage("w2", frame) 
    c = cv.WaitKey(10)
    if c == 32:
	cv.SaveImage("test.JPG", frame)
        break
    
	
