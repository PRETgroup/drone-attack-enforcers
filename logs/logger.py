import csv
import time

class DroneStatusLogger:
    def __init__(self, missionName=""):
        self.filename = "logs/" + str(missionName) + "_DroneStatus_" + time.ctime().replace(":",".").replace(" ", "_") + ".csv"
        f = open(self.filename, 'w', newline='')
        w = csv.writer(f)
        w.writerow(['time','lat','lon','alt'])
        f.close()

    def log(self, lat, lon, alt):
        f = open(str(self.filename), 'a', newline='')
        w = csv.writer(f)
        t = time.time()
        w.writerow([t, str(lat), str(lon), str(alt)])
        f.close()
