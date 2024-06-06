#!/usr/bin/env python3

import random
import time

DELAY = 10./19200 # 10/19200, this is 10 bits per symbol

while True:
    print(random.choice(["\\", "/"]), end="", flush=True)
    time.sleep(DELAY)