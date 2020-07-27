import requests

def is_downloadable(url):

    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

print (is_downloadable('https://www.raspberrypi.org/magpi-issues/MagPi06.pdf'))
print (is_downloadable('http://google.com/favicon.ico'))
