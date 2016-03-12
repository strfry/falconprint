#!/usr/bin/python2

import gpx

gpx.connect('/dev/ttyACM0', 115200, 'gpx.ini')

#gpx.write('G1 Z10')
#gpx.write('G1 Z20; fooo')

print "connected"



def home():
    setup_gcode = """
T0; set primary extruder
M73 P0; enable show build progress
M104 S42 T0; set nozzle heater to first layer temperature
G21; set units to mm  -- maybe unnecessary
G162 X Y F6000; home XY axes maximum
G161 Z F9000; home Z axis minimum
G92 Z0; set Z to 0
M132 X Y Z A B; Recall stored home offsets -- unknown
G90; set positioning to absolute -- default

G1 X-95 Y-73 Z30 F14000; move to waiting position (front left corner of print bed)
;G130 X0 Y0 A0 B0; set stepper motor vref to lower value while heating
;M6 T0; wait for bed and extruder to heat up
;G130 X127 Y127 A127 B127; set stepper motor vref to defaults
;M108 T0 R3; set extruder speed
;G92 E0; set E to 0

M320; acceleration enabled for all commands that follow -- default? no change without
;G1 Z0.2 F6000.000; move to first layer height
;G1 X100 Y-73 F14000.000; move to front right corner of bed
;G1 X-90 Y-73 ;E24 F2000.000; extrude a line of filament across the front edge of the bed
;G4 P2000; wait for ooze to slow
;G1 Z0 F6000.000; lower nozzle height to 0
;G1 X-95; wipe nozzle
;G1 Z0.2 F6000.000; set nozzle to first layer height
;G1 F12000; ensure fast travel to first print move
;G92 E0; set E to 0 again
;M73 P0; reset build progress to 0
    """

    for line in setup_gcode.splitlines():
        result = gpx.write(line)
        print line, ":", result


