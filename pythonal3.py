import serial

s = serial.Serial('/dev/cu.usbmodem14101', 9600, timeout=1)
c = "you can drive"
d = "you cannot drive"

while True:
    a = ""
    for x in range(5):
        output = s.read()
        output2 = output.strip().decode('utf-8')
        a = a + output2
    print(float(a))
    if float(a) <= 600:
        print(c)
    else:
        print(d)
        break

