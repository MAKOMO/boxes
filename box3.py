#!/usr/bin/python3
# Copyright (C) 2013-2014 Florian Festi
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from boxes import *

class Box(Boxes):
    def __init__(self, x, y, h, **kw):
        self.x, self.y, self.h = x, y, h
        Boxes.__init__(self, width=x+y+40, height=y+2*h+50, **kw)

    def render(self):
        x, y, h = self.x, self.y, self.h
        t = self.thickness

        d2 = [Bolts(2)]
        d3 = [Bolts(3)]

        d2 = d3 = None

        self.moveTo(t, t)
        self.rectangularWall(x, h, "FFeF", bedBolts=d2, move="right")
        self.rectangularWall(y, h, "Feef", bedBolts=d3, move="up")
        self.rectangularWall(y, h, "Feef", bedBolts=d3)
        #self.rectangularWall(x, h, "FFeF", bedBolts=d2, move="left up")
        
        self.rectangularWall(x, y, "efff", bedBolts=[d2, d3, d2, d3], move="left")
        #self.rectangularWall(x, y, "ffff", bedBolts=[d2, d3, d2, d3])

        self.close()

t = 6.0
b = Box(380-2*t, 370-2*t, 120-t, thickness=t)
b.edges["f"].settings.setValues(b.thickness, space=3, finger=3,
                                surroundingspaces=1)
b.render()