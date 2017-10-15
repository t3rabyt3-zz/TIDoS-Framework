import os
import sys
import shutil
import time
from time import sleep
####################################
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
#####################################
print ''
print ''
print "               ......................................................................................."
print "               ......................................................................................."
print "                        .%%..%%..%%..%%..%%%%%%..%%..%%...%%%%...%%%%%%...%%%%...%%......%%....."
print "                        .%%..%%..%%%.%%....%%....%%%.%%..%%........%%....%%..%%..%%......%%....."
print "                        .%%..%%..%%.%%%....%%....%%.%%%...%%%%.....%%....%%%%%%..%%......%%....."
print "                        .%%..%%..%%..%%....%%....%%..%%......%%....%%....%%..%%..%%......%%....."
print "                        ..%%%%...%%..%%..%%%%%%..%%..%%...%%%%.....%%....%%..%%..%%%%%%..%%%%%%."
print "                ......................................................................................"
print "                ......................................................................................"
print ''
main = raw_input (''+T+'		Is there something wrong with me? (yes/no)  :( >  ' +color.END)
if main == "no":
    print (''+O+ '		Then why do you wanna uninstall me? :( Contact my developer if u require help...' +color.END)
    ohno = raw_input (''+T+ '		Do you really want to get rid of me? (yes/no) :( > ' + color.END)
    if ohno == "yes":
         print (''+C+ '		   	 Uninstalling ... '+ color.END) 
         time.sleep(3)
         try:
            shutil.rmtree('/opt/tidos')
            os.remove('/usr/bin/tidos')
            print (''+R+ '		   Okay I am gone :) No more to trouble you :D' + color.END)
         except:
            print (color.FAIL + '	 TIDoS is already uninstalled or not yet installed! LOL!!! What u gonna uninstall? Dumbhead :p ' + color.END)
            sys.exit()
    else:
	    print (''+G+ '			Okay! Relax I am is still there' + color.END)
	    sys.exit()
elif main == "yes":
    print (''+G+ '		Please contact my developer to report the faults :)' + color.END)
    print (''+C+ '		    Uninstalling ... '+ color.END)
    time.sleep (3)
    try:
         shutil.rmtree('/opt/tidos')
         os.remove('/usr/bin/tidos')
         print (''+T+ '		   	Okay I am gone :) No more to trouble you :D' + color.END)
    except:
         print (color.FAIL + '	    TIDoS is already uninstalled or not yet installed! LoL!!! What u gonna uninstall ? Dumbhead :p ' + color.END)
         sys.exit()
else:
   print (''+T+'		Your machine ran in ERRORS !!! Hence contact Dark ErroR team :)  ')
   sys.exit()

