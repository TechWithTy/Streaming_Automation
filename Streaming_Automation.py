import subprocess
import os
# Working As Of 10/17
def start_file(file,directory):
    os.chdir(directory) if directory else print('no directory needed')
    subprocess.Popen(file)



animaze = 'E:\SteamLibrary\steamapps\common\Animaze\Bin\AnimazeDesktop.exe'
vpn = 'C:\Program Files (x86)\Proton Technologies\ProtonVPN\ProtonVPN.exe'
da_vinci = "E:\DaVinci_Resolve\Resolve.exe"
obs_launch = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
obs_directory = "C:\\Program Files\\obs-studio\\bin\\64bit"


start_file(animaze,None)
start_file(vpn,None)
start_file(da_vinci,None)
start_file(obs_launch, obs_directory)

# obs = subprocess.Popen(
#     ["C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"])


