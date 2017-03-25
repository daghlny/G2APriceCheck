
#author: Daghlny

import json
import requests
import os
import re
import g2afile

prefix_gameID_url = "https://www.g2a.com/marketplace/product/auctions/?id="

# /param gameID like 67373
def get_lowest_price(gameID):
    r = requests.get(prefix_gameID_url+gameID)
    j = json.loads(r.text)
    j = j["a"]
    priceset = []
    for k in j:
        price = j[k]["f"]
        priceset.append(price)
    priceset.sort()
    return float(priceset[0][0:-2])

# /param gameurl like "https://www.g2a.com/glove-case-key.html"
def getGameEntryID(gameurl):
    gamesite = requests.get(gameurl)
    jf = open("gameidfile.txt", "w+")
    gamehtml = gamesite.text.encode("utf-8").strip()
    jf.write(gamehtml)
    jf.close()
    pattern = re.compile("productID = \S+;")
    entryID = re.findall(pattern, gamehtml)
    print(entryID)
    if len(entryID) >= 1:
        return entryID[0][12:-1]
    else:
        print("error in getGameEntryID()")

def checkIfPriceLower(filename, gamename, gameprice):
    curprice = g2afile.readGamePrice(filename, gamename)
    if gameprice < curprice:
        g2afile.writeGamePrice(filename, gamename, gameprice)
        return True
    else:
        return False