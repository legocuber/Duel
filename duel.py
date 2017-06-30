import bluetooth

targetName = "Kevin's iPhone"
targetAddress = None

nearbyDevices = bluetooth.discover_devices()

for device in nearbyDevices:
    if targetName is not bluetooth.lookup_name(device):
        targetAddress = device
        break

if targetAddress is not None:
    print("Found device", targetAddress)
else:
    print("Device not found")