import requests
import json
import urllib.request
import time

# Url for obtaining parameters
param_url = "http://10.100.10.100/calibration/cameraCalibration"

# Image url
image_url = "http://10.100.10.100/cameraimage?name=savePPM&channelMapping=0,0,0&device=/dev/video4&suffix=2"

# HTTP headers send by the browser
headers = {
	"Accept": "*/*",
	"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
	"Connection": "keep-alive",
	"Content-Type": "text/x-gwt-rpc; charset=UTF-8",
	"Origin": "http://10.100.10.100",
	"Referer": "http://10.100.10.100/",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
	"X-GWT-Module-Base": "http://10.100.10.100/calibration/",
	"X-GWT-Permutation": "4E03BCEDEE9D362C8F89CA8597758B62"
}

# Endpoint data for obtaining V4L parameters
data = "7|0|6|http://10.100.10.100/calibration/|009318633D69F217348B09ED7A68D075|\
				com.qtec.cameracalibration.client.CameraCalibrationService|getV4LParameters|\
				java.lang.String/2004016611|/dev/video4|1|2|3|4|1|5|6|"

# Counter for filenames
c = 0

while True:
	# Perform request
	r = requests.post(param_url, headers=headers, data="")
	data = json.loads(r.text[4:])
	
	# Read temperature form response
	temperature = data[3440][54]

	# Capture image and save to file
	urllib.request.urlretrieve("", "image-" + str(c) + ".ppm")
	
	# Append temperature to csv file
	with open("temp.csv", "a") as f:
		f.write(str(c) + "," + str(temperature) + "\n")

	# Print temperature to terminal
	print(c, str(temperature) + "C")

	# Increase counter and set sampling period
	c += 1
	time.sleep(12)
