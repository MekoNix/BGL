import os,time
# netsh wlan show all  | find "BSSID" - find  BSSID only of near AP
# netsh wlan show interfaces | find "BSSID" - find BSSID only connected AP

f = open('settings.vnl', 'w')
f.write("""BSSID of near AP 
""")
netsh = os.popen('netsh wlan show all  | find "BSSID"')
for id in netsh.readlines():
    f.write(id)
f.close()