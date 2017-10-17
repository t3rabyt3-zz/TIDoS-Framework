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

if not os.geteuid() == 0:
    sys.exit(color.PURPLE+"    [!] Please run this script as root!\033[0m")

header = color.BOLD + """
        ---------------------------------
               < \033[1;36mTIDoS Installer!!\033[1;36m >
        ---------------------------------
                      _nnnn_                      
                     dGGGGMMb     
                    @p~qp~~qMb     TIDoS Rules!!! 
                    M|@||@) M|   _;
                    @,----.JM| -'
                   JS^\__/  qKL
                  dZP        qKRb
                 dZP          qKKb
                fZP            SMMb
                HZM            MMMM
                FqM            MMMM
              __| ".        |\dS"qML
              |    `.       | `' \Zq
             _)      \.___.,|     .'
             \____   )MMMMMM|   .'
                  `-'       `--' 
"""

print header
print ""+GR+color.BOLD+"          Operating Systems Available:\033[1;36m "
print ""+B+color.BOLD+"\n       +======================================+"
print ""+P+color.BOLD+"          (1) Kali Linux / Ubuntu / Raspbian"
print ""+B+color.BOLD+"       +=====================================+\n"

option = raw_input(color.OKBLUE+"           [>] Select Operating System :> \033[0m")

if option == "1":
    print color.BOLD+color.YELLOW+"  [*] Loading..."+color.END
    os.system('apt-get install python-pip')
    os.system('easy_install pip')
    import pip
    os.system('pip install google')
    os.system('pip install requests')
    os.system('pip install requests[security]')
    os.system('pip install pythonwhois')
    print color.BOLD+color.YELLOW+"  [*] Installing..."+color.END
    install = os.system("apt-get update && apt-get install -y build-essential git")
    install2 = os.system("cp -R tidos/ /opt/ && cp tidos.py /opt/tidos && cp runon.sh /opt/tidos && cp runon.sh /usr/bin/tidos && chmod +x /usr/bin/tidos")
    os.system('apt-get install libncurses5')
    pip.main(["install", "scapy", "requests", "google", "pythonwhois"])
    print color.BOLD+M+"  [!] Finished Installing! Run 'tidos' to run program [!]"+color.END
    sys.exit()
else:
    print "Whoops! Something went wrong! Try again KID..."
    sys.exit()
