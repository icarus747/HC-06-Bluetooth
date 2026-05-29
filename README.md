# HC-06-Bluetooth

Script to configure a DSD TECH HC-06 bluetooth Serial Transceiver to communicate with a Raspberry Pi 2b+ and 3. Connect
to the pinouts from this link:
http://helloraspberrypi.blogspot.com/2015/11/raspberry-pi-bluetooth-serial-terminal.html

If using a Raspberry Pi 5, look at this page for config.txt settings. What worked for me was `dtoverlay=uart0-pi5`.
Connect to 5v, ground, pin14 (TX0), pin15 (RX0)

https://github.com/raspberrypi/linux/blob/2e376fd6b1f2fe1ab785fa607f36db6669d0bb8b/arch/arm/boot/dts/overlays/README#L5289

Use screen to connect to serial interface to check communication. `screen -F /dev/ttyAMA0 9600`

Helpful commands:

`stty -F /dev/ttyAMA0`

`stty -F /dev/ttyAMA0 9600`

`pinctrl get 14-15`

This will allow you to increase the baud rate of your HC-06 for better cli throughput. Or to communicate with other
devices that use a different baud rate.

The script runs and asks questions about what you want to do.  It is a loop so you must break out of it.
 ### Enter number for programing your HC-06.
  1. Check Connection
  2. Check Version
  3. Change BAUD rate
  4. Change broadcast name
  5. Change bluetooth pin

Video explains what is going on (I'm not the author of it)
https://www.youtube.com/watch?v=Iyd4gX0AR54

A script for finding the baud rate of the HC-06 is provided as find_baud.py.  This will try baud range 1200-115200 until `AT` returns an OK.
