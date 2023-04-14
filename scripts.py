import subprocess
import platform

binos = platform.system()
devicestatus = "No device found!"

def deviceconnected():
    if binos == 'Linux':
        deviceid = subprocess.check_output(["lsusb"])
        if "12a8" in deviceid:
            devicestatus = "Device in Normal Mode"
        elif "1281" in deviceid:
            devicestatus = "Device in Recovery Mode"
        else:
            devicestatus =  "No device found!"

