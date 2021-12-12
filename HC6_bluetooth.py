#!/usr/bin/env python
import serial


def serial_setup(connbaud):
    ser = serial.Serial(port='/dev/ttyAMA0',
                        baudrate=connbaud,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=1)
    return ser


def send_commands(conn, command):
    conn.write(command)
    returned_line = conn.readline()
    print(f'\n\nReturned line: {returned_line}\n\n')
    input("Press Enter to continue...")

def baud_logic(setbaud):
    if setbaud == 1200:
        return b'AT+BAUD1'
    elif setbaud == 2400:
        return b'AT+BAUD2'
    elif setbaud == 4800:
        return b'AT+BAUD3'
    elif setbaud == 9600:
        return b'AT+BAUD4'
    elif setbaud == 19200:
        return b'AT+BAUD5'
    elif setbaud == 38400:
        return b'AT+BAUD6'
    elif setbaud == 57600:
        return b'AT+BAUD7'
    elif setbaud == 115200:
        return b'AT+BAUD8'


if __name__ == '__main__':
    connbaud = 9600
    while 1:
        user_response = int(input(
            "Enter number for programing your HC-06.\n  1. Check Connection\n  2. Check Version\n  "
            "3. Change BAUD rate\n  4. Change boradcast name\n  5. Change bluetooth pin"))
        connbaud = int(input(f"enter connection baud rate [{connbaud}]:") or connbaud)
        if user_response == 1:
            command = b'AT'

        if user_response == 2:
            command = b'AT+VERSION'

        if user_response == 3:
            setbaud = int(input("Desired baud rate [9600]:") or 9600)
            command = baud_logic(setbaud)

        if user_response == 4:
            new_name = str(input("Desired bluetooth name [HC06]?") or "HC06")
            command = f'AT+NAME{new_name}'.encode()

        if user_response == 5:
            setpin = str(input("Desired pin code [1234]:") or "1234")
            command = f'AT+PIN{setpin}'.encode()
        print(f"Command to be sent: {command}")
        pass
        # conn = serial_setup(connbaud)
        # # conn = "debug"
        # send_commands(conn, command)
        # conn.close()
