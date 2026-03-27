import urllib.request
import re
url = 'https://www.superdelivery.com/p/r/pd_p/13526173/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
og = re.search(r'property="og:image"\s+content="([^"]+)"', html)
if og:
    print('OG:', og.group(1))
else:
    imgs = re.findall(r'<img[^>]+src="([^"]*product_image[^"]+)"', html)
    print('IMGS:', list(set(imgs)))
