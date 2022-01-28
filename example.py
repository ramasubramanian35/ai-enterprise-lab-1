# This program check is the DC connect is down
#  
import requests

r = requests.get('https://sts.dc-uoit.ca/adfs/ls')

if r.status_code == 200:
    print('site is online')
else:
    print('The site is offline! please check with the IT team')