from PIL import Image
import numpy as np
from numba import jit


def median(NPimg, NPnewImg,width,height):
	one = np.zeros((height, width), int)
	two = np.zeros((height, width), int)
	three = np.zeros((height, width), int)
	four = np.zeros((height, width), int)
	five = np.zeros((height, width), int)
	six = np.zeros((height, width), int)
	seven = np.zeros((height, width), int)
	eight = np.zeros((height, width), int)
	nine = np.zeros((height, width), int)
	one[1: - 1, 1: -1] = NPimg[0 : -2	, 0: -2]
	two[1: - 1, 1: -1] = NPimg[0 : -2	,1:-1]
	three[1: - 1, 1: -1] = NPimg[0 : -2, 2: ]
	four[1: - 1, 1: -1] = NPimg[1 : -1	, 0: -2]
	five = NPimg
	six[1: - 1, 1: -1] = NPimg[1 : -1, 2: ]
	seven[1: - 1, 1: -1] = NPimg[2:		, 0: -2]
	eight[1: - 1, 1: -1] = NPimg[2:		, 1:-1]
	nine[1: - 1, 1: -1] = NPimg[2:	, 2: ]
	X = np.dstack((one, two, three, four, five, six, seven,eight,nine))
	NPnewImg = np.median(X,2)
	NPnewImg = NPnewImg.astype('uint8')
	return NPnewImg

def getMedian(NPimg,NPnewImg,width,height):
	R = (1,0,0) * NPimg
	G = (0,1,0) * NPimg
	B = (0,0,1) * NPimg
	R2 = np.sum(R, axis = 2)
	G2 = np.sum(G, axis = 2)
	B2 = np.sum(B, axis = 2)
	R3 = np.asarray(R2,dtype='int64')
	G3 = np.asarray(G2,dtype='int64')
	B3 = np.asarray(B2,dtype='int64')
	R3 = median(R2,R3,width,height)
	G3 = median(G2,G3,width,height)
	B3 = median(B2,B3,width,height)
	RGB = np.dstack((R3,G3,B3))
	NPnewImg = np.asarray(RGB,dtype='int64')
	return NPnewImg
	#RGBI = Image.fromarray(RGB.astype('uint8'))
	#RGBI.save('out12.jpg')		
			
path = "obrazek.JPG" 
img = Image.open(path)
members = [(0,0)] * 9
width, height = img.size
newimg = Image.new("RGB",(width,height),"white")
NPimg = np.asarray(img)
NPmed = np.asarray(newimg)
NPmed.setflags(write=1)

NPmed = getMedian(NPimg,NPmed,width,height)
	
NPimg2 = NPimg.astype('int64')
NPmed2 = NPmed.astype('int64')
Mask = NPimg2 - NPmed2
#Mask = Mask + 255
Mask[Mask < 0 ] = 0
NPresult = NPimg2 + Mask
NPresult[NPresult > 255 ] = 255
medianIMG = Image.fromarray(NPresult.astype('uint8'))
medianIMG.save('obrazek2.jpg')