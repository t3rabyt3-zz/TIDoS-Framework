# coding: utf-8
#!/usr/bin/env python

import sys, platform, subprocess, time, os

from urllib2 import urlopen
from time import sleep
from subprocess import call
sys.path.append('tidos/')
from clickjack import *
from banner import *
from googleSearch import *
from UDoS import *
from info import *
from geoIP import *
from whoischeckup import *
from subdom import *
from subnet import *
from dnschk import *
from piweb import *
from nmap import *
from revip import *
from revdns import *
from links import *
from grabhead import *
from adminpanel import *
from zone import *
from honeypot import *

###############################
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
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
W  = '\033[1;0m'  # white (normal)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray
T  = '\033[1;93m' # tan
M = '\033[1;35;32m' # magenta
###############################

VersionNum = "2.5"

import scapy
import pip
import requests

os.system('clear')
if str(platform.system()) != "Linux":
    sys.exit(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "             You are not using a Linux Based OS! Linux is a must-have for this script!" + color.END)
if not os.geteuid() == 0:
    sys.exit(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "                           Must be run as root. :) " + color.END)
if 'no' in open('agree.txt').read():
    print color.BOLD + """
	TIDoS is a open-source tool developed as a royalty-free website penetration testing tool.

	I was developed by Pinaxx Robinson, known by the name @_tID aka The-Infected-Drake.

	This is to make you note that I am purely developed for Penetration Testing purposes (WhiteHat in the sense). The developer is not responsible for any damage or data loss due to my misuse. If you intend to use me for any BlackHat purposes, use it at your own risk, coz I am dangerous... ;)

	Also by using this tool, you agree to be a awesome person. Try to help others, strive not being a ScriptKiD, speak fairly to everyone, offer free hugs to everyone (provided the other person agrees in a mutual hug, don't FORCE xD), and never underestimate anyone.

	You can edit these scripts within me as per your own needs, provided you use it only for yourself. If u wanna publish me again in a reformed appearance, give the developer some credits...  :)
"""
    agree = raw_input(''+G+color.BOLD+ 'Do you agree to these terms and conditions? :> ' + color.END)
    if agree == "yes":
        print (''+G+ color.BOLD+'Awesome !!! Now drift ahead...' + color.END)
        time.sleep(3)
        FILE = open("agree.txt","w")
        FILE.write('yes')
        FILE.close()
    elif agree == "y":
        print (''+G+ color.BOLD+'   Awesome !!! Now drift ahead...' + color.END)
        time.sleep(3)
        FILE = open("agree.txt","w")
        FILE.write('yes')
        FILE.close()
    elif agree == "Y":
        print (''+G+ color.BOLD+'   Awesome !!! Now Drift Ahead...' + color.END)
        time.sleep(3)
        FILE = open("agree.txt","w")
        FILE.write('yes')
        FILE.close()
    else:
        print (''+R+color.BOLD+'[!] You have to agree!' + color.END)
        time.sleep(1)
        sys.exit()

#=============================================#
#          Actual coding in here              #
#=============================================#

os.system('clear')
banner()
def banner1():
	print""
	print color.BLUE + color.BOLD+"                             +=============================================+"
	print color.CYAN + color.BOLD+"                             | +-----------------------------------------+ |"
	print color.DARKCYAN + color.BOLD+"                             | |   Author: The-Infected-Drake (@_tID)    | |"
	print color.GREEN + color.BOLD+"                             | |               Version: 2.0              | |"
	print color.BLUE + color.BOLD+"                             | |         Website Pentesting Tool         | |"
	print color.RED + color.BOLD+"                             | |            1 Tool -> 23 choices         | |"
	print color.YELLOW + color.BOLD+"                             | |       Test the PEN, stay LEGAL !!!      | |"
	print color.CYAN + color.BOLD+"                             | +-----------------------------------------+ |"
	print color.BLUE + color.BOLD+"                             +=============================================+" + color.END

print color.BLUE +color.BOLD+ "                             +=============================================+"
time.sleep(0.3)
print color.CYAN + color.BOLD+"                             | +-----------------------------------------+ |"
time.sleep(0.5)
print color.DARKCYAN + color.BOLD+"                             | |   Author: The-Infected-Drake (@_tID)    | |"
time.sleep(0.5)
print color.WARNING + color.BOLD+"                             | |               Version: 2.0              | |"
time.sleep(0.5)
print color.GREEN + color.BOLD+"                             | |         Website Pentesting Tool         | |"
time.sleep(0.5)
print ""+ GR + color.BOLD+"                             | |            1 Tool -> 23 choices         | |"
time.sleep(0.5)
print ""+R + color.BOLD+"                             | |       Test the PEN, stay LEGAL !!!      | |"
time.sleep(0.5)
print color.CYAN + color.BOLD+"                             | +-----------------------------------------+ |"
time.sleep(0.3)
print color.BLUE + color.BOLD+"                             +=============================================+" + color.END
time.sleep(0.5)

