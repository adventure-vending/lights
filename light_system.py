import multiprocessing
from time import sleep
import sys
import signal
import constants
from kinet import *
# see https://github.com/vishnubob/kinet

#TODO, fix but in kinet library that chooses wifi interface when avalible

#ethernet attached power supply.
#The PowerSupply class inherits from list
ip_address = "192.168.1.120"
pds = PowerSupply(ip_address)
box = 0
#TODO, read from config file that includes fixures and starting addresses,
#TODO, create simple UI for setting number of fixtures and addresses

# address light fixtures using lowest dmx address
# example if using RGB addresses 3,4,5 choose 5
fix00 = FixtureRGB(0)
fix01 = FixtureRGB(6)
#fix02 = FixtureRGB(0)
#fix03 = FixtureRGB(0)
#fix04 = FixtureRGB(0)
#fix05 = FixtureRGB(0)
#fix06 = FixtureRGB(0)
#fix07 = FixtureRGB(0)
#fix08 = FixtureRGB(0)
#fix09 = FixtureRGB(0)
#fix10 = FixtureRGB(0)
#fix11 = FixtureRGB(0)
#fix12 = FixtureRGB(0)
#fix13 = FixtureRGB(0)
#fix14 = FixtureRGB(0)
#fix15 = FixtureRGB(0)
#fix16 = FixtureRGB(0)
#fix17 = FixtureRGB(0)
#fix18 = FixtureRGB(0)
#fix19 = FixtureRGB(0)
#fix20 = FixtureRGB(0)
#fix21 = FixtureRGB(0)
#fix22 = FixtureRGB(0)
#fix23 = FixtureRGB(0)

# Attach each of the 24 light fixtures to the power supply
# TODO, automate appending based on the number of fixtures defined.
pds.append(fix00)
pds.append(fix01)
#pds.append(fix02)
#pds.append(fix03)
#pds.append(fix04)
#pds.append(fix05)
#pds.append(fix06)
#pds.append(fix07)
#pds.append(fix08)
#pds.append(fix09)
#pds.append(fix10)
#pds.append(fix11)
#pds.append(fix12)
#pds.append(fix13)
#pds.append(fix14)
#pds.append(fix15)
#pds.append(fix16)
#pds.append(fix17)
#pds.append(fix18)
#pds.append(fix19)
#pds.append(fix20)
#pds.append(fix21)
#pds.append(fix22)
#pds.append(fix23)

def TGselectBox(pds, box, pause=.1, steps=1000):
    div = steps / len(pds)
    box = box -1
    for step in range(steps):
        ratio = 0
        for idx, fixture in enumerate(pds):

            if idx == box:
              #if this is the selected prize then turn white
              #TODO make light pulse
              pds[idx].rgb = (255, 255, 255)

            else:
              #if not the prize box do a slow rainbow patern
              ratio += (step + idx * div) % steps / float(steps)
              fixture.hsv = (ratio, 1.0, 1.0)
        print pds
        pds.go()
        time.sleep(pause)

def TGopenBox(pds, box):
  #TODO write a light show to celebrate when a box is opened
  #for now this is just the same routine for select box but faster
  #not sure if this looks good or not
      TGselectBox(pds, box, steps=10)

def TGidle(pds, pause=.1, steps=1000):
    div = steps / len(pds)
    for step in range(steps):
        ratio = 0
        for idx, fixture in enumerate(pds):
            ratio += (step + idx * div) % steps / float(steps)
            fixture.hsv = (ratio, 1.0, 1.0)
        print pds
        pds.go()
        time.sleep(pause)


class LightSystem(multiprocessing.Process):
    def __init__(self, q):
        super(LightSystem, self).__init__()
        self.q = q
        self.setup_handlers()

    def setup_handlers(self):
        def signal_handler(action, _):
            box = self.q.get()
            if action == constants.OPEN_BOX:
                self.open_box(box)
            elif action == constants.SELECT_BOX:
                self.select_box(box)
            self.idle()
        signal.signal(constants.OPEN_BOX, signal_handler)
        signal.signal(constants.SELECT_BOX, signal_handler)

    def run(self):
        self.idle()

    def idle(self):
        TGidle(pds, box)
        while True:
            print "in idle mode"
            sleep(.3)

    def open_box(self, box):
        TGopenBox(pds, box)
        print "box opened {}".format(box)
        sys.stdout.flush()

    def select_box(self, box):
        TGselectBox(pds, box)
        print "box selected {}".format(box)
        sys.stdout.flush()

