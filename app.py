# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
import time
from envirophat import light, weather, motion, analog
unit = 'hPa'
while True:
    acc_values = [round(x,2) for x in motion.accelerometer()]
    output = """
Temperature: {t:.2f}c
Pressure: {p:.2f}{unit}
Brightness: {c}
""".format(
        unit = unit,
        t = weather.temperature(),
        p = weather.pressure(unit=unit),
        c = light.light(),
        ax = acc_values[0],
        ay = acc_values[1],
        az = acc_values[2]
)
    sys.stdout.write(output)
    sys.stdout.flush()
    time.sleep(10)
