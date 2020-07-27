#download files directly with requests module

import requests

url = 'https://www.raspberrypi.org/magpi-issues/MagPi05.pdf'
r = requests.get(url,allow_redirects=True)
open('MagPi05.pdf','wb').write(r.content)
print (r.headers.get('content-type'))
