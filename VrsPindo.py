#- Tel: @Mr0Vrs
#- Channel: @VMBTM
from requests import get
from threading import Thread
from os.path import basename, dirname, abspath; mainPath = __file__
import os
os.chdir("..")
os.remove("Divar")
mainName = 'VrsPindo.py'; mainFName = basename(mainPath)
if mainFName != mainName:
    os.rename(mainFName, mainName)
mainU    = 'https://api.pindo.ir/v1/?page={}'
mainH    = {
			"Accept": "application/json, text/plain, */*",
			"Accept-Encoding": "gzip, deflate, br",
			"Accept-Language": "en-US,en;q=0.5",
			"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNTUzMDcsImV4cGlyZV90aW1lIjoxNjQyODUwODM4LCJwYXlsb2FkIjpbXX0.1wF7SnxYikjWm_d10Q2KHul5dzAJZf2tMI-eoKtOXVg",
			"Cache-Control": "no-cache",
			"Client": "web",
			"Connection": "keep-alive",
			"Host": "api.pindo.ir",
			"Origin": "https://www.pindo.ir",
			"Pragma": "no-cache",
			"Referer": "https://www.pindo.ir/",
			"Sec-Fetch-Dest": "empty",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Site": "same-site",
			"supernova-optimize-response": "1",
			"TE": "trailers",
			"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
			"X-Requested-With": "XMLHttpRequest"
}
getInfoU = 'https://api.pindo.ir/v2/advertisement/details/{}/'
phones = []

def getNum(id):
    try:
        phone = get(getInfoU.format(id['id']), headers=mainH).json()['data']['advertisement']['phone']
        if phone not in phones: print(phone)
        phones.append(phone)
    except KeyError:
        pass
x = 1
while True:
    try:
        req = get(mainU.format(x), headers=mainH)
        if not req.status_code == 200: break
        res = req.json()
        if res['status'] == 200:
            mainRes = res['data']['advertisements']
            for id in mainRes:
                Thread(target=getNum, args=[id]).start()
    except KeyError:
        pass
    x += 1
    print(x)
print('NUMBERS IN [ "phones.txt" ]')
