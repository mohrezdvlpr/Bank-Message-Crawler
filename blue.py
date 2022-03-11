import re,os

fo = open("mess.txt",'r',encoding='utf-8').read()
messages = fo.split('----------------------------------------------------')

incom_cash = 0
outcom_cash = 0
data = {}
print('-------------All-------------')
for msg in messages:
    mojodi = ''
    tarikh = ''
    try:
        if "نشست" in msg:
            tarikh = re.findall('14\w\w.10.\w\w',msg)[0]
            mojodi = re.findall('موجودی: (.+) ریال',msg)[0]
            mojodi2 = int(re.findall(' (\w+) ریال',msg.replace(',',''))[0])/10
            incom_cash += mojodi2
            print('\n[+] '+str(mojodi2/1000),mojodi,tarikh)
        if "پرید" in msg:
            tarikh = re.findall('14\w\w.11.\w\w',msg)[0]
            mojodi = re.findall('موجودی: (.+) ریال',msg)[0]
            mojodi2 = int(re.findall(' (\w+) ریال',msg.replace(',',''))[0])/10
            outcom_cash += mojodi2
            try:
                data[tarikh].append(mojodi2)
            except:
                data[tarikh] = []
                data[tarikh].append(mojodi2)
            
            print('\n[-] '+str(mojodi2/1000),mojodi,tarikh)
            
    except:
        pass
print('-------------Daily-------------')
for tarikh in data:
    cash = 0
    for c in data[tarikh]:
        cash+=c
    print('\n[-] '+str(cash/1000),tarikh)
    
print('---------------------------------')
print('Incoming Cash : +'+str(incom_cash))
print('Outcoming Cash : -'+str(outcom_cash))
print('Average Cash : -'+str(outcom_cash/30))