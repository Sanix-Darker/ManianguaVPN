
import sys
import os

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
        os.system("clear")
    if get_platform() == 'windows':
        os.system('cls')
        os.system('color a')
    else:
        pass

def present():
    clear()
    print("-----------------------------------------------------------------------")
    print("|  \/  | __ _ _ __ (_) __ _ _ __   __ _ _   _  __ \ \   / /  _ \| \ | |")
    print("| |\/| |/ _` | '_ \| |/ _` | '_ \ / _` | | | |/ _` \ \ / /| |_) |  \| |")
    print("| |  | | (_| | | | | | (_| | | | | (_| | |_| | (_| |\ V / |  __/| |\  |")
    print("|_|  |_|\__,_|_| |_|_|\__,_|_| |_|\__, |\__,_|\__,_| \_/  |_|   |_| \_|")
    print("                                  |___/")
    print("                               github.com/sanix-darker  By S@n1x-d4rk3r")
