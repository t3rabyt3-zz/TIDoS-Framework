#!/usr/bin/python2.7
# coding: utf-8

import sys, urllib2, time
from time import sleep

#############################
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
################################

def clickjack():
    print ""+C+"\n                     _________ .__  .__        __        ____.              __    "
    time.sleep(0.1)
    print ""+C+"                     \_   ___ \|  | |__| ____ |  | __   |    |____    ____ |  | __"
    time.sleep(0.1)
    print ""+C+"                     /    \  \/|  | |  |/ ___\|  |/ /   |    \__  \  / ___\|  |/ /"
    time.sleep(0.1)
    print ""+C+"                     \     \___|  |_|  \  \___|    </\__|    |/ __ \/  \___|    < "
    time.sleep(0.1)
    print ""+C+"                      \______  /____/__|\___  >__|_ \________(____  /\___  >__|_ \ "
    time.sleep(0.1)
    print ""+C+"                             \/             \/     \/             \/     \/     \/"
    print ""
    print ""+C+"                      +======================================================+"
    time.sleep(0.1)
    print(''+GR+'                        Enter target website address for the ClickJack Test ')
    time.sleep(0.1)
    print(''+C+'                      +======================================================+')
    h = raw_input(''+ T + color.BOLD + '                                 Website :> ' + color.END)
    time.sleep(0.4)
    print (""+R+"                               Target set :> %s" % (site))
    time.sleep(0.1)
    print ''+GR+'                     +======================================================+'
    try:
	domains = [h]
        for dom in domains:
	    print ''+C+'                 [*] Configuring the web address...'
	    time.sleep(0.8)
            if "http" not in dom: 
	        dom = "http://" + dom
	    print ''+GR+'                 [*] Checking the Web Address...'
	    time.sleep(0.4)	    
	    req = urllib2.urlopen(dom)
	    print ''+B+'                 [*] Requesting related info...'
	    time.sleep(0.7)
            headers = req.info()
	    print ''+P+'                 [*] Checking for ClickJackability...'
	    time.sleep(1)
            if not "X-Frame-Options" in headers:
	        print ''+G+'\n                 [*] Checking for missing X-Frame-Options...'
		time.sleep(0.5)
		print ''+O+'                 [!] The Website is clickjackable!!!'
		time.sleep(0.2)
		print ''+GR+'                 [*] Generating report...'
		time.sleep(0.4)
	        print ''+C+'                 [*] POC as below... You can save it as a html file ;)'
		time.sleep(0.2)
	        print ''
	        code1 = """
	     	    <html>
		       <head><title>Clickjack test page</title></head>
   		          <body>
		             <p>Website is vulnerable to clickjacking!</p>
		             <iframe src="{}" width="500" height="500"></iframe>
		          </body>
		    </html>
		"""
	        code = """
		    \033[1;32m<html>
		       \033[1;32m<head><title>\033[1;33mClickjack test page\033[1;32m</title></head>
		       \033[1;32m<body>
		         \033[1;32m<p>\033[1;33mWebsite is vulnerable to clickjacking!\033[1;32m</p>
		         \033[1;32m<iframe src="{}" width="500" height="500"></iframe>
		       \033[1;32m</body>
		    \033[1;32m</html>
		"""
	        print code
		time.sleep(0.3)
	        w = raw_input(""+GR+"                 [*] Do you want to save this as a output file? (y/n) :> ")
	        if w == "y":
		    print''+B+'                 [!] Generating POC in html format...'
		    time.sleep(1.5)
		    html_file = open("webpoc.html","w")
		    html_file.write(code1)
		    html_file.close()
		    print ''
		    print''+G+'                 [!] POC successfully saved!'
		    print ''
	        else:
		    print ''+B+'                 [*] Okay :)'
	    else:
	        print ''+R+'                 [!] Oh no! This Website is Immune! Its not Clickjackable dude :('
    except:
	    print ''+R+'                 [!] Fuck, something went wrong!'
