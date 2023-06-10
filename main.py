from pypresence import Presence
import time
from colorama import Fore
from colorama import init
import os, ctypes
import fade

cmd = 'mode 250,250'
os.system(cmd)

ctypes.windll.kernel32.SetConsoleTitleW("RPC MAKER | by Pitusd")  


rpcbanner = fade.fire(f'''  
            
                                                
                                                                            ██████╗ ██████╗  ██████╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
                                                                            ██╔══██╗██╔══██╗██╔════╝    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
                                                                            ██████╔╝██████╔╝██║         ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
                                                                            ██╔══██╗██╔═══╝ ██║         ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
                                                                            ██║  ██║██║     ╚██████╗    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
                                                                            ╚═╝  ╚═╝╚═╝      ╚═════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                            
                                                                                        
      ''')                                                  

print(rpcbanner)

input(Fore.LIGHTCYAN_EX + 'Press enter to start the activity') 

print(Fore.LIGHTGREEN_EX + 'Activiy Started Enjoy')

clientID = ''  #application id, https://discord.com/developers/applications

rpc = Presence(clientID)
rpc.connect()


rpc.update(state= 'by Pitusd',
           details= '',
           large_image= '',
           large_text= '',
           small_image= '',
           small_text= '',
           buttons= [{'label': 'Discord Server', 'url': ''},
           {'label': '', 'url': ''}])
           
while True:
    time.sleep(15)
    
#SO IMPORTANT! the script must remain open if you close the cmd the activity will stop
# https://github.com/Pitusd-V2    
