import sounddevice as sd

# Get a list of all available devices
devices = sd.query_devices()
print(devices)
