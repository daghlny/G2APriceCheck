
#author: Daghlny

import g2agame
import g2afile
import sendEmail
import sys

pricefile = "price.json"
configfile = "conf.json"

if __name__ == "__main__":

    config = g2afile.readConfig(configfile)
    notice_method = config["notice_method"]
    gamelist = config["gamelist"]
    print("start init lowest price\n")
    for game in gamelist:
        gameurl = game["link"]
        threshold = game["threshold"]
        gID = g2agame.getGameEntryID(gameurl)
        lprice = g2agame.get_lowest_price(gID)
        g2afile.writeGamePrice(pricefile, game, lprice)




    gameurl = "https://www.g2a.com/glove-case-key.html"
    gameName = "Glove case key"
    gameID = g2agame.getGameEntryID(gameurl)
    lowestprice = g2agame.get_lowest_price(gameID)
    sendEmail.send_notice_email(rec_email_addr, sender_email_addr, sender_email_pw, sender_smtp_addr, gameName, lowestprice)

