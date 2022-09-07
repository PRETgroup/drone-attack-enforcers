#############DEPENDENCIES#######################
from dronekit import connect, VehicleMode,LocationGlobalRelative,APIException
import time
import socket
import math
from time import asctime, localtime
from logs.logger import DroneStatusLogger

class Mission:
	vehicle = None

	def __init__(self):
		return 

	def _notify(self, msg):
		print("DRONEKIT: " + str(msg))

	def connect(self):
		####sim_vehicle.py opens up port on localhost:14550
		self._notify('Connecting...')
		self.vehicle = connect('127.0.0.1:14550',wait_ready=True)
		self._notify('Connected!')

	def configure(self, targetAltitude):
		self.targetAltitude = targetAltitude

	##Function to arm the drone props and takeoff at targetHeight (m)
	def _arm_and_takeoff(self, vehicle, targetHeight):

		while vehicle.is_armable!=True:
			self._notify("Waiting for vehicle to become armable.")
			time.sleep(1)
		self._notify("Vehicle is now armable")

		vehicle.mode = VehicleMode("GUIDED")

		while vehicle.mode!='GUIDED':
			self._notify("Waiting for drone to enter GUIDED flight mode")
			time.sleep(1)
		self._notify("Vehicle now in GUIDED MODE. Have fun!!")

		vehicle.armed = True
		while vehicle.armed==False:
			self._notify("Waiting for vehicle to become armed.")
			time.sleep(1)
		self._notify("Look out! Virtual props are spinning!!")

		vehicle.simple_takeoff(targetHeight)

		return None

	## Determine if at the target altitude
	def atAltitude(self):
		self._notify("Current Altitude: %d"%self.vehicle.location.global_relative_frame.alt)
		if self.vehicle.location.global_relative_frame.alt>=.95*self.targetAltitude:
			self._notify("Target altitude reached!!")
			return True
		else:
			return False

	## Take off
	def take_off(self):
		####Arm the drone and takeoff into the air at target altitude
		self._arm_and_takeoff(self.vehicle, self.targetAltitude)
		self._notify("Vehicle reached target altitude")
		return True

	## Land
	def begin_Landing(self):
		####Change mode to LAND 
		self.vehicle.mode=VehicleMode('LAND')
		# while self.vehicle.mode!='LAND':
		# 	self._notify("Waiting for drone to enter LAND mode")
		# 	time.sleep(1)
		# self._notify("Vehicle now in LAND mode. Will touch ground shortly.")
		# while not self.hasLanded():
			# time.sleep(1)
		return True

	def hasLanded(self):
		self._notify("Current Altitude: %d"%self.vehicle.location.global_relative_frame.alt)
		if self.vehicle.location.global_relative_frame.alt>=1:
			return False
		else:
			return True

	def getStatus(self):
		return {
			"lat": self.vehicle.location.global_frame.lat,
			"lon": self.vehicle.location.global_frame.lon,
			"alt": self.vehicle.location.global_frame.alt
		}

class Manager:
	def __init__(self, pipe_c, log=False):
		self.pipe = pipe_c
		self.l = "L_DISCONNECT"
		self.log = log
		if log:
			self.logger = DroneStatusLogger("TOAL")

	def _notify(self, msg):
		print("MANAGER: " + str(msg))
	
	def run(self, a):
		mission = None

		req_exit = False
		while not req_exit:

			# Logging
			if mission is not None and self.log:
				a = mission.getStatus()
				self.logger.log(a["lat"], a["lon"], a["alt"])

			if self.pipe.poll():
				request = self.pipe.recv()
				self._notify("Request from base: " + str(request))
			else:
				request = [None, ""]

			curLoc = self.l

			# Output & Transition Logic
			if self.l == "L_DISCONNECT":
				if request[1] == "NEW":
					self._notify("Initiate new mission")
					mission = Mission()
					mission.connect()

					self.l = "L_CONNECTED" # Connect is blocking so we know it will be connected
					self.pipe.send([asctime(localtime()), "CONNECTED"])

				elif request[1] == "END":
					self.pipe.send([asctime(localtime()), "END"])
					req_exit = True

				elif request[1] == "ABORT":
					self.pipe.send([asctime(localtime()), "END"])
					req_exit = True

			if self.l == "L_CONNECTED":
				if request[1] == "CONFIG_ALT":
					try:
						mission.configure(int(request[2]))
						self.pipe.send([asctime(localtime()), "CONFIGED"])
						self.l = "L_CONFIGED"
					except:
						self._notify("Invalid config. Waiting for new config")

				elif request[1] == "END":
					self.pipe.send([asctime(localtime()), "END"])
					req_exit = True
					
				elif request[1] == "ABORT":
					self.l = "L_DISCONNECT"
					self._notify("Abort.")
					self.pipe.send([asctime(localtime()), "END"])

			if self.l == "L_CONFIGED":
				if request[1] == "RUN":
					mission.take_off()
					self.l = "L_TAKEOFF"
					self._notify("Take Off")
					self.pipe.send([asctime(localtime()), "TAKE_OFF"])

				elif request[1] == "END":
					self.l = "L_DISCONNECT"
					self._notify("End mission")
					self.pipe.send([asctime(localtime()), "END"])

				elif request[1] == "ABORT":
					self.l = "L_DISCONNECT"
					self._notify("Abort.")
					self.pipe.send([asctime(localtime()), "END"])

			elif self.l == "L_TAKEOFF":
				if not self.log: time.sleep(1) # To slow things down
				if mission.atAltitude():
					self.l = "L_HOVERING"
					self.pipe.send([asctime(localtime()), "AT_ALTITUDE"])

				elif request[1] == "ABORT":
					mission.begin_Landing()
					self.l = "L_LANDING"
					self._notify("Abort. Landing now.")

			elif self.l == "L_HOVERING":
				if not self.log: time.sleep(1) # To slow things down
				if request[1] == "LAND":
					mission.begin_Landing()
					self.pipe.send([asctime(localtime()), "LANDING"])
					self.l = "L_LANDING"

				elif request[1] == "ABORT":
					mission.begin_Landing()
					self.l = "L_LANDING"
					self._notify("Abort. Landing now.")

			elif self.l == "L_LANDING":
				if not self.log: time.sleep(1) # To slow things down
				if mission.hasLanded():
					self.pipe.send([asctime(localtime()), "LANDED"])
					self.l = "L_CONNECTED"

			if curLoc != self.l:
				self._notify("FSM Location Transition: " + str(curLoc) + " to " + str(self.l))

