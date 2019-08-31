
import sys
from os import system, path
import time, datetime

def get_platform():
    platforms = {
        'linux1' : 'linux',
        'linux2' : 'linux',
        'darwin' : 'mac',
        'win32' : 'windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]

def clear():
    if get_platform() == 'linux' or get_platform() == 'mac':
        system("clear")
    if get_platform() == 'windows':
        system('cls')
        system('color a')
    else:
        pass

def present():
    clear()
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("|  \/  | __ _ _ __ (_) __ _ _ __   __ _ _   _  __ \ \   / /  _ \| \ | |")
    print("| |\/| |/ _` | '_ \| |/ _` | '_ \ / _` | | | |/ _` \ \ / /| |_) |  \| |")
    print("| |  | | (_| | | | | | (_| | | | | (_| | |_| | (_| |\ V / |  __/| |\  |")
    print("|_|  |_|\__,_|_| |_|_|\__,_|_| |_|\__, |\__,_|\__,_| \_/  |_|   |_| \_|")
    print("                                  |___/")
    print("-----------------------------------------------------------------------")
    print("                             github.com/sanix-darker    By S@n1x-d4rk3r")
    print("-----------------------------------------------------------------------")


def check_installed_module(module):
	print("[+] Checking if "+module+" is installed...")
	output1 = './test_'+module+'.txt'
	system("which "+module+" > "+output1)
	with open(output1, "r") as ffr:
		content = ffr.read()

	if "bin" in content:
		print("[+] "+module+" is installed here !")
		return True
	else:
		print("[+] "+module+" is not installed here !")
		return False

def Warranty():
	print("[+] ---IMPORTANT NOTE----------------------------------------------------------------------------")
	print("[+] ---VPNBOOK has IPs who changes every day with a frequency, so if it's been too long the last time you used ManianguaVPN")
	print("[+] ---IMPORTANT NOTE----------------------------------------------------------------------------")

def get_and_install():
	print("[+] Getting VPNBook and Unzipping the VPNBOOK")
	command = 'ls'
	command += ' && wget http://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-US1.zip && rm -rf vpnbook-us1*'
	command += ' && unzip VPNBook.com-OpenVPN-US1.zip'
	command += ' && rm -rf VPNBook.com-OpenVPN-US1.zip'
	system(command)

def check_date_then_install(elt):
	command = 'ls'
	print("[+] Checking the date-age of : "+elt)
	if (time.ctime(path.getctime(elt)).split(" ")[2] != datetime.datetime.now().strftime("%d")):
		print("[+] Getting VPNBook and Unzipping the VPNBOOK")
		command += ' && wget http://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-US1.zip && rm -rf vpnbook-us1*'
	command += ' && unzip VPNBook.com-OpenVPN-US1.zip'
	command += ' && rm -rf VPNBook.com-OpenVPN-US1.zip'
	system(command)

def getRessources():
	# Installing UnZip
	# We check if zip is installed
	if check_installed_module("zip") == False:
		system('sudo apt-get install zip')

	# We check if UnZip is installed
	if check_installed_module("unzip") == False:
		system('sudo apt-get install unzip')

	Warranty()

	if (path.exists("VPNBook.com-OpenVPN-US1.zip") == False and path.exists("./vpnbook-us1-tcp80.ovpn") == False):
		get_and_install()
	else:
		if (path.exists("VPNBook.com-OpenVPN-US1.zip") == True and path.exists("./vpnbook-us1-tcp80.ovpn") == False):
			check_date_then_install("VPNBook.com-OpenVPN-US1.zip")
		elif (path.exists("VPNBook.com-OpenVPN-US1.zip") == False and path.exists("./vpnbook-us1-tcp80.ovpn") == True):
			check_date_then_install("./vpnbook-us1-tcp80.ovpn")
