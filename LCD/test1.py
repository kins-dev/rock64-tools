#!/usr/bin/env python3
import RPi_I2C_driver
from time import *

my_lcd = RPi_I2C_driver.lcd()
# test 2
my_lcd.lcd_display_string("Feed ME", 1)
