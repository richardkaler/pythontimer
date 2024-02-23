# Copyright 2023 Richard Kaler 

# This script is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 3 of the License, or (at
# your option) any later version.

# This script is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

#NOTE: this script is straightforward - no bells and whistles. You simply run the code and a timer appears - which is sort of nifty in cases when you are in the CLI and have no GUI timer
#I will make this fancier as time goes by. I already have a bash timer that includes a feature to set the timer to expire but I just wrote this on the fly. 
#This will work on both Windows and Linux but I have yet to test it on Windows. It does work well on Linux with Python3. I tested it on Ubuntu, Jammy Jellyfish, LTS. Code version: 22.04

import datetime
import time
import os

current_time = datetime.datetime.now().strftime("%I:%M:%S %p")

# Print a string starting with the current time

def print_time():
    current_time = datetime.datetime.now().strftime("%I:%M:%S %P")
    formatted = f"\033[1;33m\033[20m{current_time}\033[0m"
    return formatted

while True:
    os.system('clear||cls')
    print(f"start: {current_time} ")
    print("current: "+print_time())
    time.sleep(1)
