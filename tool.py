 #!/bin/env python


import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet TARAYICI Seition2 | lolcat")
print("yapımcılar : Seition2 | ghooter")
print("""

_________________
|               |
| 1)Port Tarama |
|_______________|
__________________________
|                        |
| 2) Tüm Portları Tarama |
|________________________|
_____________________________
|                           |
| 3)işletim sistemi tarama  |
|___________________________|
__________________
|                 |
| 4)nikto tarama  |
|_________________|
_______________________
|                      |
| 5)Gobuster Taraması  |
|______________________|


""")
islemno = input("işlem numarasını giriniz > ")
if(islemno=="1"):
        hedefip = input("hedef ip yi giriniz > ")
        os.system("nmap " + hedefip)
elif(islemno=="4"):
        hedefip = input("hedef url yi giriniz > ")
        os.system("nikto -h " + hedefip)
elif(islemno=="3"):
        hedefip = input("hedef ip nizi giriniz > ")
        os.system("nmap -O " + hedefip)
elif(islemno=="2"):
    verbose = input("Verbose Modu Açmak için -vv yazınız > ")
    hedefip = input("hedef ip yi giriniz = ")
    os.system("nmap -p- " + hedefip+" "+verbose)

elif(islemno=="5"):
        hedefurl = input("hedef url'i giriniz > ")
        uzantı = input("uzantıları giriniz > ")
        os.system("gobuster dir -u " + hedefurl +" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x"+uzantı+verbose) 

else:
        print("malesef doğru girdiğinizden emin olun ...")
