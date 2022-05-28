from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()   #getting all frames by turing stream on

while True:
    img = me.get_frame_read().frame #getting indiviual frames
    #img = cv2.resize(img,(360, 240))   #resizing the image for faster graphic processing

    cv2.imshow("Image", img)    #making a window to view image and giving object
    cv2.waitKey(1)     #giving a wait so that windows doesn't closes (imshow doesn't work without it)

