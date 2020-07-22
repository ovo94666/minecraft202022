# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:37:41 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

blockid = int(input("YOUR BLOCK ID :" ))
mc.setBlock(x,y-1,z,blockid)