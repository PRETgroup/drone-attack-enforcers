#############DEPENDENCIES#######################


from dronekit import connect, VehicleMode,LocationGlobalRelative,APIException
import time
import socket
# import exceptions
import math

##############FUNCTIONS##########################



##Function to arm the drone props and takeoff at targetHeight (m)


def arm_and_takeoff(targetHeight):

	while vehicle.is_armable!=True:
		print("Waiting for vehicle to become armable.")
		time.sleep(1)
	print("Vehicle is now armable")

	vehicle.mode = VehicleMode("GUIDED")

	while vehicle.mode!='GUIDED':
		print("Waiting for drone to enter GUIDED flight mode")
		time.sleep(1)
	print("Vehicle now in GUIDED MODE. Have fun!!")

	vehicle.armed = True
	while vehicle.armed==False:
		print("Waiting for vehicle to become armed.")
		time.sleep(1)
	print("Look out! Virtual props are spinning!!")

	vehicle.simple_takeoff(targetHeight)

	while True:
		print("Current Altitude: %d"%vehicle.location.global_relative_frame.alt)
		if vehicle.location.global_relative_frame.alt>=.95*targetHeight:
			break
		time.sleep(1)
	print("Target altitude reached!!")

	return None


############MAIN EXECUTABLE#############


####sim_vehicle.py opens up port on localhost:14550


vehicle = connect('127.0.0.1:14550',wait_ready=True)


####Arm the drone and takeoff into the air at 5 meters


arm_and_takeoff(5)
print("Vehicle reached target altitude")


####Once drone reaches target altitude, change mode to LAND 



vehicle.mode=VehicleMode('LAND')
while vehicle.mode!='LAND':
	print("Waiting for drone to enter LAND mode")
	time.sleep(1)
print("Vehicle now in LAND mode. Will touch ground shortly.")