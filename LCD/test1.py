#!/usr/bin/env python3
import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()
# test 2
mylcd.lcd_display_string("Feed ME", 1)
