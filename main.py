import sys, serial
import decode, ui

port = 'COM1'

print(ui.logo_black)
print("■ Welcome to ThingsSpeek Serial Code Decoder API")
print(rf"/:::\ Serial port, try to connect {port}...")

ser = serial.Serial(
    port= port,\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print(rf"■ Connected to {port}.")
print("Listening...")

#this will store the line
line = []
history = []

while True:
    for c in ser.read():
        if chr(c) == '$':
            data = ''.join(line)
            print(f"Data Received: {data}")
            decoded = decode.word_by_word(data)
            decode.print_results(decoded)
            print("%")

            history.append(data)
            line = []
            break
        line.append(chr(c))

ser.close()
