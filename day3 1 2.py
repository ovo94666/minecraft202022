# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 09:24:27 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0 :
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
        block = mc.getBlock(x,y,z)
        mc.postToChat("ID:"+str(block))
        stone = mc.getBlock(x,y,z,1)
        if block == 1 :
                        mc.setBlock(x,y,z,)