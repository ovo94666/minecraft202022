# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:25:25 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
import random,time
while True:
    x = pos.x+random.uniform(-20,20)
    y = pos.y
    z = pos.z+random.uniform(-20,20)
    
    mc.spawnEntity(x,y,z,93)
    time.sleep (0.3)              
    