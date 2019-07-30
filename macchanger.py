#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Macchanger.py
#  
#  Copyright 2019 l1nt1p 
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os
import time
import sys
import subprocess
import colorama
from colorama import Fore, Back, Style
if os.name == 'nt':
    print('Sorry Macchanger doesnt currently support windows')
    print('Macchanger will close in ten seconds')
    time.sleep(10)
else:
    if sys.version_info[0] < 3:
        os.system('pip3 install -r requirements.txt')
    else:
        os.system('pip install -r requirements.txt')
    time.sleep(3)

arch = subprocess.check_output("ip route get 1.1.1.1 | awk '{print $5}'", shell=True);
print arch
time.sleep(3)
while True:
    print(Fore.GREEN + 'GOOD')
    os.system('sudo macchanger -r %s' % arch)

else:
    print(Fore.RED + 'ERROR')

exit()

