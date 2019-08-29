import os 

def download():
	link = 'wget http://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-US1.zip'
	print (' \033[94m\n[+]\033[94m ---> Downloading VPN-FREE \n\n')
	os.system(link)

def unzip():
	download()
	# Installing UnZip
	os.system('sudo apt-get update')
	os.system('sudo apt-get install zip')
	os.system('sudo apt-get install unzip')
	os.system('unzip -v')

	crack = 'unzip VPNBook.com-OpenVPN-US1.zip'
	print ('\n \033[94m\n[+]\033[94m ---> Unzip File\n\n')
	out = os.path.isfile('VPNBook.com-OpenVPN-US1.zip')
	if out:
		os.system(crack)
	else:
		print ('Error: \033[93m\n[+]\033[93m ---> No Unzip File')

def connect():
	#sudo apt-get install libpkcs11-helper1
	os.system('sudo apt-get update')
	os.system('sudo apt-get install libpkcs11-helper1')

	#Installation of openvpn
	os.system('sudo apt-get update')
	os.system('sudo apt-get install openvpn')
	os.system('openvpn --config vpnbook-us1-tcp80.ovpn')
