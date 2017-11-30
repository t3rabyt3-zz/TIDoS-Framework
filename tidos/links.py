# coding: utf-8
#!/usr/bin/env python
import urllib, urllib2, requests, time
from time import sleep
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan

def links():
    print ""
    print color.CYAN+color.BOLD+"                                      88     88 88b 88 88  dP .dP'Y8 "
    time.sleep(0.1)
    print color.CYAN+color.BOLD+"                                      88     88 88Yb88 88odP  `Ybo.' "
    time.sleep(0.1)
    print color.CYAN+color.BOLD+"                                      88  .o 88 88 Y88 88'Yb  o.`Y8b "
    time.sleep(0.1)
    print color.CYAN+color.BOLD+"                                      88ood8 88 88  Y8 88  Yb 8bod8P' "
    time.sleep(0.1)   
    print ""                                                                  
    print ""+B+color.BOLD+"                      +======================================================+"
    time.sleep(0.1)
    print(''+GR+color.BOLD+'                              Enter website address for the Link LookUP')
    time.sleep(0.1)
    print(''+B+color.BOLD+'                      +======================================================+')
    time.sleep(0.3)
    h = raw_input(''+ T + color.BOLD + '                                 Website :> ' + color.END)
    time.sleep(0.4)
    print('' + GR + color.BOLD + '                                    Lookup begins...')
    time.sleep(0.2)
    print(""+ GR + color.BOLD + "                                [~] Result: "+color.YELLOW+color.BOLD+"════════════════╗" + color.END)
    print(""+ color.YELLOW + color.BOLD + "     ╔══════════════════════════════════════════════════════╝")            
    print(""+ color.YELLOW + color.BOLD + "     ║")
    print(""+ color.YELLOW + color.BOLD + "     ▽")
    domains = [h]
    for dom in domains:
        text = requests.get('http://api.hackertarget.com/pagelinks/?q=' + dom).text
	resultlinks = str(text)
	print(""+G+ color.BOLD + resultlinks)
