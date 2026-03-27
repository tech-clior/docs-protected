import urllib.request
import re

urls = [
    '13614595', '13616529', '13618239', '13618239', # Yukatas
    '4814398', '6109167', '4814414', '4814395', # Uchiwas/Tenuguis
    '13372263' # Random Tenugui
]

def get_images(item_id):
    url = f"https://www.superdelivery.com/p/r/pd_p/{item_id}/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        og = re.search(r'property="og:image"\s+content="([^"]+)"', html)
        bg = re.findall(r'data-original="([^"]+)"', html)
        print(f"ID: {item_id}")
        if og:
            print(f"OG: {og.group(1)}")
        if bg:
            print(f"Imgs: {bg[:3]}")
    except Exception as e:
        print(f"Error {item_id}: {e}")

for u in urls:
    get_images(u)
