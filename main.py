
#author: Daghlny

import g2agame
import g2afile
import sendEmail
import sys
import time
import platform
import os
from g2agame import G2AGame

pricefile = "price.json"
configfile = "conf.json"
config = dict()

def notice(gameName, lowestprice):
    notice_method = config["notice_method"]
    if notice_method == "email":
        rec_email_addr = config["rec_email_addr"]
        sender_email_addr = config["sender_email_addr"]
        sender_email_pw   = config["sender_email_pw"]
        sender_smtp_addr  = config["sender_smtp_addr"]
        sendEmail.send_notice_email(rec_email_addr, sender_email_addr, sender_email_pw, sender_smtp_addr, gameName, lowestprice)

if __name__ == "__main__":
    if not (platform.system() == "Linux"):
        print("This script only can run in linux operating system.")
        os._exit(0)

    # load the configures from file
    config = g2afile.readConfig(configfile)
    backend = config["run_backend"]
    if backend:
        try:
            if os.fork() > 0:
                os._exit(0)
        except OSError, error:
            print("fork failed:%d (%s)"%(error.errno, error.strerror))
            os._exit(1)
    notice_method = config["notice_method"]
    gamelist = config["gamelist"]
    Tinterval = config["time interval"]
    print("start init lowest price\n")
    games = []
    for game in gamelist:
        gameurl = gamelist[game]["link"]
        threshold = gamelist[game]["threshold"]
        gID = g2agame.getGameEntryID(gameurl)
        g = G2AGame(game, threshold, threshold, gameurl, gID)
        games.append(g)
        g2afile.writeGamePrice(pricefile, game, threshold)
    while 1:
        for game in games:
            Lower = game.UpdateLowestPrice()
            if Lower & game.IfLowerThreshold():
                print("GameName:"+game.name+" new Lowest Price:"+game.lowest)
                notice(game.name, game.lowest)
        time.sleep(Tinterval)
