#!/usr/bin/env python 

from skytraq.venus6 import Venus6

serial_speed = 115200
gps = Venus6('/dev/ttyUSB0', serial_speed, debug=False)


# Get serial speed
serial_speed = gps.guessSerialSpeed()
print "serial speed =", serial_speed

# Set serial speed
gps.setSerialSpeed(115200)

print "serial speed set to =", gps.guessSerialSpeed()

# Get Software Version
print "software version =", gps.getSoftwareVersion()

# Set Navigation Mode (5 is airborne)
# 0 = auto
# 1 = pedestrian
# 2 = car
# 3 = marine
# 4 = balloon
# 5 = airbourne
gps.setNavigationMode(5)
print "navigation mode =", gps.getNavigationMode()


#Set Position Update rate
gps.setPositionUpdateRate(20)
print "position update rate =", gps.getPositionUpdateRate()


