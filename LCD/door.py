#******************************************************************************
# File Name:   udp_client.py
#
# Description: A simple python based UDP client.
# 
#******************************************************************************
# (c) 2020, Cypress Semiconductor Corporation. All rights reserved.
#******************************************************************************
# This software, including source code, documentation and related materials
# ("Software"), is owned by Cypress Semiconductor Corporation or one of its
# subsidiaries ("Cypress") and is protected by and subject to worldwide patent
# protection (United States and foreign), United States copyright laws and
# international treaty provisions. Therefore, you may use this Software only
# as provided in the license agreement accompanying the software package from
# which you obtained this Software ("EULA").
#
# If no EULA applies, Cypress hereby grants you a personal, non-exclusive,
# non-transferable license to copy, modify, and compile the Software source
# code solely for use in connection with Cypress's integrated circuit products.
# Any reproduction, modification, translation, compilation, or representation
# of this Software except as specified above is prohibited without the express
# written permission of Cypress.
#
# Disclaimer: THIS SOFTWARE IS PROVIDED AS-IS, WITH NO WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, NONINFRINGEMENT, IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. Cypress
# reserves the right to make changes to the Software without notice. Cypress
# does not assume any liability arising out of the application or use of the
# Software or any product or circuit described in the Software. Cypress does
# not authorize its products for use in any products where a malfunction or
# failure of the Cypress product may reasonably be expected to result in
# significant property damage, injury or death ("High Risk Product"). By
# including Cypress's product in a High Risk Product, the manufacturer of such
# system or application assumes all risk of such use and in doing so agrees to
# indemnify Cypress against all liability.
#******************************************************************************/

#!/usr/bin/env python
import socket
import optparse
import time
import sys
import RPi_I2C_driver
from datetime import date, datetime


BUFFER_SIZE = 1024

# IP details for the UDP server
DEFAULT_IP   = '127.0.0.1'    # IP address of the UDP server
DEFAULT_PORT = 50007             # Port of the UDP server

START_MSG="A"

def udp_client( server_ip, server_port):
    print("================================================================================")
    print("UDP Client")
    print("================================================================================")
    print("Sending data to UDP Server with IP Address:",server_ip, " Port:",server_port)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(bytes(START_MSG, "utf-8"), (server_ip, server_port))

    while True:
        print("================================================================================")
        day = datetime.now().strftime("%-m/%-d/%y")
        tme = datetime.now().strftime("%-I:%M%S %p")
        data = int(s.recv(BUFFER_SIZE).decode('utf-8'))
        print(day)
        print(tme)
        my_lcd = RPi_I2C_driver.lcd()
        my_lcd.lcd_display_string(day, 1)
        my_lcd.lcd_display_string(tme, 2)
        my_lcd.backlight(data)
        print("Command from Server:")
        if data == 0:
            print("LED OFF")
            message = 'LED OFF ACK'
            s.sendto(message.encode('utf-8'), (server_ip, server_port))
        if data == 1:
            print("LED ON")
            message = 'LED ON ACK'
            s.sendto(message.encode('utf-8'), (server_ip, server_port))
        print("Acknowledgement sent to server")

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-p", "--port", dest="port", type="int", default=DEFAULT_PORT, help="Port to listen on [default: %default].")
    parser.add_option("--hostname", dest="hostname", default=DEFAULT_IP, help="Hostname or IP address of the server to connect to.")
    (options, args) = parser.parse_args()
    #start udp client
    udp_client(options.hostname, options.port)
