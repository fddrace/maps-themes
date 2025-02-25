#!/usr/bin/env python3
"""
    chillber_dark based on chillber

    dark design by cyberFighter
"""

import sys
import twmap

if len(sys.argv) != 3:
    print("usage: chillber_dark.py chillber.map chillber_dark.map")
    sys.exit(0)


m = twmap.Map(sys.argv[1])

#background lamao
m.groups[0].layers[0].quads[0].colors = [(148, 73, 50, 255), (148, 73, 50, 255),
                                         (162, 129, 111, 255), (162, 129, 111, 255)]

#plotbg
m.groups[10].layers[0].color = (214, 193, 142, 100)

#alleybg
m.groups[11].layers[1].color = (49, 60, 60, 255)

#caves
m.groups[11].layers[2].color = (166, 166, 166, 255)
m.groups[11].layers[4].color = (242, 242, 242, 255)

#doodads
m.groups[11].layers[3].color = (162, 162, 162, 255)
m.groups[11].layers[5].color = (234, 234, 234, 255)
m.groups[11].layers[6].color = (234, 234, 234, 255)
m.groups[11].layers[7].color = (234, 234, 234, 255)
m.groups[11].layers[8].color = (234, 234, 234, 255)
m.groups[11].layers[9].color = (234, 234, 234, 255)
m.groups[11].layers[10].color = (234, 234, 234, 255)
m.groups[11].layers[11].color = (234, 234, 234, 255)
m.groups[11].layers[12].color = (234, 234, 234, 255)
m.groups[16].layers[0].color = (234, 234, 234, 255)

#switch
m.groups[15].layers[0].color = (198, 198, 198, 255)

#blocks
m.groups[18].layers[0].color = (214, 193, 142, 255)
m.groups[18].layers[2].color = (213, 213, 213, 255)
m.groups[18].layers[3].color = (231, 182, 231, 185)
m.groups[18].layers[4].color = (214, 193, 142, 255)
m.groups[18].layers[5].color = (195, 195, 195, 255)
m.groups[18].layers[6].color = (162, 144, 99, 255)
m.groups[18].layers[7].color = (140, 140, 140, 255)
m.groups[18].layers[8].color = (214, 193, 142, 255)
m.groups[18].layers[9].color = (234, 234, 234, 255)
m.groups[19].layers[9].color = (162, 144, 99, 255)

#logo
m.groups[18].layers[11].quads[0].colors = [(213, 213, 213, 255), (213, 213, 213, 255),
                                         (213, 213, 213, 255), (213, 213, 213, 255)]

m.save(sys.argv[2])

