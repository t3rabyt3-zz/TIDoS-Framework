import urllib2
import time
from time import sleep
###################################
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
   ENDC = '\033[0m'
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
###################################
def webex():
	print ''    
	print ""+color.CYAN+color.BOLD+"                                    Yb        dP 888888 88''Yb 888888 Yb  dP " 
	time.sleep(0.1)
	print ""+color.CYAN+color.BOLD+"                                     Yb  db  dP  88__   88__dP 88__    YbdP  "
	time.sleep(0.1)
	print ""+color.CYAN+color.BOLD+"                                      YbdPYbdP   88''   88''Yb 88''    dPYb  "
	time.sleep(0.1)
	print ""+color.CYAN+color.BOLD+"                                       YP  YP    888888 88oodP 888888 dP  Y8 "
	time.sleep(0.3)
	print ''
	print (""+O+color.BOLD+"                    +========================================================================+")
	print (""+B+color.BOLD+"                         Remember to give the full URL along with 'https','http' or 'www'")
	print (""+O+color.BOLD+"                    +========================================================================+")
	try:
	    site = raw_input(''+T+color.BOLD+'                                      Website :> ' + color.END)
	    urllib2.urlopen(site)
	except urllib2.HTTPError, e:
		x=str(e.code)
		print (''+R+color.BOLD+'                                                Error:' + color.END)
		print (''+R+color.BOLD+'                                                   '+ x + '' + color.END)
	except urllib2.URLError, e:
		y=str(e.args)
		print (''+R+color.BOLD+'                                                Error:' + color.END)
		print (''+R+color.BOLD+'                                                    '+ y + '' + color.END)
	else:
		print (''+G+color.BOLD+'                                           Oh Yeah!!! Page Exists!' + color.END)
		print (''+O+color.BOLD+'                    +========================================================================+' + color.END)
