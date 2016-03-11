import gpx

gpx.connect('/dev/ttyACM1')

print "connected"

gpx.write('G1 Z20')
gpx.write('G1 Z30')
