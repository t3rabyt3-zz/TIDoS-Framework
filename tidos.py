#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework 

import sys
import platform
import os
import subprocess
import logging
import time
import scapy
from scapy.all import *
from time import sleep
from subprocess import call
sys.path.append('core/')
from impo import *
from logging import getLogger, ERROR
getLogger("scapy.runtime").setLevel(ERROR)

agree()

os.system('clear')
loadstyle()
sleep(2)
tid()
os.system('clear')
banner()
banner1()

web = raw_input(''+O+' [#] Target web address :> '+GR+'')
global web
if 'http' not in web:
	mo = raw_input(GR+' [#] Does this website use SSL? (y/n) :> ')
	if mo == 'y' or mo == 'Y':
		web = 'https://'+web
	elif mo == 'n':
		web = 'http://'+web
def tidosmain(web):

    while True:

        try:

	    print ''+O+'\n Choose from the options below :'
	    print ''+B+'\n [1] \033[1;36mReconnaissance'
	    print ''+B+' [2] \033[1;36mScanning & Enumeration'
	    print ''+B+' [3] \033[1;36mVulnerability Analysis'
	    print ''+B+' [4] \033[1;36mExploitation (beta)'
	    print ''+B+' [5] \033[1;36mPost-Exploitation (alpha)\n'
	    zop = raw_input(''+GR+' [#] \033[1;4mTID\033[0m'+GR+' :> ' + color.END)

	    if zop == '1':

		print '\n'
		footprint(web)

	    elif zop == '2':

		print '\n'
		scanenum(web)

	    elif zop == '3':

		print '\n'
		vuln(web)

	    elif zop == '4':

		print '\n'
		print '  +------------------+'
		print '  |   EXPLOITATION   |'
		print '  +------------------+'
		print ''+O+'\n  Presently not updated...\n\n'

	    elif zop == '5':

		print '[!] To be shortly available here :)\n\n'
	
        except KeyboardInterrupt:
                print (""+R+"\n[!] " + color.UNDERLINE + "\033[91m" + "User Interruption detected!" + color.END)
                print ''+GR+'[!] Stopping jobs...'
		time.sleep(0.4)
		print ''+B+'[!] Goodbye, see ya!\n\n'
		sys.exit(0)

tidosmain(web)
