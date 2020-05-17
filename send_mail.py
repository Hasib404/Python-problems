import smtplib
from time import strftime


fromaddr = ""
toaddr = ""
serveraddr = ""
usetls = False
usessl = False
serverport = 25
SMTP_USER = ""
SMTP_PASS = ""
debuglevel = 1
verbose = True
now = strftime("%Y-%m-%d %H:%M:%S")
msg = "From: %s\r\nTo: %s\r\nSubject: Test Message from smtptest at %s\r\n\r\nTest message from the smtptest tool sent at %s" % (fromaddr, toaddr, now, now)
if verbose:
    print('usetls:', usetls)
    print('usessl:', usessl)
    print('from address:', fromaddr)
    print('to address:', toaddr)
    print('server address:', serveraddr)
    print('server port:', serverport)
    print('smtp username:', SMTP_USER)
    print('smtp password: *****')
    print('smtplib debuglevel:', debuglevel)
    print("-- Message body ---------------------")
    print(msg)
    print("-------------------------------------")
server = smtplib.SMTP()
server.set_debuglevel(debuglevel)
server.connect(serveraddr, serverport)
server.ehlo()
if usetls: server.starttls()
server.ehlo()
if SMTP_USER != "":
    server.login(SMTP_USER, SMTP_PASS)
    server.sendmail(fromaddr, toaddr, msg)
else:
    server.sendmail(fromaddr, toaddr, msg)
server.quit()
