# coding: utf-8
#!/usr/bin/env python

import urllib, urllib2, requests, time, socket
from time import sleep

###############################
class color:
   PURPLE = '\033[1;95m'
   CYAN = '\033[1;96m'
   DARKCYAN = '\033[1;36m'
   BLUE = '\033[1;94m'
   GREEN = '\033[1;92m'
   YELLOW = '\033[1;93m'
   RED = '\033[1;91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[1;4m'
   END = '\033[1;0m'
W  = '\033[1;0m'  # white (normal)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray
T  = '\033[1;93m' # tan
################################

def honeypot():
    print ""
    print color.CYAN+color.BOLD+"                         __ __   ___   ____     ___  __ __  ____   ___   ______ "
    print color.CYAN+color.BOLD+"                        |  |  | /   \ |    \   /  _]|  |  ||    \ /   \ |      |"
    print color.CYAN+color.BOLD+"                        |  |  ||     ||  _  | /  [_ |  |  ||  o  )     ||      |"
    print color.CYAN+color.BOLD+"                        |  _  ||  O  ||  |  ||    _]|  ~  ||   _/|  O  ||_|  |_|"
    print color.CYAN+color.BOLD+"                        |  |  ||     ||  |  ||   [_ |___, ||  |  |     |  |  |  "
    print color.CYAN+color.BOLD+"                        |  |  ||     ||  |  ||     ||     ||  |  |     |  |  |  "
    print color.CYAN+color.BOLD+"                        |__|__| \___/ |__|__||_____||____/ |__|   \___/   |__|  "
                                                        
    time.sleep(0.1)   
    print ""                                                                  
    print ""+O+color.BOLD+"                      +======================================================+"
    time.sleep(0.1)
    print(''+GR+color.BOLD+'                                 Enter IP address for the Link LookUP')
    time.sleep(0.1)
    print(''+O+color.BOLD+'                      +======================================================+')
    time.sleep(0.3)
    h = raw_input(''+ B + color.BOLD + '                               Website or IP :> ' + color.END)
    time.sleep(0.4)
    print('' + GR + color.BOLD +'                                [*] Detection initiated...\n')
    time.sleep(0.2)
    domains = [h]
    for dom in domains:
	    print ''+GR+'                                [*] Checking the Obtained IP Address...'        
	    ip=socket.gethostbyname(dom)
	    time.sleep(1) 
	    print ''+B+ '                                [*] Configuring related info...' 
            honey = "https://api.shodan.io/labs/honeyscore/" + ip + "?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by"
	    time.sleep(1)
	    print ''+C+ '                                [*] Detecting...'
	    time.sleep(1.5)
            phoney = urllib2.urlopen(honey).read()
            if '0.0' in phoney:
	    	print ''+P+ '                                [*] Reading info...'
		time.sleep(0.3)
                print ""+R+"\n                               [!] \033[1;32mHoneypot Probabilty: 0%\033[1;m"
		print ''
            if '0.1' in phoney:
	    	print ''+P+ '                                [*] Reading info...'
		time.sleep(0.3)
                print ""+R+"\n    			     [!] \033[1;32mHoneypot Probabilty: 10%\033[1;m"
		print ''
            if '0.2' in phoney:
	    	print ''+P+ '                                [*] Reading info...'
		time.sleep(0.3)
                print ""+R+"\n    			     [!] \033[1;32mHoneypot Probabilty: 20%\033[1;m"
		print ''
            if '0.3' in phoney:
	    	print ''+P+ '                                [*] Reading info...'
		time.sleep(0.3)
                print ""+R+"\n    			     [!] \033[1;32mHoneypot Probabilty: 30%\033[1;m"
		print ''
            if '0.4' in phoney:
	    	print ''+P+ '                                [*] Reading info...'
		time.sleep(0.3)
                print ""+R+"\n    			     [!] \033[1;32mHoneypot Probabilty: 40%\033[1;m"
		print ''
            if '0.5' in phoney:
	    	print ''+P+ '                                [*] Reading info...'
		time.sleep(0.3)
                print ""+R+"\n    			     [!] \033[1;31mHoneypot Probabilty: 50%\033[1;m"
		print ''
            if '0.6' in phoney:
	    	print ''+P+ '                                [*] Reading info...'
		time.sleep(0.3)
                print ""+R+"\n    			     [!] \033[1;31mHoneypot Probabilty: 60%\033[1;m"
		print ''
            if '0.7' in phoney:
	    	print ''+P+ '                                [*] Reading info...'
		time.sleep(0.3)
                print ""+R+"\n    			     [!] \033[1;31mHoneypot Probabilty: 70%\033[1;m"
		print ''
            if '0.8' in phoney:
	    	print ''+P+ '                                [*] Reading info...'
		time.sleep(0.3)
                print ""+R+"\n    			     [!] \033[1;31mHoneypot Probabilty: 80%\033[1;m"
		print ''
            if '0.9' in phoney:
	    	print ''+P+ '                                [*] Reading info...'
		time.sleep(0.3)
                print ""+R+"\n    			     [!] \033[1;31mHoneypot Probabilty: 90%\033[1;m"
		print ''
            if '1.0' in phoney:
	    	print ''+P+ '                                [*] Reading info...'
		time.sleep(0.3)
                print ""+R+"\n    			     [!] \033[1;31mHoneypot Probabilty: 100%\033[1;m"
		print ''

