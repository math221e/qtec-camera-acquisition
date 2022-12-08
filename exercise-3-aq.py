import requests
import json
import urllib.request
import time

headers = {
	"Accept": "*/*",
	"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
	"Connection": "keep-alive",
	"Content-Type": "text/x-gwt-rpc; charset=UTF-8",
	"Origin": "http://10.100.10.100",
	"Referer": "http://10.100.10.100/",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
	"X-GWT-Module-Base": "http://10.100.10.100/calibration/",
	"X-GWT-Permutation": "4E03BCEDEE9D362C8F89CA8597758B62",
}

c = 0


while True:
	r = requests.post("http://10.100.10.100/calibration/cameraCalibration", headers=headers, data="7|0|6|http://10.100.10.100/calibration/|009318633D69F217348B09ED7A68D075|com.qtec.cameracalibration.client.CameraCalibrationService|getV4LParameters|java.lang.String/2004016611|/dev/video4|1|2|3|4|1|5|6|")
	data = json.loads(r.text[4:])
	temperature = data[3440][54]
	urllib.request.urlretrieve("http://10.100.10.100/cameraimage?name=savePPM&channelMapping=0,0,0&device=/dev/video4&suffix=2", "exercise-3-data/5sec-" + str(c) + ".ppm")
	
	with open("exercise-3-data/5sec-temp.csv", "a") as f:
		f.write(str(c) + "," + str(temperature) + "\n")


	print(c, str(temperature) + "C")
	c += 1
	time.sleep(12)

"""
curl 'http://10.100.10.100/calibration/cameraCalibration' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: text/x-gwt-rpc; charset=UTF-8' \
  -H 'Origin: http://10.100.10.100' \
  -H 'Referer: http://10.100.10.100/' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36' \
  -H 'X-GWT-Module-Base: http://10.100.10.100/calibration/' \
  -H 'X-GWT-Permutation: 4E03BCEDEE9D362C8F89CA8597758B62' \
  --data-raw '7|0|6|http://10.100.10.100/calibration/|009318633D69F217348B09ED7A68D075|com.qtec.cameracalibration.client.CameraCalibrationService|getV4LParameters|java.lang.String/2004016611|/dev/video4|1|2|3|4|1|5|6|' \
  --compressed \
  --insecure

 """