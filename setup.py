# coding: utf-8
#!/usr/bin/env python
import os, sys, time
from time import sleep

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

os.system("clear")

time.sleep(1)
print ""+B+color.BOLD+"    [!] Gathering info..."+color.END
time.sleep(2)
print ""+GR+color.BOLD+"    [*] Checking your resources..."+color.END
time.sleep(3)
if os.geteuid() == 0:
    print ""+G+color.BOLD+"    [!] No problems found."+color.END
    print ""+G+color.BOLD+"    [!] CheckUP complete. Launching the installer..."+color.END
else:
    sys.exit(color.PURPLE+"    [!] Run this script as ROOT !!!\033[0m")
    sys.exit()
time.sleep(4)
os.system("clear")
print
header = color.BOLD + """
           \033[37m---------------------------------
                  < \033[1;36mTIDoS Installer!!\033[1;36m >
           ---------------------------------"""
print header
print color.CYAN+color.BOLD+"                        _nnnn_"
time.sleep(0.2)
print color.CYAN+color.BOLD+"                       dGGGGMMb"
time.sleep(0.2)
print color.CYAN+color.BOLD+"                      @p~qp~~qMb     "+color.YELLOW+color.BOLD+"TIDoS Rules!!!" 
time.sleep(0.2)
print color.CYAN+color.BOLD+"                      M(\033[37m@\033[96m)(\033[37m@\033[96m) M|   "+GR+"_;"
time.sleep(0.2)
print color.CYAN+color.BOLD+"                      @\033[33m,----.\033[96mJM| "+GR+"-'"
time.sleep(0.2)
print color.CYAN+color.BOLD+"                     JS^\033[33m\__/  \033[96mqKL"
time.sleep(0.2)
print color.CYAN+color.BOLD+"                    dZP        qKRb"
time.sleep(0.2)
print color.CYAN+color.BOLD+"                   dZP          qKKb"
time.sleep(0.2)
print color.CYAN+color.BOLD+"                  fZP            SMMb"
time.sleep(0.2)
print color.CYAN+color.BOLD+"                  HZM            MMMM"
time.sleep(0.2)
print color.CYAN+color.BOLD+"                  FqM            MMMM"
time.sleep(0.2)
print color.CYAN+color.BOLD+"                 \033[33m_| '.        |\033[96mdS'qML'"
time.sleep(0.2)
print color.CYAN+color.BOLD+"                \033[33m|    `.       | `' \_\033[96mZq'"
time.sleep(0.2)
print color.CYAN+color.BOLD+"               \033[33m_)      \.___.,|     .'     "+R+color.BOLD+"[■] "+color.YELLOW+color.BOLD+"Unleash the POWER of" 
time.sleep(0.2)
print color.CYAN+color.BOLD+"               \033[33m\________)\033[96mMMMMM\033[33m|   .'               "+GR+color.BOLD+"   CYBER RECONNAISSANCE "+R+color.BOLD+"(⊙_⊙)"+color.END
time.sleep(0.2)
print color.BOLD+"                              \033[33m`--'         "+color.END
time.sleep(0.2)
print''
print(""+color.YELLOW+color.BOLD+"           ╔════════════════════════════════╗")
print(""+color.YELLOW+color.BOLD+"           ║  \033[37mthe-Infected-Drake \033[91maka \033[92m@_tID  \033[93m║")
print(""+color.YELLOW+color.BOLD+"           ╚═══════════════════════════════════╗"+color.END)
print(""+color.YELLOW+color.BOLD+"       ╔════════════════════════════════════╝  ║")
print(""+color.YELLOW+color.BOLD+"       ║      \033[37mOperating Systems Available: \033[93m════╝"+color.END)
print(""+color.YELLOW+color.BOLD+"       ║    "+GR+"+======================================+"+color.END)
print(""+color.YELLOW+color.BOLD+"       ╚═══》"+color.DARKCYAN+color.BOLD+"  (1) Kali Linux / Ubuntu / Raspbian  "+GR+"|"+color.END)
time.sleep(0.2)
print(""+GR+color.BOLD+"            +======================================+\n"+color.END)

option = raw_input(color.PURPLE+color.BOLD+"           [>] Select Operating System :> " + color.END)

if option == "1":
    time.sleep(0.2)
    print color.BOLD+color.YELLOW+"  [*] Loading..."+color.END
    os.system('apt-get install python-pip')
    try:
        import pip
    except:
        os.system('easy_install pip')
    os.system('pip install google')
    os.system('pip install requests')
    print color.BOLD+color.YELLOW+"  [*] Installing..."+color.END
    install = os.system("apt-get update && apt-get install -y build-essential git")
    install2 = os.system("cp -R tidos/ /opt/ && cp tidos.py /opt/tidos && cp runon.sh /opt/tidos && cp runon.sh /usr/bin/tidos && chmod +x /usr/bin/tidos")
    os.system('apt-get install nmap')
    os.system('apt-get install libncurses5')
    pip.main(["install", "scapy", "requests", "google"])
    time.sleep(0.3)
    print color.BOLD+color.GREEN+"  [!] SetUP Successfull ! Execute 'tidos' now to launch the tool [!]"+color.END
    time.sleep(0.5)
    print ''+M+"  [+] Also note that the next time, you want to run this tool, just simply execute 'tidos' in terminal."
    sys.exit()
else:
    print ""+R"  [!] Whoops! Operating system not Compatible..."
    sys.exit()
