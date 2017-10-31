# coding: utf-8
#!/usr/bin/env python
import sys, platform, subprocess, time, os
from urllib2 import urlopen
from time import sleep
from subprocess import call
sys.path.append('tidos/')
from webex import *
from banner import *
from googleSearch import *
from UDoS import *
from info import *
from geoIP import *
from whoischeckup import *
from subdom import *
from subnet import *
from dnschk import *
from nping import *
from piweb import *
from nmap import *
from trcrt import *
from revip import *
from revdns import *
from links import *
from grabhead import *

VersionNum = "2.0"

try:
    import scapy
    import pip
    import google
    import requests
    import argparse
except ImportError as e:
    print (color.UNDERLINE + "\033[91m" + "You don't have some modules installed! \nPlease run setup.py to install this tool fully! " + color.END)
    print "Error: {}".format(e)
    print "Execute: pip install (module name)"
    if (e) == "DependencyWarning":
        os.system("sudo apt-get update")
        os.system("apt-get remove python-pip")
        os.system("easy_install pip")
    elif (e) == "Unable to locate package lib32ncurses5":
        os.system("sudo apt-get update")
        os.system("sudo apt-get install lib32ncurses5 lib32bz2-1.0")
    sys.exit()
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
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta
###############################

os.system('clear')
if str(platform.system()) != "Linux":
    sys.exit(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "             You are not using a Linux Based OS! Linux is a must-have for this script!" + color.END)
if not os.geteuid() == 0:
    sys.exit(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "                           Must be run as root. :) " + color.END)
if 'no' in open('agree.txt').read():# take out the treaty/
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
os.system('clear')
banner()
def banner1():
	print""
	print color.BLUE + color.BOLD+"                             +=============================================+"
	print color.CYAN + color.BOLD+"                             | +-----------------------------------------+ |"
	print color.DARKCYAN + color.BOLD+"                             | |   Author: The-Infected-Drake (@_tID)    | |"
	print color.WARNING + color.BOLD+"                             | |               Version: 2.0              | |" 
	print color.PURPLE + color.BOLD+"                             | |      Team  : Dark Error Cyber Team      | |"
	print color.BLUE + color.BOLD+"                             | |         Website Pentesting Tool         | |"
	print color.YELLOW + color.BOLD+"                             | |            1 Tool -> 21 choices         | |"
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
print color.PURPLE + color.BOLD+"                             | |      Team  : Dark Error Cyber Team      | |"
time.sleep(0.5)
print color.GREEN + color.BOLD+"                             | |         Website Pentesting Tool         | |"
time.sleep(0.5)
print color.YELLOW + color.BOLD+"                             | |            1 Tool -> 21 choices         | |"
time.sleep(0.5)
print color.DARKCYAN + color.BOLD+"                             | |       Test the PEN, stay LEGAL !!!      | |"
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
            elif main == "webex":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
                webex()
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
		nmap()
	    elif main == "pglink":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
		links()
	    elif main == "nping":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
		nping()
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
                print ""+C+color.BOLD+"                          [1] help "+GR+"- Displays this help message"
                time.sleep(0.05)
                print ""+P+color.BOLD+"                          [2] banner "+GR+"- Prints a new banner"
                time.sleep(0.05)                
                print ""+G+color.BOLD+"                          [3] cls "+GR+"- Clears the screen"
                time.sleep(0.05)
                print ""+T+color.BOLD+"                          [4] info "+GR+"- Displays information about your Network"
                time.sleep(0.05)
                print ""+C+color.BOLD+"                          [5] piweb "+GR+"- Pings a website"
                time.sleep(0.205)
		print ""+R+color.BOLD+"                          [6] nping"+GR+" - Perform a nPing(NMap-Ping) on a Website"
		time.sleep(0.05)             
                print ""+T+color.BOLD+"                          [7] webex"+GR+" - Check whether a website exists or not"
                time.sleep(0.05)
		print ""+M+color.BOLD+"                          [8] grabhead"+GR+" - Grabs the HTTP Headers of a Website"
		time.sleep(0.05)
		print ""+B+color.BOLD+"                          [9] trace"+GR+" - Use MTR for Advanced TraceRoute of Web"
		time.sleep(0.05)
		print ""+T+color.BOLD+"                          [10] whois"+GR+" - Get WHOIS info of a website"
		time.sleep(0.05)
		print ""+P+color.BOLD+"                          [11] revip"+GR+" - Do a Reverse IP LookUP of a Website"
		time.sleep(0.05)
		print ""+M+color.BOLD+"                          [13] revdns"+GR+" - Does a Reverse DNS LookUP of Website"
		time.sleep(0.05)
		print ""+R+color.BOLD+"                          [12] geoip"+GR+" - Does a GeoIP Lookup of the website"
		time.sleep(0.05)
		print ""+C+color.BOLD+"                          [13] subdom"+GR+" - Launches the Sub-Domain scanner"
		time.sleep(0.05)
		print ""+G+color.BOLD+"                          [14] subnet"+GR+" - Does a SubNet Scan of a Website"
		time.sleep(0.05)
		print ""+P+color.BOLD+"                          [15] dnschk"+GR+" - Starts up a DNS LookUP of a Website"
		time.sleep(0.05)
                print ""+B+color.BOLD+"                          [16] gsearch"+GR+" - Search Google about a Website"
                time.sleep(0.05)
		print ""+C+color.BOLD+"                          [17] pglink"+GR+" - Dumps a list of the links with Website"
		time.sleep(0.05)
		print ""+G+color.BOLD+"                          [18] nmap"+GR+" - Shoots up NMap Port Scan on a Website" 
		time.sleep(0.05)
                print ""+O+color.BOLD+"                          [19] fl00d"+GR+" - Flood a website at the UDP level dead"
                time.sleep(0.05)		
                print ""+R+color.BOLD+"                          [20] exit"+GR+" - Quits this tool "
                time.sleep(0.05)
                print ""+M+color.BOLD+"                          [21] contact"+GR+" - Contact me for queries :)"
                time.sleep(0.05)
                print ""+O+color.BOLD+"                     +=================================================================+"
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
	    elif main == "trace":
		print ""+P+color.BOLD+"                    [!] Preparing scripts about the info you requested..."+color.END
		time.sleep(0.3)
		print ""+G+color.BOLD+"                    [*] Launching module..."+color.END
		time.sleep(1)
		trcrt()
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
                print (""+M+color.BOLD+"                                         [*] \033[91m" + "Exiting..." + color.END)
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
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly...")
	    elif main == "2": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly...")
	    elif main == "3": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly...")
	    elif main == "4": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly...")
	    elif main == "5": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly...")
	    elif main == "6": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly...")
	    elif main == "7": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly...")
	    elif main == "8": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly...")
	    elif main == "9": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly")
	    elif main == "10": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly")
	    elif main == "11": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly")
	    elif main == "12": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly")
	    elif main == "13": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly")
	    elif main == "14": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly")
	    elif main == "15": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly")
	    elif main == "16": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly")
	    elif main == "17": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly")
	    elif main == "18": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly")
	    elif main == "19": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly")
	    elif main == "20": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly")
	    elif main == "21": 
		print (R+"                               [!] " + color.UNDERLINE + "\033[91m" + "Enter the keyword properly")
            else:
                print (""+R+"                              [!] " + color.UNDERLINE + "\033[91m" + "That is not an option! Type 'help'" + color.END)
        except KeyboardInterrupt:
                print (""+R+"                             [!] " + color.UNDERLINE + "\033[91m" + " Use 'exit' to close the tool!" + color.END)
                tidosmain()
tidosmain()
