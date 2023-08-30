# front camera to capture some images (the basic movements of the drone) and we will use our keyboard to move the drone
from djitellopy import tello
from time import sleep



print("Create Tello object")
drone = tello.Tello() #instance of the drone
print("Connect to Tello Drone")
drone.connect() # connecting to the drone

#ToF cameras can be used to avoid obstacles

print(drone.get_battery()) # get the charge status of the drone battery
#print(f"Battery Life Pecentage: {tello.get_battery()}")

drone.takeoff()

# Go forward / backward
drone.send_rc_control(0, 10, 0, 0)

# go right / left
drone.send_rc_control(10, 0, 0, 0)

#rotate CW/ CCW
drone.send_rc_control(0, 0, 0, 10) # inputs are velocities (angular or linear)
# drone.get_current_state() # flight controller or DJI estimates its own state

# Go up / down
drone.send_rc_control(0, 0, 10, 0)

sleep(1) # wait some time

# Stop 
drone.send_rc_control(0, 0, 0, 0)

# Land manouvre
drone.land()