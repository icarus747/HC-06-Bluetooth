import serial
import time

PORT = "/dev/ttyAMA0"   # change to your port, e.g. "/dev/ttyUSB0"
BAUD_RATES = [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]
TIMEOUT = 0.5

def try_baud(port, baud):
    try:
        with serial.Serial(
            port=port,
            baudrate=baud,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=TIMEOUT,
            write_timeout=TIMEOUT,
        ) as ser:
            ser.reset_input_buffer()
            ser.reset_output_buffer()

            # HC-06 often expects plain "AT" with no CR/LF
            ser.write(b"AT")
            ser.flush()
            time.sleep(0.2)

            response = ser.read(100)
            return response.decode(errors="replace").strip()

    except Exception as e:
        return f"ERROR: {e}"

def main():
    print(f"Testing port: {PORT}")
    for baud in BAUD_RATES:
        resp = try_baud(PORT, baud)
        print(f"{baud}: {resp!r}")
        if "OK" in resp.upper():
            print(f"Working baud rate found: {baud}")
            break

if __name__ == "__main__":
    main()
