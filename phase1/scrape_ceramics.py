import urllib.request
import re
import os

urls = {
    "ceramics_hoccori_branch": "https://www.superdelivery.com/p/r/pd_p/11029245/",
    "ceramics_hoccori_round": "https://www.superdelivery.com/p/r/pd_p/11029246/",
    "ceramics_hoccori_attached": "https://www.superdelivery.com/p/r/pd_p/11029247/",
    "ceramics_hoccori_incense": "https://www.superdelivery.com/p/r/pd_p/13813571/",
    "ceramics_authentic_fire": "https://www.superdelivery.com/p/r/pd_p/11029291/",
    "ceramics_authentic_flower": "https://www.superdelivery.com/p/r/pd_p/11029287/"
}

os.makedirs('images', exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
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
