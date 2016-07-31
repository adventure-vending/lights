from kinet import *

#ethernet attached power supply.
#The PowerSupply class inherits from list

ipAddress = "192.168.1.120"

pds = PowerSupply(ipAddress)

# address light fixtures using lowest dmx address
# example if using RGB addresses 3,4,5 choose 5
fix00 = FixtureRGB(12)
fix01 = FixtureRGB(24)
fix02 = FixtureRGB(0)
fix03 = FixtureRGB(0)
fix04 = FixtureRGB(0)
fix05 = FixtureRGB(0)
fix06 = FixtureRGB(0)
fix07 = FixtureRGB(0)
fix08 = FixtureRGB(0)
fix09 = FixtureRGB(0)
fix10 = FixtureRGB(0)
fix11 = FixtureRGB(0)
fix12 = FixtureRGB(0)
fix13 = FixtureRGB(0)
fix14 = FixtureRGB(0)
fix15 = FixtureRGB(0)
fix16 = FixtureRGB(0)
fix17 = FixtureRGB(0)
fix18 = FixtureRGB(0)
fix19 = FixtureRGB(0)
fix20 = FixtureRGB(0)
fix21 = FixtureRGB(0)
fix22 = FixtureRGB(0)
fix23 = FixtureRGB(0)


# Attach each of the 24 light fixtures to the power supply
pds.append(fix00)
pds.append(fix01)
pds.append(fix02)
pds.append(fix03)
pds.append(fix04)
pds.append(fix05)
pds.append(fix06)
pds.append(fix07)
pds.append(fix08)
pds.append(fix09)
pds.append(fix10)
pds.append(fix11)
pds.append(fix12)
pds.append(fix13)
pds.append(fix14)
pds.append(fix15)
pds.append(fix16)
pds.append(fix17)
pds.append(fix18)
pds.append(fix19)
pds.append(fix20)
pds.append(fix21)
pds.append(fix22)
pds.append(fix23)



# choose a box from 0- 23 and that box will be lit with all white, all others off
#TODO make into a class that can be called with the current box number
prize_box = 0

for i in range(0, len(list(pds))):
  if i == prize_box:
    #if this is the selected prize then turn white
    #TODO make light pulse
    pds[i].rgb = (255, 255, 255)
  else:
    #turn off light
    #TODO make slowly fade or some other aswsome effect
    pds[i].rgb = (0, 0, 0)

pds.go()
time.sleep(0.1)




