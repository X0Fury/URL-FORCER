import requests
import urllib3
from datetime import date
import random
import os
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
print('Exemplo: https://docs.microsoft.com/')
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
    print(f"URL PASSADA JA POSSUI UM STATUS CODE DE {R}404")
brutes = open("pastas.txt")
data_agora = date.today()
for linha in brutes:
    try:
      #time.sleep(10)
      headers = {
             'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            }
      headers = {
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            }
      headers1 = {
                'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            }
      headers2 = {
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            }
      headers3 = {
                'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            }
      headers4 = {
                'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            }
      tdsheaders = [0, 1, 2, 3, 4]
      headersort = random.choice(tdsheaders)
      if headersort == 0:
         headersort = headers
      elif headersort == 1:
           headersort = headers1
      elif headersort == 2:
           headersort = headers2
      elif headersort == 3:
           headersort = headers3
      else:
           headersort = headers4
      url = requests.get(f'{alvo}/{linha}', headers=headersort, verify=False)
      if url.status_code != 404:
         if url.status_code == 403:
            letra = R
         elif url.status_code == 200:
            letra = G
         else:
           letra = C
         print(f'{B}Possivel endereco encontrado! {R}=> {G}{alvo}{linha} {B}Status Code: {letra}{url.status_code}{C}')
    except:
      print(f'{R}URL  INVALIDA!')
