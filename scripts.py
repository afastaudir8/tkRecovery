import subprocess
import platform

binos = platform.system()


def deviceconnected():
    if binos == 'Linux':
        deviceid = subprocess.check_output(["lsusb"])
        deviceid = str(deviceid)
    elif binos == 'Darwin':
        deviceid = subprocess.check_output(["system_profiler", "SPUSBDataType"])
        deviceid = str(deviceid)
    if "12a8" in deviceid:
        devicestatus = "Device in Normal Mode"
    elif "1281" in deviceid:
        devicestatus = "Device in Recovery Mode"
    else:
        devicestatus =  "No device found!"
    return devicestatus

def enterrecovery():
    deviceinfo = subprocess.check_output(f"./{binos}/ideviceinfo | grep UniqueDeviceID", shell=True)
    deviceinfo = str(deviceinfo)
    UUID = deviceinfo[18:]
    UUID = UUID[:-3]
    subprocess.call(f"./{binos}/ideviceenterrecovery {UUID}", shell=True)

def exitrecovery():
    subprocess.call(f"{binos}/irecovery -n", shell=True)

