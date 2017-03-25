
#author: Daghlny

import sys
import os
import json

def writeGamePrice(filename, gamename, gameprice):
    file = open(filename, "rw+")
    gamejson = json.load(file)
    gamejson[gamename] = gameprice
    file.write(json.dumps(gamejson, indent=4))
    file.close()

# /return if @gamename doesn't exist in current data file, return -1
def readGamePrice(filename, gamename):
    file = open(filename, "rw+")
    gamejson = json.load(file)
    if gamename in gamejson:
        return float(gamejson[gamename])
    else:
        return -1

def readConfig(filename):
    file = open(filename, "r")
    config = json.load(file)
    file.close()
    return config