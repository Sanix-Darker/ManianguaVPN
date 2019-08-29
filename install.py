def command():
	os.system('clear')
	os.system('rm -f vpnbook-us1-*')
	os.system('rm -f VPNBook.com-OpenVPN-US1.zip*')

def download():
	link = 'wget http://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-US1.zip'
	print ' \033[94m\n[+]\033[94m ---> Downloading VPN-FREE \n\n' 
	os.system(link)

def unzip():
	download()
	# Installing UnZip
	os.system('sudo apt-get update')
	os.system('sudo apt-get install zip')
	os.system('sudo apt-get install unzip')
	os.system('unzip -v')

	crack = 'unzip VPNBook.com-OpenVPN-US1.zip'
	print '\n \033[94m\n[+]\033[94m ---> Unzip File\n\n'
	out = os.path.isfile('VPNBook.com-OpenVPN-US1.zip')
	if out:
		os.system(crack)
	else:
		print 'Error: \033[93m\n[+]\033[93m ---> No Unzip File'

def getpass():
	print '\n \033[94m\n[+]\033[94m ---> Getting New Password\n\n'
	global user, passwd
	user = 'vpnbook'
	passwd = '5e38t23'
	# try:
	# 	openUrl = urllib2.urlopen('http://www.vpnbook.com/freevpn')
	# except urllib2.URLError:
	# 	exit('Verify that you are connected to the Internet')
	# kader = openUrl.read()
	# joker = '''<li>Password: <strong>(.+?)</strong></li>'''
	# dz = re.findall(joker, kader)

	# if dz:
	# 	passwd = dz[0]
	# passwd = '5e38t23'
	print '''
		\t\033[94m\n[+]\033[91m---> Username: {0}
		\t\033[94m\n[+]\033[93m---> Password: {1}
	\n'''.format(user, passwd)

def connect():
	#sudo apt-get install libpkcs11-helper1
	os.system('sudo apt-get update')
	os.system('sudo apt-get install libpkcs11-helper1')

	#Installation of openvpn
	os.system('sudo apt-get update')
	os.system('sudo apt-get install openvpn')
	os.system('openvpn --config vpnbook-us1-tcp80.ovpn')
