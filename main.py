import cv2
import numpy as np

drawing = False # true if mouse is pressed
ix,iy = -1,-1

# mouse callback function

def nothing(x):
    pass

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
                cv2.circle(img,(x,y),s,(b,g,r),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img,(x,y),s,(b,g,r),-1)


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cv2.namedWindow('video test')
img = np.zeros((480,640,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
cv2.setMouseCallback('video test',draw_circle)

# Create a black image, a window
img1 = np.zeros((1,512,3), np.uint8)
cv2.namedWindow('bars')

# create trackbars for color change
cv2.createTrackbar('R','bars',0,255,nothing)
cv2.createTrackbar('G','bars',0,255,nothing)
cv2.createTrackbar('B','bars',0,255,nothing)
cv2.createTrackbar('Size','bars',1,255,nothing)

cv2.moveWindow('video test',0,0)
cv2.moveWindow('image',640,0)
cv2.moveWindow('bars',320,530)

while(1):
    ret,im = cap.read()
    cv2.imshow('video test',im)
    cv2.imshow('bars',img1)
    r = cv2.getTrackbarPos('R','bars')
    g = cv2.getTrackbarPos('G','bars')
    b = cv2.getTrackbarPos('B','bars')
    s = cv2.getTrackbarPos('Size','bars')
    cv2.imshow('image',img)
    cv2.waitKey(3)
    img = np.zeros((480,640,3), np.uint8)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


