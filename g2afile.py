
#author: Daghlny

import sys
import os
import json

def writeGamePrice(filename, gamename, gameprice):
    file = open(filename, "r+")
    gamejson = json.load(file)
    gamejson[gamename] = gameprice
    file.close()
    file = open(filename, "w")
    file.write(json.dumps(gamejson, indent=4))
    file.close()

# /return if @gamename doesn't exist in current data file, return -1
def readGamePrice(filename, gamename):
    file = open(filename, "r+")
    gamejson = json.load(file)
    if gamename in gamejson:
        return float(gamejson[gamename])
    else:
        return -1

# Remember: the last property should not add "," of sub class in json format
def readConfig(filename):
    file = open(filename, "r")
    config = json.load(file)
    file.close()
    return config