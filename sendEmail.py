
#author: Daghlny

import email
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# this function is copied from @liaoxuefeng
def _format_addr(s):
    name, addr = email.utils.parseaddr(s)
    return email.utils.formataddr((\
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if   isinstance(addr, unicode) else addr))


def send_notice_email(recaddr, senderaddr, senderpw, sendersmtp, game, price):
    msg = MIMEText("the game <b>"+game+"</b>'s price is <b>"+str(price)+"</b> now", 'html', 'utf-8')
    msg['from'] = _format_addr(u'G2APriceNoticer <%s>' % senderaddr)
    msg['To'] = _format_addr(u'G2APriceReceiver <%s>' % recaddr)
    msg['Subject'] = Header(u'From G2A Gmae Price Alert', 'utf-8').encode()

    server = smtplib.SMTP(sendersmtp, 25)
    server.set_debuglevel(1)
    server.login(senderaddr, senderpw)
    server.sendmail(senderaddr, recaddr, msg.as_string())
    server.quit()