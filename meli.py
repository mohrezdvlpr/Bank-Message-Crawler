import re,os

fo = open("meli.txt",'r',encoding='utf-8').read()
messages = fo.split('----------------------------------------------------')

incom_cash = 0
outcom_cash = 0
data = {}
back = 0
print('-------------All-------------')
for msg in messages:
    mojodi = 0
    mojodi2 = 0
    tarikh = ''
    try:
        if "مانده" in msg:
            tarikh = re.findall('(10\w\w)-\w\w:\w\w',msg)[0]
            mojodi = round(int(re.findall('مانده:(.+)',msg)[0].replace(',',''))/10)
            mojodi2 = mojodi-back
            back = mojodi
            
            try:
                data[tarikh].append(mojodi2)
            except:
                data[tarikh] = []
                data[tarikh].append(mojodi2)
            if mojodi2 < 0 :
                print('\n[-] '+str(mojodi2/1000),mojodi,tarikh)
                outcom_cash += mojodi2

            if mojodi2 > 0 :
                print('\n[+] '+str(mojodi2/1000),mojodi,tarikh)
                incom_cash += mojodi2

            
    except :
        pass
print('-------------Daily-------------')
for tarikh in data:
    cash = 0
    for c in data[tarikh]:
        cash+=c
    print('\n[-] '+str(cash/1000),tarikh)
    
print('---------------------------------')
print('Incoming Cash : +'+str(incom_cash))
print('Outcoming Cash : '+str(outcom_cash))
print('Average Cash : '+str(outcom_cash/30))