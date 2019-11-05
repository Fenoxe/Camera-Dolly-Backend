from DriverInterface import DriverInterface
import time
from Move import Move

def di_test():
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

def move_test():
    print("Beginning Move.py Test")
    time.sleep(0.5)
    s = 1
    e = 0.5
    d = 4
    print("start = " + str(s))
    print("end = " + str(e))
    print("duration = " + str(d))
    m = Move()
    m.start_pos = s
    m.end_pos = e
    m.duration = d
    time.sleep(0.5)
    print("Executing...")
    m.execute_move()

def current_test(n, t):
    print("Beginning current test")
    time.sleep(0.5)
    
    d = DriverInterface()

    ms = 0
    print(ms)
    d.set_step(ms)
    d.execute(0.001 * n, int(round(t * 10000 / n)))

    ms = 1
    print(ms)
    d.set_step(ms)
    d.execute(0.001 * n, int(round(t * 10000 / n)))

    ms = 2
    print(ms)
    d.set_step(ms)
    d.execute(0.001 * n, int(round(t * 10000 / n)))

    ms = 3
    print(ms)
    d.set_step(ms)
    d.execute(0.001 * n, int(round(t * 10000 / n)))

    ms = 4
    print(ms)
    d.set_step(ms)
    d.execute(0.001 * n, int(round(t * 10000 / n)))
    
