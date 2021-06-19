import logic
import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)
print("Starting")
(temp1, temp2, ldr) = ser.readline().decode('utf-8').strip().split(",")
maxt1 = float(temp1)
mint1 = float(temp1)
maxt2 = float(temp2)
mint2 = float(temp2)
maxd = float(temp1) - float(temp2)
mind = maxd
maxldr = int(ldr)
minldr = int(ldr)
print("\n\n")
while True:
    (temp1, temp2, ldr) = ser.readline().decode('utf-8').strip().split(",")
    temp1 = float(temp1)
    temp2 = float(temp2)
    ldr = int(ldr)
    delta = temp1 - temp2
    if minldr > ldr: minldr = ldr
    if maxldr < ldr: maxldr = ldr
    if maxt1 < temp1: maxt1 = temp1
    if mint1 > temp1: mint1 = temp1
    if maxt2 < temp2: maxt2 = temp2
    if mint2 > temp2: mint2 = temp2
    if maxd < delta: maxd = delta
    if mind > delta: mind = delta
    ups = "\033[1A"
    print(F"{ups * 3}Current: \tTemp 1: {temp1:3.2f} Temp2: {temp2:3.2f} Delta: {delta:05.2f} LDR: {ldr:04d}")
    print(F"Maximums: \tTemp 1: {maxt1:3.2f} Temp2: {maxt2:3.2f} Delta: {maxd:05.2f} LDR: {maxldr:04d}")
    print(F"Minimums: \tTemp 1: {mint1:3.2f} Temp2: {mint2:3.2f} Detla: {mind:05.2f} LDR: {minldr:04d}")
