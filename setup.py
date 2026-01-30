import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pip install requests")
    os.system("pip install multiprosess")
    os.system("pip install pystyle")
    os.system("pip install aiohttp")
elif c == "1":
    os.system("pip3 install requests")
    os.system("pip3 install multiprosess")
    os.system("pip3 install pystyle")
    os.system("pip3 install aiohttp")
print("Done.")
