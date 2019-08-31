from os import system, path
import time, datetime
from utils import *

def main():
	# First let autoremove all precedent vpnbook files
	system("rm -rf vpnbook*")
	system('sudo apt-get update')
	present()
	getRessources()
	# We check if libpkcs11-helper1 is installed
	if check_installed_module("libpkcs11-helper1") == False:
		system('sudo apt-get install libpkcs11-helper1')

	# We check if libpkcs11-helper1 is installed
	if check_installed_module("openvpn") == False:
		system('sudo apt-get install openvpn')

	present()
	system("rm -rf test*")
	print("[+] Starting to establish connection using openvpn...")
	system('openvpn --config vpnbook-us1-tcp80.ovpn')

if __name__ == '__main__':
	main()