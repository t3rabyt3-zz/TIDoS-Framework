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
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray
T  = '\033[1;93m' # tan

def zone():
    print ""
    print color.CYAN+color.BOLD+'                    ____                           _____                                  '
    print color.CYAN+color.BOLD+'                   |_  /    ___    _ _      ___   |_   _|    _ _   __ _    _ _      ___   '
    print color.CYAN+color.BOLD+'                    / /    / _ \  | " \    / -_)    | |     | "_| / _` |  | " \    (_-<   '
    print color.CYAN+color.BOLD+'                   /___|   \___/  |_||_|   \___|   _|_|_   _|_|_  \__,_|  |_||_|   /__/_  '
    print color.CYAN+color.BOLD+'                 _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| '
    print color.CYAN+color.BOLD+'                 "`-0-0-""`-0-0-""`-0-0-""`-0-0-""`-0-0-""`-0-0-""`-0-0-""`-0-0-""`-0-0-" '
    time.sleep(0.1)   
    print ""                                                                  
    print ""+P+color.BOLD+"                      +======================================================+"
    time.sleep(0.1)
    print(''+GR+color.BOLD+'                              Enter website address for the Link LookUP')
    time.sleep(0.1)
    print(''+P+color.BOLD+'                      +======================================================+')
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
        text = requests.get('http://api.hackertarget.com/zonetransfer/?q=' + dom).text
	resultlinks = str(text)
	print(""+G+ color.BOLD + resultlinks)

