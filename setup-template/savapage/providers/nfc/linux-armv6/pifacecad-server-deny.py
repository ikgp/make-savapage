#!/usr/bin/env python
'''
This file is part of the SavaPage project <http://savapage.org>.
Copyright (c) 2011-2015 Datraverse B.V.
Author: Rijk Ravestein.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

For more information, please contact Datraverse B.V. at this
address: info@datraverse.com
'''
import os
import time

hasPiFaceCad = False

try:
    import pifacecad as p

    cad = p.PiFaceCAD()
    cad.lcd.write("Nothing to print\ncheck your inbox")
    cad.lcd.backlight_on()

    hasPiFaceCad = True

except:
    pass

os.system('aplay --quiet beep-3.wav')

if hasPiFaceCad:
    time.sleep(4)
    cad.lcd.clear()
    cad.lcd.write("Swipe your card\nto release print")
