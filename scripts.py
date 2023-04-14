import subprocess
import platform

binos = platform.system()


def deviceconnected():
    global devicestatus
    if binos == 'Linux':
        deviceid = subprocess.check_output(["lsusb"])
        deviceid = str(deviceid)
        if "12a8" in deviceid:
            devicestatus = "Device in Normal Mode"
        elif "1281" in deviceid:
            devicestatus = "Device in Recovery Mode"
        else:
            devicestatus =  "No device found!"
    return devicestatus

