#!/usr/bin/env python3
import RPi_I2C_driver
from time import *

my_lcd = RPi_I2C_driver.lcd()
# test 2
my_lcd.backlight(1)
my_lcd.lcd_display_string("RPi I2C test", 1)
my_lcd.lcd_display_string(" Custom chars", 2)

sleep(2) # 2 sec delay
my_lcd.backlight(0)

my_lcd.lcd_clear()
# let's define a custom icon, consisting of 6 individual characters
# 3 chars in the first row and 3 chars in the second row
fontdata1 = [
        # Char 0 - Upper-left
        [ 0x00, 0x00, 0x03, 0x04, 0x08, 0x19, 0x11, 0x10 ],
        # Char 1 - Upper-middle
        [ 0x00, 0x1F, 0x00, 0x00, 0x00, 0x11, 0x11, 0x00 ],
        # Char 2 - Upper-right
        [ 0x00, 0x00, 0x18, 0x04, 0x02, 0x13, 0x11, 0x01 ],
        # Char 3 - Lower-left
        [ 0x12, 0x13, 0x1b, 0x09, 0x04, 0x03, 0x00, 0x00 ],
        # Char 4 - Lower-middle
        [ 0x00, 0x11, 0x1f, 0x1f, 0x0e, 0x00, 0x1F, 0x00 ],
        # Char 5 - Lower-right
        [ 0x09, 0x19, 0x1b, 0x12, 0x04, 0x18, 0x00, 0x00 ],
        # Char 6 - my test
	[ 0x1f,0x0,0x4,0xe,0x0,0x1f,0x1f,0x1f],
]

# Load logo chars (fontdata1)
my_lcd.lcd_load_custom_chars(fontdata1)


# Write first three chars to row 1 directly
my_lcd.lcd_write(0x80)
my_lcd.lcd_write_char(0)
my_lcd.lcd_write_char(1)
my_lcd.lcd_write_char(2)
# Write next three chars to row 2 directly
my_lcd.lcd_write(0xC0)
my_lcd.lcd_write_char(3)
my_lcd.lcd_write_char(4)
my_lcd.lcd_write_char(5)
my_lcd.backlight(1)
sleep(2)

my_lcd.lcd_clear()

my_lcd.lcd_display_string_pos("Testing",1,1) # row 1, column 1
sleep(1)
my_lcd.lcd_display_string_pos("Testing",2,3) # row 2, column 3
sleep(1)
my_lcd.lcd_clear()

# Now let's define some more custom characters
fontdata2 = [
        # Char 0 - left arrow
        [ 0x1,0x3,0x7,0xf,0xf,0x7,0x3,0x1 ],
        # Char 1 - left one bar 
        [ 0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10 ],
        # Char 2 - left two bars
        [ 0x18,0x18,0x18,0x18,0x18,0x18,0x18,0x18 ],
        # Char 3 - left 3 bars
        [ 0x1c,0x1c,0x1c,0x1c,0x1c,0x1c,0x1c,0x1c ],
        # Char 4 - left 4 bars
        [ 0x1e,0x1e,0x1e,0x1e,0x1e,0x1e,0x1e,0x1e ],
        # Char 5 - left start
        [ 0x0,0x1,0x3,0x7,0xf,0x1f,0x1f,0x1f ],
        # Char 6 - 
        # [ ],
]

# Load logo chars from the second set
my_lcd.lcd_load_custom_chars(fontdata2)

block = chr(255) # block character, built-in

# display two blocks in columns 5 and 6 (i.e. AFTER pos. 4) in row 1
# first draw two blocks on 5th column (cols 5 and 6), starts from 0
my_lcd.lcd_display_string_pos(block * 2,1,4)

# 
pauza = 0.2 # define duration of sleep(x)
#
# now draw cust. chars starting from col. 7 (pos. 6)

pos = 6
my_lcd.lcd_display_string_pos(chr(1),1,6)
sleep(pauza)

my_lcd.lcd_display_string_pos(chr(2),1,pos)
sleep(pauza)

my_lcd.lcd_display_string_pos(chr(3),1,pos)
sleep(pauza)

my_lcd.lcd_display_string_pos(chr(4),1,pos)
sleep(pauza)

my_lcd.lcd_display_string_pos(block,1,pos)
sleep(pauza)

# and another one, same as above, 1 char-space to the right
pos = pos +1 # increase column by one

my_lcd.lcd_display_string_pos(chr(1),1,pos)
sleep(pauza)
my_lcd.lcd_display_string_pos(chr(2),1,pos)
sleep(pauza)
my_lcd.lcd_display_string_pos(chr(3),1,pos)
sleep(pauza)
my_lcd.lcd_display_string_pos(chr(4),1,pos)
sleep(pauza)
my_lcd.lcd_display_string_pos(block,1,pos)
sleep(pauza)


#
# now again load first set of custom chars - smiley
my_lcd.lcd_load_custom_chars(fontdata1)

my_lcd.lcd_display_string_pos(chr(0),1,9)
my_lcd.lcd_display_string_pos(chr(1),1,10)
my_lcd.lcd_display_string_pos(chr(2),1,11)
my_lcd.lcd_display_string_pos(chr(3),2,9)
my_lcd.lcd_display_string_pos(chr(4),2,10)
my_lcd.lcd_display_string_pos(chr(5),2,11)

sleep(2)
my_lcd.lcd_clear()
sleep(1)
my_lcd.backlight(0)
