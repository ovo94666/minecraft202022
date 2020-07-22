# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:19:00 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x,y,z = mc.player.geTilePos()
for i in range (20):
    time.sleep (0.10)
    mc.setBlock(x+i,y-1,z+i,41)
    