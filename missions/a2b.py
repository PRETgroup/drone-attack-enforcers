#############DEPENDENCIES#######################
from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import time
import socket
import math
from time import asctime, localtime
from pymavlink import mavutil

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

	def configure(self, targetAltitude, distANorth, distAEast):
		self.targetAltitude = targetAltitude
		# self.distANorth = distANorth
		# self.distAEast = distAEast
		self._add_point(self.vehicle, distANorth, distAEast)

	def _add_point(self, vehicle, distANorth, distAEast):
		currentLoc = vehicle.location.global_frame

		cmds = vehicle.commands
		self._notify("Clear existing commands")
		cmds.clear()
		self._notify("Add new commands")
		cmds.add(Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 0, self.targetAltitude))
		pointA = self.get_location_metres(currentLoc, distANorth, distAEast)
		cmds.add(Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, pointA.lat, pointA.lon, self.targetAltitude))

		# add dummy point to know when we are there
		cmds.add(Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, pointA.lat, pointA.lon, self.targetAltitude))    

		cmds.upload()

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
		self._notify("Current Altitude: " + str(self.vehicle.location.global_relative_frame.alt))
		if self.vehicle.location.global_relative_frame.alt>=.95*self.targetAltitude:
			self._notify("Target altitude reached!!")
			return True
		else:
			return False

	## Travel
	def begin_Travel(self):
		# Reset mission set to first (0) waypoint
		self.vehicle.commands.next=0

		# Set mode to AUTO to start mission
		self.vehicle.mode = VehicleMode("AUTO")

	def get_location_metres(self, original_location, dNorth, dEast):
		"""
		Returns a LocationGlobal object containing the latitude/longitude `dNorth` and `dEast` metres from the 
		specified `original_location`. The returned Location has the same `alt` value
		as `original_location`.

		The function is useful when you want to move the vehicle around specifying locations relative to 
		the current vehicle position.
		The algorithm is relatively accurate over small distances (10m within 1km) except close to the poles.
		For more information see:
		http://gis.stackexchange.com/questions/2951/algorithm-for-offsetting-a-latitude-longitude-by-some-amount-of-meters
		"""
		earth_radius=6378137.0 #Radius of "spherical" earth
		#Coordinate offsets in radians
		dLat = dNorth/earth_radius
		dLon = dEast/(earth_radius*math.cos(math.pi*original_location.lat/180))

		#New position in decimal degrees
		newlat = original_location.lat + (dLat * 180/math.pi)
		newlon = original_location.lon + (dLon * 180/math.pi)
		return LocationGlobal(newlat, newlon,original_location.alt)

	def get_distance_metres(self, aLocation1, aLocation2):
		"""
		Returns the ground distance in metres between two LocationGlobal objects.

		This method is an approximation, and will not be accurate over large distances and close to the 
		earth's poles. It comes from the ArduPilot test code: 
		https://github.com/diydrones/ardupilot/blob/master/Tools/autotest/common.py
		"""
		dlat = aLocation2.lat - aLocation1.lat
		dlong = aLocation2.lon - aLocation1.lon
		return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5

	def distance_to_current_waypoint(self):
		"""
		Gets distance in metres to the current waypoint. 
		It returns None for the first waypoint (Home location).
		"""
		nextwaypoint = self.vehicle.commands.next

		if nextwaypoint==0:
			return None
		missionitem=self.vehicle.commands[nextwaypoint-1] #commands are zero indexed
		lat = missionitem.x
		lon = missionitem.y
		alt = missionitem.z
		targetWaypointLocation = LocationGlobalRelative(lat,lon,alt)
		distancetopoint = self.get_distance_metres(self.vehicle.location.global_frame, targetWaypointLocation)
		return distancetopoint

	## Determine if at the target position B
	def atPositionA(self):
		nextwaypoint=self.vehicle.commands.next
		self._notify("Distance to waypoint (" + str(nextwaypoint) + "): " + str(self.distance_to_current_waypoint()))

		if nextwaypoint==2: #Dummy waypoint - as soon as we reach waypoint 4 this is true and we exit.
			self._notify("In location when at point B")
			return True
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
		while self.vehicle.mode!='LAND':
			self._notify("Waiting for drone to enter LAND mode")
			time.sleep(1)
		self._notify("Vehicle now in LAND mode. Will touch ground shortly.")
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
			self.logger = DroneStatusLogger("A2B")

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
				self._notify(request)
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
					req_exit = True

			elif self.l == "L_CONNECTED":
				if request[1] == "CONFIG_LOC":
					try:
						alt = int(request[2])
						d_n = int(request[3])
						d_e = int(request[4])
						mission.configure(alt, d_n, d_e)
						self.pipe.send([asctime(localtime()), "CONFIGED"])
						self._notify("Done configure")
						self.l = "L_CONFIGED"
					except:
						self._notify("Invalid config. Waiting for new config")

				elif request[1] == "END":
					self.l = "L_DISCONNECT"
					self._notify("End mission")
					self.pipe.send([asctime(localtime()), "END"])
					req_exit = True
				
			elif self.l == "L_CONFIGED":
				if request[1] == "RUN":
					mission.take_off()
					self.l = "L_TAKEOFF"
					self._notify("Take Off")

			elif self.l == "L_TAKEOFF":
				if not self.log: time.sleep(1) # To slow things down
				if mission.atAltitude():
					mission.begin_Travel()
					self.l = "L_TRAVEL_TO_B"
					self.pipe.send([asctime(localtime()), "TRAVELING_B"])

				elif request[1] == "ABORT":
					mission.begin_Landing()
					self.l = "L_LANDING"
					self._notify("Abort. Landing now.")

			elif self.l == "L_TRAVEL_TO_B":
				if not self.log: time.sleep(1) # To slow things down
				if mission.atPositionA():
					self.l = "L_AT_B"
					self.pipe.send([asctime(localtime()), "AT_B"])

				elif request[1] == "ABORT":
					mission.begin_Landing()
					self.l = "L_LANDING"
					self._notify("Abort. Landing now.")

			elif self.l == "L_AT_B":
				if not self.log: time.sleep(1) # To slow things down
				if request[1] == "LAND":
					mission.begin_Landing()
					self.l = "L_LANDING"

			elif self.l == "L_LANDING":
				if not self.log: time.sleep(1) # To slow things down
				if mission.hasLanded():
					self.pipe.send([asctime(localtime()), "LANDED"])
					self.l = "L_CONNECTED"

			if curLoc != self.l:
				self._notify("FSM Location Transition: " + str(curLoc) + " to " + str(self.l))

