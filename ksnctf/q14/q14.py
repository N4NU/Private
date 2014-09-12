# this code can only run on Unix

import crypt
import getpass
import pwd

questions = open('q.txt', 'r'). read(). split('\n')
questions.pop()
for q in questions:
    splitedq = q.replace('$', ':').split(':')
    salt = splitedq[3]
    crptpwd = splitedq[4]
    passlist = open('pass.txt', 'r'). read(). split('\n')
    for passwd in passlist:
        mycrptpwd = crypt.crypt(passwd, "$6$"+salt).split("$")
        if mycrptpwd[3] == crptpwd:
            print splitedq[0] + ":" + passwd
            break
