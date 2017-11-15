# coding: utf-8
#!/usr/bin/env python

import httplib
import socket
import sys
import time
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

def adminpanel():
     try:
	  print ''
	  print ""+B+"                    _____ ___ _______   ____     _      ____   __   _____ _______ "
	  time.sleep(0.1)
	  print ""+B+"                   |  ___|_  |.  __  | |__  |   / \    |__  |  \ \ / |_  |.  __  |"
	  time.sleep(0.1)
	  print ""+B+"                   | |_    | || |  | |    | |  / _ \      | |   \ V /  | || |  | |"
	  time.sleep(0.1)
	  print ""+B+"                   |  _|   | || | _| |____| | / ___ \ ____| | ___\  \  | || | _| |"
	  time.sleep(0.1)
	  print ""+B+"                   |_|     | ||_||___/____/\_/_/   \_/____/\_|______|  | ||_||___|"
	  time.sleep(0.1)
	  print ""+B+"                           |_|                                         |_|        \n"
	  global var1
	  global var2
	  var1=0
	  var2=0
	
	  quick = ['admin/','administrator/','admin/login.html','admin/index.html','wp-login.php','admin/admin-login.php','admin-	login.php','adm.php','login.html','administrator.html','login.html','admin.html',
'cp.html','adminpanel.php','admin_login.php']

	  regular = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','_admin/','usuarios/',
'usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html', 'adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']  

	  thorough = [ 'admin/slider.php','admin/add-slider.php','admin/add_gallery_image.php','admin/welcome.php','admin/configration.php','admin/dashbord.php','manage_admin.php','admin/form.php','admin/my_account.php','admin/specializations.php',
'admin/initialadmin.php','admin/pages/home_admin.php','admin/home.php','/admin/save.php','admin/enter.php','admin/userpage.php','admin/banners_report.php','admin/login-home.php','admin/category.php','admin/dashboard/index.php','admin/add_banner.php',
'admin/add_testimonials.php','admin/userpage.php','admin_main.html','admin/addblog.php','admin/products.php','admin/admin_management.php','admin/add.php','admin/add-room.php','admin/main_page.php','admin/adminview.php','admin/welcomepage.php','admin/index-digital.php',
'admin/overview.php','admin_home.php','admin/admin_users.php','/admin/upload.php','admin/index_ref.php','admin/checklogin.php','admin/member_home.php','admin/banner.php','admin/manageImages.php','admin/login_success.php','admin/leads.php',
'admin/uhome.html','admin/AdminDashboard.php','admin/cpanel.php','admin/manage_team.php','admin/voucher.php','admin/ManageAdmin.php','admin/dashboard.php','admin/account.php','admin/change_gallery.php','admin/list_gallery.php','admin/viewblog.php','admin/main.php',
'admin/AdminHome.php','admin/dash.php','admin/gallery.php','admin/product.php','admin/loginsuccess.php','admin/gallery.php','admin/headline.php','admin/page_management.php','admin/index.php','admin/event.php','admin/admin-home.php','admin/myaccount.php','admin/admin_index.php',
'admin/viewmembers.php','admin/default.php','admin/CPhome.php','admin/control_pages/admin_home.php','admin/adminarea.php' ]

	  php = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']

	  asp = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp',
'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','pages/admin/admin-login.html','admin/admin-login.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html']

	  cfm = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm']

	  js = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js']

	  cgi = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.cgi','admin/index.cgi','admin/login.cgi','admin/admin.cgi','admin/account.cgi',
'admin_area/admin.cgi','admin_area/login.cgi','siteadmin/login.cgi','siteadmin/index.cgi','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cgi','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi']

	  brf = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.brf','admin/index.brf','admin/login.brf','admin/admin.brf','admin/account.brf',
'admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf']    
	  try:
	        print ""+C+"                      +======================================================+"
		time.sleep(0.1)
		print(''+GR+'                         Enter target web address for the Admin Panel Hunt ')
		time.sleep(0.1)
		print(''+C+'                      +======================================================+')
		site = raw_input(''+ T + color.BOLD + '                                 Website :> ' + color.END)
		time.sleep(0.4)
		print (""+R+"                               Target set :> %s" % (site))
	  	time.sleep(0.1)
		print ''+GR+'                     +======================================================+'
	        site = site.replace("http://","")
	        print (""+C+"\n                           [*] Checking availability -> " + site)
		time.sleep(1)
	        conn = httplib.HTTPConnection(site)
	        conn.connect()
	        print (""+G+"                           [!] Server detected online.")
	  except (httplib.HTTPResponse, socket.error) as Exit:
	        raw_input(""+R+"                        [!] Error occured, Server is Offline or Invalid URL")
		sys.exit()
	  def adpa():
	    time.sleep(0.4)
	    print ''+B+'                           [*] Preparing modules...'
	    time.sleep(0.6)
	    print ''+GR+'                           [*] Preparing action lists...'
	    time.sleep(1)                         
	    global var1, var2
	    print ''+O+'\n                            Choose the type of scan you want to perform :-'
	    time.sleep(0.3)
	    print ''+GR+'                      +=====================================================+\n'
	    print ""+C+"                          [1] \033[1;94mSpecific Scan (more chances of detection)"
	    print ""+G+"                           -- This type of scan requires knowledge of the"
	    print ""+G+"                               lang. in which the website is written in."
	    time.sleep(0.3)
	    print ""+C+"                          [2] \033[1;94mRandom Scan (less chances)"
	    print ""+G+"                           -- This scan is for websites which you have zero"
	    print ""+G+"                                             knowledge of.\n"
	    print ''+GR+'                      +=====================================================+\n'
	    time.sleep(0.2)
	    co = raw_input(""+O+"                         Enter the number corresponding to the scan :> ")
	    if co == '2':
		    print ''
		    print ''+R+ '                         Choose the type of scan you want to perform :-'
		    time.sleep(0.2)
		    print ''+GR+'                      +=====================================================+\n'
		    print ""+C+"                          [1] \033[94mA Quick Shuffle Hunt of the Website"
		    time.sleep(0.05)
		    print ""+C+"                          [2] \033[94mA Regular Scan through the website"
		    time.sleep(0.05)
		    print ""+C+"                          [3] \033[94mA Thorough Hunt through the website\n"
		    time.sleep(0.05)
		    print ''+GR+'                      +=====================================================+' 
		    time.sleep(0.2)
		    code = raw_input(""+O+"\n                         Enter the number corresponding to the scan :> ")
		    time.sleep(0.2)
		    if code =='1':
			print ""+O+"                        [¬] Scan Type Selected: "+GR+"Quick Shuffle"
			time.sleep(0.8)
		        print(""+B+"\n                        [+] Scanning initiated -> "+GR+"" +site+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in quick:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = site + admin
		            print (""+C+"                        [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(site)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n                        [+] " + host, ""+G+"Admin page found!\n")
		                raw_input(""+G+"                            [-] Press 'Enter' to " +O+ "continue "+G+"scanning.\n")
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n                    [!] " + host, "Possible admin page (302 - Redirect)\n")
		            else:
		                print "%s %s %s" % (""+G+"                        [!] "+host, ""+O+" Interesting response: ", response.status)
		            connection.close()
		        print(""+GR+"\n                            [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+"                            [!] Admin page path found -> %s" % (var1))
			time.sleep(0.5)
		        print(""+O+"                            [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+"       [!] The scan completed, press 'Enter' to continue or use 'back' to get back to the TID Shell :> ")
			if s == "":
			    adpa()
			elif s == 'back':
			    print ''

		    elif code =='2':
			print ""+O+"                        [¬] Scan Type Selected: "+GR+"Regular"
			time.sleep(0.8)
		        print(""+B+"\n                        [+] Scanning initiated -> "+GR+"" +site+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in regular:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = site + admin
		            print (""+C+"                        [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(site)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n                        [+] " + host, ""+G+"Admin page found!\n")
		                raw_input(""+G+"                            [-] Press 'Enter' to " +O+ "continue "+G+"scanning.\n")
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n                    [!] " + host, "Possible admin page (302 - Redirect)\n")
		            else:
		                print "%s %s %s" % (""+G+"                        [!] "+host, ""+O+" Interesting response: ", response.status)
		            connection.close()
		        print(""+GR+"\n                            [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+"                            [!] Admin page path found -> %s" % (var1))
			time.sleep(0.5)
		        print(""+O+"                            [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+"       [!] The scan completed, press 'Enter' to continue or use 'back' to get back to the TID Shell :> ")
			if s == "":
			    adpa()
			elif s == 'back':
			    print ''

		    elif code =='3':
			print ""+O+"                        [¬] Scan Type Selected: "+GR+"Thorough Scan"
			time.sleep(0.8)
		        print(""+B+"\n                        [+] Scanning initiated -> "+GR+"" +site+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in thorough:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = site + admin
		            print (""+C+"                        [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(site)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n                        [+] " + host, ""+G+"Admin page found!\n")
		                raw_input(""+G+"                            [-] Press 'Enter' to " +O+ "continue "+G+"scanning.\n")
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n                    [!] " + host, "Possible admin page (302 - Redirect)\n")
		            else:
		                print "%s %s %s" % (""+G+"                        [!] "+host, ""+O+" Interesting response: ", response.status)
		            connection.close()
		        print(""+GR+"\n                            [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+"                            [!] Admin page path found -> %s" % (var1))
			time.sleep(0.5)
		        print(""+O+"                            [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+"       [!] The scan completed, press 'Enter' to continue or use 'back' to get back to the TID Shell :> ")
			if s == "":
			    adpa()
			elif s == 'back':
			    print ''

	    elif co == '1':
		    print ''
		    print ''+R+ '                       Choose the type of website you want scan to perform :-'
		    print ''+GR+'                      +=====================================================+\n'
		    print ""+C+"                                [1] \033[94mPHP Website"
		    print ""+C+"                          	[2] \033[94mASP Website"
		    print ""+C+"                          	[3] \033[94mCFM Website"
		    print ""+C+"                          	[4] \033[94mJS Website"
		    print ""+C+"                          	[5] \033[94mCGI Website"
		    print ""+C+"                          	[6] \033[94mBRF Website\n"
		    print ''+GR+'                      +=====================================================+' 
		    code = raw_input(""+O+"\n                         Enter the number corresponding to the scan :> ")
		    if code =='1':
			print ""+O+"                        [¬] Web Type Selected: "+GR+"PHP"
			time.sleep(0.8)
		        print(""+B+"\n                        [+] Scanning initiated -> "+GR+"" +site+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in php:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = site + admin
		            print (""+C+"                        [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(site)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n                        [+] " + host, ""+G+"Admin page found!\n")
		                raw_input(""+G+"                            [-] Press 'Enter' to " +O+ "continue "+G+"scanning.\n")
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n                    [!] " + host, "Possible admin page (302 - Redirect)\n")
		            else:
		                print "%s %s %s" % (""+G+"                        [!] "+host, ""+O+" Interesting response: ", response.status)
		            connection.close()
		        print(""+GR+"\n                            [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+"                            [!] Admin page path found -> %s" % (var1))
			time.sleep(0.5)
		        print(""+O+"                            [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+"       [!] The scan completed, press 'Enter' to continue or use 'back' to get back to the TID Shell :> ")
			if s == "":
			    adpa()
			elif s == 'back':
			    print ''

		    elif code =='2':
			print ""+O+"                        [¬] Web Type Selected: "+GR+"ASP"
			time.sleep(0.8)
		        print(""+B+"\n                        [+] Scanning initiated -> "+GR+"" +site+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in asp:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = site + admin
		            print (""+C+"                        [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(site)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n                        [+] " + host, ""+G+"Admin page found!\n")
		                raw_input(""+G+"                            [-] Press 'Enter' to " +O+ "continue "+G+"scanning.\n")
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n                    [!] " + host, "Possible admin page (302 - Redirect)\n")
		            else:
		                print "%s %s %s" % (""+G+"                        [!] "+host, ""+O+" Interesting response: ", response.status)
		            connection.close()
		        print(""+GR+"\n                            [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+"                            [!] Admin page path found -> %s" % (var1))
			time.sleep(0.5)
		        print(""+O+"                            [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+"       [!] The scan completed, press 'Enter' to continue or use 'back' to get back to the TID Shell :> ")
			if s == "":
			    adpa()
			elif s == 'back':
			    print ''

		    elif code =='3':
			print ""+O+"                        [¬] Web Type Selected: "+GR+"CFM"
			time.sleep(0.8)
		        print(""+B+"\n                        [+] Scanning initiated -> "+GR+"" +site+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in cfm:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = site + admin
		            print (""+C+"                        [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(site)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n                        [+] " + host, ""+G+"Admin page found!\n")
		                raw_input(""+G+"                            [-] Press 'Enter' to " +O+ "continue "+G+"scanning.\n")
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n                    [!] " + host, "Possible admin page (302 - Redirect)\n")
		            else:
		                print "%s %s %s" % (""+G+"                        [!] "+host, ""+O+" Interesting response: ", response.status)
		            connection.close()
		        print(""+GR+"\n                            [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+"                            [!] Admin page path found -> %s" % (var1))
			time.sleep(0.5)
		        print(""+O+"                            [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+"       [!] The scan completed, press 'Enter' to continue or use 'back' to get back to the TID Shell :> ")
			if s == "":
			    adpa()
			elif s == 'back':
			    print ''

		    elif code =='4':
			print ""+O+"                        [¬] Web Type Selected: "+GR+"JS"
			time.sleep(0.8)
		        print(""+B+"\n                        [+] Scanning initiated -> "+GR+"" +site+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in js:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = site + admin
		            print (""+C+"                        [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(site)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n                        [+] " + host, ""+G+"Admin page found!\n")
		                raw_input(""+G+"                            [-] Press 'Enter' to " +O+ "continue \n")
				connection.close()
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n                    [!] " + host, "Possible admin page (302 - Redirect)\n")
		            else:
		                print "%s %s %s" % (""+G+"                        [!] "+host, ""+O+" Interesting response: ", response.status)
		            connection.close()
		        print(""+GR+"\n                            [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+"                            [!] Admin page path found -> %s" % (var1))
			time.sleep(0.5)
		        print(""+O+"                            [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+"       [!] The scan completed, press 'Enter' to continue or use 'back' to get back to the TID Shell :> ")
			if s == "":
			    adpa()
			elif s == 'back':
			    print ''

		    elif code =='5':
			print ""+O+"                        [¬] Web Type Selected: "+GR+"CGI"
			time.sleep(0.8)
		        print(""+B+"\n                        [+] Scanning initiated -> "+GR+"" +site+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in cgi:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = site + admin
		            print (""+C+"                        [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(site)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n                        [+] " + host, ""+G+"Admin page found!\n")
		                raw_input(""+G+"                            [-] Press 'Enter' to " +O+ "continue\n")
				connection.close()
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n                    [!] " + host, "Possible admin page (302 - Redirect)\n")
		            else:
		                print "%s %s %s" % (""+G+"                        [!] "+host, ""+O+" Interesting response: ", response.status)
		            connection.close()
		        print(""+GR+"\n                            [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+"                            [!] Admin page path found -> %s" % (var1))
			time.sleep(0.5)
		        print(""+O+"                            [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+"       [!] The scan completed, press 'Enter' to continue or use 'back' to get back to the TID Shell :> ")
			if s == "":
			    adpa()
			elif s == 'back':
			    print ''

		    elif code =='6':
			print ""+O+"                        [¬] Web Type Selected: "+GR+"BRF"
			time.sleep(0.8)
		        print(""+B+"\n                        [+] Scanning initiated -> "+GR+"" +site+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in brf:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = site + admin
		            print (""+C+"                        [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(site)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n                        [+] " + host, ""+G+"Admin page found!\n")
		                raw_input(""+G+"                            [-] Press 'Enter' to " +O+ "continue "+G+"scanning.\n")
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n                    [!] " + host, "Possible admin page (302 - Redirect)\n")
		            else:
		                print "%s %s %s" % (""+G+"                        [!] "+host, ""+O+" Interesting response: ", response.status)
		            connection.close()
		        print(""+GR+"\n                            [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+"                            [!] Admin page path found -> %s" % (var1))
			time.sleep(0.5)
		        print(""+O+"                            [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+"       [!] The scan completed, press 'Enter' to continue or use 'back' to get back to the TID Shell :> ")
			if s == "":
			    adpa()
			elif s == 'back':
			    print ''

	  adpa()
     except (httplib.HTTPResponse, socket.error):
    	print "\n\t\033[1;31m                               [!] Network error occured! Check internet settings\033[1;m"
     except (KeyboardInterrupt, SystemExit):
    	print "\n\t\033[1;31m                               [!] Scan Aborted By User\033[1;m"
     except:
	print "\n\t\033[1;31m                               [!] Fuck, Something went Wrong... :("

