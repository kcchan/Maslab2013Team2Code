print __doc__

import SimpleCV

display = SimpleCV.Display()
cam = SimpleCV.Camera()
normaldisplay = True

while display.isNotDone():
	
	if display.mouseRight:
		normaldisplay = not(normaldisplay)
		print "Display:", "normal" if normaldisplay else "segmented"
	img= cam.getImage().flipHorizontal()
	dist= img.colorDistance(SimpleCV.Color.BLACK).dilate(2)
	segmented= dist.stretch(225,255)
	blobs=segmented.findBlobs()
	if blobs:
		circles= blobs.filter([b.isCircle(0.2) for b in blobs])
		if circles:
			img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(),SimpleCV.Color.BLUE,3)
	if normaldisplay:
		img.show()
	else:
		segmented.show()
