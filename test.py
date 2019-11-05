from DriverInterface import DriverInterface
import time

def test():
    d = DriverInterface()

    sd = 0.5
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)

    sd = 0.2
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)

    sd = 0.1
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)

    sd = 0.05
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)

    sd = 0.01
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)

    sd = 0.005
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)

    sd = 0.001
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)
