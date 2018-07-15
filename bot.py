#!/usr/bin/python
# -*- coding: utf-8 -*-



import time
import random

random.seed()
while True:
    n = random.uniform(172800, 864000)
    print('Привет')
    time.sleep(n)   # Delay for 1 minute (60 seconds).
