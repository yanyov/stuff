#pip install mouse
import mouse
import time

# move 100 right and 100 down with a duration of 0.5 seconds
while True:
    mouse.move(100, 100, absolute=False, duration=0.5)
    time.sleep(2.5)
    mouse.click('right')
    mouse.move(-100, -100, absolute=False, duration=0.5)
    time.sleep(2.5)
    mouse.click('right')