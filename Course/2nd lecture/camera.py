# getting images fron the drone camera

from djitellopy import tello
import cv2 # CV library

drone = tello.Tello() # create an instance
drone.connect() # connection with the drone
print(drone.get_battery())

drone.streamon()

while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (320, 240))
    
    # show the image
    cv2.imshow("Image", img)

    # method to read the keyboards, send cmd and then display the next image
    cv2.waitKey(1)