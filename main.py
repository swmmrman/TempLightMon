import logic
import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)
print("Starting")
(temp1, temp2, h1, h2, ldr) = map(float, ser.readline().decode('utf-8').strip().split(","))
maxt1 = mint1 = temp1
maxh1 = minh1 = h1
maxt2 = mint2 = temp2
maxh2 = minh2 = h2
maxd = mind = temp2 - temp1

up_arrow = u'\u2191'
down_arrow = u'\u2193'

maxldr = int(ldr)
minldr = int(ldr)
print("\n\n")
while True:
    (temp1, temp2, h1, h2, ldr) = map(float, ser.readline().decode('utf-8').strip().split(","))
    delta = temp2 - temp1
    dv = abs(delta)
    arrow = up_arrow if delta > 0 else down_arrow
    ldr = int(ldr)
    if minldr > ldr: minldr = ldr
    if maxldr < ldr: maxldr = ldr
    if maxt1 < temp1: maxt1 = temp1
    if mint1 > temp1: mint1 = temp1
    if maxh1 < h1: maxh1 = h1
    if minh1 > h1: minh1 = h1
    if maxt2 < temp2: maxt2 = temp2
    if mint2 > temp2: mint2 = temp2
    if minh2 > h2: minh2 = h2
    if maxh2 < h2: maxh2 = h2
    if maxd < delta: maxd = delta
    if mind > delta: mind = delta
    hdv = abs(maxd)
    ldv = abs(mind)
    harrow = up_arrow if maxd > 0 else down_arrow
    larrow = up_arrow if mind > 0 else down_arrow
    ups = "\033[1A"
    print(F"{ups * 3}", end="")
    print(F'Current: \tT1: {temp1:5.2f} H1: {h1: 5.2f} T2: {temp2:5.2f} H2: {h2: 5.2f} TD: {dv: 6.2f}{arrow} LDR: {ldr:04d}')
    print(F"High:\t\tT1: {maxt1:5.2f} H1: {maxh1: 5.2f} T2: {maxt2:5.2f} H2: {maxh2: 5.2f} TD: {hdv: 6.2f}{harrow} LDR: {maxldr:04d}")
    print(F"Low:\t\tT1: {mint1:5.2f} H1: {minh1: 5.2f} T2: {mint2:5.2f} H2: {minh2: 5.2f} TD: {ldv: 6.2f}{larrow} LDR: {minldr:04d}")
