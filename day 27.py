# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:08:18 2020

@author: user
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

USERNAME = input("YOUR USERNAME:")

MESSAGE = input("WHAT YOU WANT TO SAY :")


mc.postToChat("<"+USERNAME+">"+MESSAGE)