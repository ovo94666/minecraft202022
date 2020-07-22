# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:46:43 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    mc.setBlocks(x,y,z,x,y+4,z,17)
    
x,y,z = mc.player.getTilePos()
plantTree(x,y,z)
plantTree(x,y,z+5)
plantTree(x,y,z+10)
plantTree(x,y,z+15)
plantTree(x,y,z+20)
plantTree(x,y,z+25)
plantTree(x,y,z+30)
plantTree(x,y,z+35)
plantTree(x,y,z+40)
    