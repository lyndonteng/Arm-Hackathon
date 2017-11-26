# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 07:18:00 2017

@author: Lyndon Teng
"""

import numpy as np

def xyznumpyFromDict(dictList):
    matches = ["x","y","z"]
    return[np.array(dict[list(dict)[0]]) for dict in dictList if list(dict)[0] in matches]

def lasernumpyFromDict(dictList):
    matches = ["laser"]
    return[np.array(dict[list(dict)[0]]) for dict in dictList if list(dict)[0] in matches]

def dotp(vector):
    dort=np.dot(np.array([0,0,1]))
    return dort

#def addDisplacement(dictList):
 #   """
  #     Adds a displacement dictionary to the dict list, removes the acceleration and laser readings
   # """
    #variables=xyznumpyFromDict(dictList)
    #laser=lasernumpyFromDict(dictList)
        
    #deltaheight=[]
    #for n in len(laser):
    #    deltaheight.append(laser[n]-laser[n-1])
    #list_scalar_z=dotp([variables[0],variables[1],variables[2]])
    #    
    #speedlist=list_scalar_z*(deltaheight/0.05) #timestep
    #output_str=
    #pandaCsv(output_str, 'test', r'D:\OneDrive\Documents\Part 1A\Hackathon Data')