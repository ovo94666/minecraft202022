# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:01:03 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0 :
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z

        stone = mc.getBlock(x,y,z,1)
        if hit (stone) :
                        mc.setBlock(x,y,z,41)