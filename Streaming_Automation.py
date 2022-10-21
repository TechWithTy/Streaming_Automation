import os
import subprocess
import time

import psutil
import win32api

answer = input("Continue (Y or N) ?")
obs_directory = "C:\\Program Files\\obs-studio\\bin\\64bit"
obs = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
vpn = 'C:\Program Files (x86)\Proton Technologies\ProtonVPN\ProtonVPN.exe'
davinci = "E:\DaVinci_Resolve\Resolve.exe"
animaze = 'E:\SteamLibrary\steamapps\common\Animaze\Bin\AnimazeDesktop.exe'


def start_file(file, directory):
    os.chdir(directory) if directory else print('no directory needed')
    subprocess.Popen(file)


start_file(vpn, None)
start_file(obs, obs_directory)
start_file(animaze, None)


if answer.lower() in ["y", "yes"]:
    start_file(davinci, None)
elif answer.lower() in ["n", "no"]:
    pass

# Verify VPN Started


def verification(program):
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if program.lower() in proc.name().lower():
                print(True)
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            print("VPN Not Started Check script or program")
            pass
    print(False)


time.sleep(5)
verification("ProtonVPN.exe")
