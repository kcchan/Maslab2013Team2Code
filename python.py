import cv2;
import cv;
cv.NamedWindow("preview")
vc = cv2.VideoCapture(1)

if vc.isOpened():
	rval, frame = vc.read()
else:
	rval=False

#grey=cv.fromarray(cv.CreateImage(cv.GetSize(frame),8,3));
#cv.CvtColor(frame,grey,cv.CV_BGR2GRAY);

while rval:
	cv2.imshow("preview",frame)
	rval, frame = vc.read()
	key = cv2.waitKey(20)
	if key == 27:
		break

