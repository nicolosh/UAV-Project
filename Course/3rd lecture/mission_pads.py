# to COMPLETE
from djitellopy import Tello

# create and connect

tello = Tello()
tello.connect()

# configure drone

tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2)  # both directions (FW and BW)

tello.takeoff()

# retrieve the ID of the pad RF
pad = tello.get_mission_pad_id()


'''
batteryLevel = tello.get_battery()


flag = False
vectorDist = []

# detect and react to pads until we see pad #3 and the battery level is less than 20% 
while pad != 3:
  if pad == 2:
    tello.get_current_state()
    tello.move_back(30)
    tello.rotate_clockwise(90)

  if pad == 4:
    tello.move_up(30)
    tello.flip_forward()
  
  distX = tello.get_mission_pad_distance_x
  distY = tello.get_mission_pad_distance_y
  distZ = tello.get_mission_pad_distance_z

  distFromPAD = distance(distX, distY, distZ)

  vectorDist.append(distFromPAD)
  
while pad != 2:



  if batteryLevel < 20 & distFromPAD: # less than 20%
    flag = True



# graceful termination
tello.disable_mission_pads()
tello.land()
tello.end()
'''
