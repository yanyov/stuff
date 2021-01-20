# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:33:24 2021

@author: asen.yanyov
"""

#pip install mouse
import mouse
# move 100 right and 100 down with a duration of 0.5 seconds
while True:
    mouse.move(100, 100, absolute=False, duration=0.5)
    mouse.move(-100, -100, absolute=False, duration=0.5)