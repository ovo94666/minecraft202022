# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:59:39 2020

@author: user
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
x,y,z = mc.player.getTilePos()
while True:
      hits = mc.events.pollBlockHits()
      if len(hits) > 0 :
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z

        stone = mc.getBlock(x,y,z)
        if hit (stone) : mc.spawnEntity(x,y,z,93)
    time.sleep (0.3) mc.spawnEntity(x,y,z,93)
   
                        mc.createExplosion(x,y,z,power=100)
                        mc.spawnEntity(x,y,z,93)
                        time.sleep (0.3)

 
