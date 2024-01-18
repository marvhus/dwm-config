from os.path import exists
from os import system

print("Running power_warning.py")

def writeCharge(percent, path):
    with open(path, "wt") as f:
        f.write(f'{percent}')

batery = "BAT1"

print("Checking battery status")

with open(f"/sys/class/power_supply/{batery}/charge_now") as f:
    charge_now = float(f.read())
with open(f"/sys/class/power_supply/{batery}/charge_full") as f:
    charge_full = float(f.read())

lastChargePath = "/home/mh/.cache/lastCharge"

percent = 100*charge_now/charge_full

if not exists(lastChargePath):
    writeCharge(percent, lastChargePath)

with open(lastChargePath, "rt") as f:
    lastPercent = float(f.read())

print("Checking percentage")

if percent < 30 and percent < lastPercent:
    print("Low power")
    system(f"notify-send 'Low Power!' 'You have {percent:.2f}% battery left.' -u critical")
else:
    print("Enough power")

writeCharge(percent, lastChargePath)
