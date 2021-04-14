import requests
import urllib3
from datetime import date
import os
import urllib
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'
os.system("clear")
os.system("figlet URL FORCER")
print(f"    {B}v {G}1.0\n{R}By Helior")
print("Exemplo: https://docs.microsoft.com/")
alvo = input(f'{R}Digite A Url Do Seu Alvo: {B}')
gg = requests.get(alvo, verify=False)
if gg.status_code != 404:
    if gg.status_code == 403:
        letra = R
    elif gg.status_code == 200:
        letra = G
    else:
        letra = C
    print(f'{B}ALVO {R}=> {G}{alvo} {B}Status Code: {letra}{gg.status_code}{C}')
else:
    print(f'{R} {B}[AVISO] URL PASSADA JA POSSUI UM STATUS CODE DE {R} => {R}{gg.status_code}{C}')
brutes = open("pastas.txt")
data_agora = date.today()
for linha in brutes:

    try:
      #time.sleep(10)
      url = urllib.request.urlopen(f'{alvo}{linha}')
      status_codefoda = url.getcode()
      if status_codefoda != 404:
         if status_codefoda == 403:
            letra = R
         elif status_codefoda == 200:
            letra = G
         else:
           letra = C
         print(f'{B}[{G}{data_agora}]{B} Possivel endereco encontrado! {R}=> {G}{alvo}{linha} {B}Status Code: {letra}{status_codefoda}{C}')
    except:
      print()
