import urllib.request
import re
import os

urls = {
    "noren_hokusai_shiranami": "https://www.superdelivery.com/p/r/pd_p/1304817/",
    "noren_hokusai_redfuji": "https://www.superdelivery.com/p/r/pd_p/7523420/",
    "noren_accordion_redfuji": "https://www.superdelivery.com/p/r/pd_p/12258837/",
    "noren_accordion_shiranami": "https://www.superdelivery.com/p/r/pd_p/12258836/",
    "noren_popular_indigo": "https://www.superdelivery.com/p/r/pd_p/5411647/",
    "noren_popular_sakura_fuji": "https://www.superdelivery.com/p/r/pd_p/12193453/",
    "noren_popular_sakura_cat": "https://www.superdelivery.com/p/r/pd_p/9968621/"
}

os.makedirs('images', exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Referer': 'https://www.superdelivery.com/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

for name, url in urls.items():
    print(f"Fetching {name} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
            # Find og:image
            match = re.search(r'<meta\s+property="og:image"\s+content="([^"]+)"', html)
            if match:
                img_url = match.group(1)
                print(f"Found image URL: {img_url}")
                
                # Download image
                img_req = urllib.request.Request(img_url, headers=headers)
                with urllib.request.urlopen(img_req) as img_resp:
                    img_data = img_resp.read()
                    with open(f"images/{name}.jpg", "wb") as f:
                        f.write(img_data)
                print(f"Saved images/{name}.jpg\n")
            else:
                print(f"Could not find og:image for {name}\n")
    except Exception as e:
        print(f"Error processing {name}: {e}\n")

print("Done.")
