# Creation of a script to read cmds from the keyboard controlling the Tello drone

# import module for tello
from djitellopy import tello

# import the previous keyboard input module file from the first step:
import keyboardTelloModule as kp

# import module for time:
import time

from time import sleep

# Import opencv python module
import cv2

# Global variable
global img

def getKeyboardInput():
    #LEFT RIGHT, FRONT BACK, UP DOWN, YAW VELOCITY
    lr, fb, ud, yv = 0, 0, 0, 0 
    # setting std speeds for the drone
    speed = 30
    liftSpeed = 40
    moveSpeed = 45
    rotationalSpeed = 20

    # BASIC CONTROL for left and right motion
    if kp.getKey("LEFT"):
        lr = - speed # LEFT
    elif kp.getKey("RIGHT"):
        lr = speed # right

    # Controlling The Front And Back Motion
    if kp.getKey("UP"):
      fb = moveSpeed
    elif kp.getKey("DOWN"):
      fb = - moveSpeed

    # Controlling The Up And Down Motion
    if kp.getKey("w"):
      ud = liftSpeed
    elif kp.getKey("s"):
      ud = - liftSpeed
    
    # Controlling the rotation
    if kp.getKey("a"): # YAW CW
      yv = - rotationalSpeed
    elif kp.getKey("d"): # YAW CCW
      yv = rotationalSpeed

    if kp.getKey("q"): # Land
      drone.land()
    elif kp.getKey("e"): # Takeoff
       drone.takeoff()

    return [lr, fb, ud, yv] # Return the given Value

# Initialize Keyboard Input
kp.init() # to read from keyboard

# Start connecting with the drone
drone = tello.Tello()
drone.connect()

# Get Battery Info
print(drone.get_battery())

while True:
  # Get The Return Value And Stored It On Variable
  keyValues = getKeyboardInput()

  # control The Drone
  drone.send_rc_control(keyValues[0],keyValues[1],keyValues[2],keyValues[3]) 
  