import requests
import subprocess
import urllib

digest = 'b5ff24ed3b12bcd01169c1920365397d7568adf25bfb21dd6dcae82c7de93bd00b732e3f0cc5f17370982bd09ff97d255c65c12b459bd443a68b738179a44a19'
data = '5'
addData = ',10'

for length in range(1, 26):
    cmd = './hash_extender ' + '-s ' + digest + ' -d ' + data + ' -a ' + addData + ' -l ' + str(length) + '-f sha512 --out-data-format=html'
    hash_extender = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    payload = hash_extender.stdout.read()
    splited = payload.splitlines()
    ship = splited[3].replace('New string: ', '')
    signature = splited[2].replace('New signature: ', '')

    cookies = {'ship': ship, 'signature': signature}

    r = requests.get('http://ctfq.sweetduet.info:10080/~q31/kangacha.php', cookies=cookies)

    if 'Yamato' in r.content:
        print 'Salt Length : ' + str(length)
        print r.content.splitlines()[13]
        break