def tidosmain():
    while True:
        try:
            main = raw_input(''+M+'                                    ' + color.BOLD + 'TID :>  ' + color.END)
            if main == "info":
		print ""+O+color.BOLD+"                    [!] Collecting info about your network..."
		time.sleep(0.5)
		print ""+G+color.BOLD+"                    [*] Info collected... Preparing results..."+color.END
		time.sleep(1)         
                info()
	    elif main == "geoip":
		time.sleep(0.5)
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
		geoIP()
	    elif main == "subdom":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
		subdom()
	    elif main == "grabhead":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
		grabhead()
	    elif main == "subnet":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
		subnet()
	    elif main == "dnschk":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
		dnschk()
	    elif main == "nmap":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
		nmapmain()
	    elif main == "pglink":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
		links()
	    elif main == "revip":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
		revip()
            elif main == "help":
                print ""+O+color.BOLD+"                      +================================================================+"
                print ""+C+color.BOLD+"                                                  ╦ ╦╔═╗╦  ╔═╗"
                print ""+C+color.BOLD+"                                                  ╠═╣║╣ ║  ╠═╝"
                print ""+C+color.BOLD+"                                                  ╩ ╩╚═╝╩═╝╩  "
                print ""+O+color.BOLD+"                      +================================================================+"
                time.sleep(0.2)
                print ""+C+color.BOLD+"                         [1] help "+GR+"- Displays this help message"
                time.sleep(0.05)
                print ""+P+color.BOLD+"                         [2] banner "+GR+"- Prints a new banner"
                time.sleep(0.05)                
                print ""+G+color.BOLD+"                         [3] cls "+GR+"- Clears the screen"
                time.sleep(0.05)
                print ""+R+color.BOLD+"                         [4] info "+GR+"- Displays information about your Network"
                time.sleep(0.05)
                print ""+C+color.BOLD+"                         [5] piweb "+GR+"- Pings a website"
		time.sleep(0.05)
		print ""+M+color.BOLD+"                         [6] grabhead"+GR+" - Grabs the HTTP Headers of a Website"
		time.sleep(0.05)
		print ""+T+color.BOLD+"                         [7] whois"+GR+" - Get WHOIS info of a website"
		time.sleep(0.05)
		print ""+P+color.BOLD+"                         [8] revip"+GR+" - Do a Reverse IP LookUP of a Website"
		time.sleep(0.05)
		print ""+M+color.BOLD+"                         [9] revdns"+GR+" - Does a Reverse DNS LookUP of Website"
		time.sleep(0.05)
		print ""+R+color.BOLD+"                         [10] geoip"+GR+" - Does a GeoIP Lookup of the website"
		time.sleep(0.05)
		print ""+C+color.BOLD+"                         [11] subdom"+GR+" - Launches the Sub-Domain scanner"
		time.sleep(0.05)
		print ""+G+color.BOLD+"                         [12] subnet"+GR+" - Does a SubNet Scan of a Website"
		time.sleep(0.05)
		print ""+P+color.BOLD+"                         [13] dnschk"+GR+" - Starts up a DNS LookUP of a Website"
		time.sleep(0.05)
                print ""+B+color.BOLD+"                         [14] gsearch"+GR+" - Search Google for a DORK or a Query"
                time.sleep(0.05)
		print ""+O+color.BOLD+"                         [15] pglink"+GR+" - Dumps a list of the links with Website"
		time.sleep(0.05)
		print ""+C+color.BOLD+"                         [16] adminpnl"+GR+" - Hunt for the Admin Panel of a Website"
		time.sleep(0.05)
		print ""+B+color.BOLD+"                         [17] clikjak"+GR+" - Test a website for clickjackabilities"
		time.sleep(0.05)
		print ""+O+color.BOLD+"                         [18] honeypot"+GR+" - Test whether a IP is a honeypot"
		time.sleep(0.05)
		print ""+R+color.BOLD+"                         [19] zonetrans"+GR+" - Test a Web for ZoneTransfer Vulerability"
		time.sleep(0.05)
		print ""+G+color.BOLD+"                         [20] nmap"+GR+" - For Advanced Reconnaissance on a Website" 
		time.sleep(0.05)
                print ""+C+color.BOLD+"                         [21] fl00d"+GR+" - Flood a website at the UDP level dead"
                time.sleep(0.05)
                print ""+R+color.BOLD+"                         [22] exit"+GR+" - Quits this tool "
                time.sleep(0.05)
                print ""+P+color.BOLD+"                         [23] contact"+GR+" - Contact me for queries :)"
                time.sleep(0.05)
                print ""+O+color.BOLD+"                      +=================================================================+"
            elif main == "zonetrans":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
                zone()
            elif main == "honeypot":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
                honeypot()
            elif main == "adminpnl":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
                adminpanel()
            elif main == "clikjak":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
                clickjack()
            elif main == "fl00d":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
                UDoS()
	    elif main == "whois":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
		whoischeckup()
            elif main == "gsearch":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
                googleSearch()
	    elif main == "revdns":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
		revdns()
            elif main == "contact":
                print(''+O+color.BOLD+'                 +=====================================================================+' + color.END)
                print(''+T+color.BOLD+'                                      ╔═╗╔═╗╔╗╔╔╦╗╔═╗╔═╗╔╦╗  ╔╦╗╔═╗')
                time.sleep(0.1)
                print(''+T+color.BOLD+'                                      ║  ║ ║║║║ ║ ╠═╣║   ║   ║║║║╣ ')
                time.sleep(0.1)
                print(''+T+color.BOLD+'                                      ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝ ╩   ╩ ╩╚═╝')
                time.sleep(0.1)
                print(''+O+color.BOLD+'                 +=====================================================================+' + color.END)
                print(''+T+color.BOLD+'                          Facebook :>'+GR+'' + color.BOLD + ' https://www.facebook.com/pinaxx.robinson' + color.END)
                time.sleep(0.3)
                print(''+T+color.BOLD+'                          Instagram :>'+GR+'' + color.BOLD + ' @tID - www.instagram.com/the_infected_drake'+color.END)
                time.sleep(0.3)
                print(''+T+color.BOLD+'                          Email me :>'+GR+'' + color.BOLD + ' robinsonpinaxx2000@gmail.com' + color.END)
                print(''+O+color.BOLD+'                 +=====================================================================+' + color.END)
            elif main == "piweb":
                piweb()
            elif main == "banner":
                print (""+C+color.BOLD+"                                   ╔╗╔╔═╗╦ ╦  ╔╗ ╔═╗╔╗╔╔╗╔╔═╗╦═╗")
                time.sleep(0.1)
                print (""+C+color.BOLD+"                                   ║║║║╣ ║║║  ╠╩╗╠═╣║║║║║║║╣ ╠╦╝")
                time.sleep(0.1)
                print (""+C+color.BOLD+"                                   ╝╚╝╚═╝╚╩╝  ╚═╝╩ ╩╝╚╝╝╚╝╚═╝╩╚═")
                time.sleep(0.5)
                os.system('clear')
                banner()
                banner1()
            elif main == "cls":
                time.sleep(0.1)
                print (""+C+color.BOLD+"                                ╔═╗╦  ╔═╗╔═╗╦═╗  ╔═╗╔═╗╦═╗╔═╗╔═╗╔╗╔")
                time.sleep(0.1)
                print (""+C+color.BOLD+"                                ║  ║  ║╣ ╠═╣╠╦╝  ╚═╗║  ╠╦╝║╣ ║╣ ║║║")
                time.sleep(0.1)
                print (""+C+"                                ╚═╝╩═╝╚═╝╩ ╩╩╚═  ╚═╝╚═╝╩╚═╚═╝╚═╝╝╚╝")
                time.sleep(0.5)
                os.system('clear')
            elif main == "exit":
                print (''+O+'                   +==============================================================+' + color.END)
                print (""+C+color.BOLD+"                                          ╔═╗ ╦ ╦╦╔╦╗")
                time.sleep(0.1)
                print (""+C+color.BOLD+"                                          ║═╬╗║ ║║ ║")
                time.sleep(0.1) 
                print (""+C+color.BOLD+"                                          ╚═╝╚╚═╝╩ ╩" + color.END)
                time.sleep(0.1)
                print(''+O+color.BOLD+'                    +==============================================================+' + color.END)
                print (""+R+color.BOLD+"                                         [*] \033[91m" + "Exiting..." + color.END)
                time.sleep(0.3)
                print (""+GR+color.BOLD+"                                [*] " + "Remember the Infected Drake" + color.END)
                time.sleep(0.3)
                print (""+O+color.BOLD+"                                        [*] " + "GoodBye... ^_^" + color.END)
                time.sleep(0.3)
                print (''+O+color.BOLD+'                    +==============================================================+' + color.END)
                sys.exit()
            elif main == "":
                print (""+R+"                             [!] " + color.UNDERLINE + "\033[91m" + "Enter an option properly..." + color.END)
	    elif main == "1": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "2": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "3": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "4": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "5": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "6": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "7": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "8": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "9": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "10": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "11": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "12": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "13": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "14": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "15": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "16": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "17": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "18": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "19": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "20": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
	    elif main == "21": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
            else:
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the corresponding keyword..."+color.END)
        except KeyboardInterrupt:
                print (""+R+"\n                             [!] " + color.UNDERLINE + "\033[91m" + " Use 'exit' to close the tool!" + color.END)
                tidosmain()
tidosmain()
