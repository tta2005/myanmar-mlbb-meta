import requests
from bs4 import BeautifulSoup

def get_hero_data(hero_id):
    # သင်ပေးတဲ့ URL ပုံစံအတိုင်း Dynamic ဆွဲယူမယ်
    url = f"https://www.mobilelegends.com/hero/detail?heroid={hero_id}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Site ထဲက Hero နာမည်နဲ့ ပုံကို ရှာဖွေခြင်း
        # (မှတ်ချက် - MLBB Site structure အပြောင်းအလဲပေါ်မူတည်၍ class name များ ပြင်ရန်လိုနိုင်သည်)
        name = soup.find('h2').text.strip() if soup.find('h2') else "Unknown Hero"
        img_url = soup.find('img', {'class': 'hero-img'})['src'] if soup.find('img') else ""
        
        return {"name": name, "img": img_url, "wr": "Fetch from Rank", "tier": "S"}
    except:
        return None

def update_web():
    # Hero ID အလိုက် Data တွေကို API လိုမျိုး Loop ပတ်ပြီး ဆွဲထုတ်မယ်
    hero_ids = [33, 1, 50] # 33 က Akai, တခြား ID တွေ ထည့်နိုင်ပါတယ်
    hero_list = []
    
    for hid in hero_ids:
        data = get_hero_data(hid)
        if data:
            hero_list.append(data)

    cards_html = ""
    for h in hero_list:
        cards_html += f'''
        <div class="hero-card p-6 rounded-3xl bg-slate-800 border border-slate-700">
            <img src="{h['img']}" class="w-24 h-24 mx-auto rounded-full border-2 border-yellow-500 mb-4">
            <h3 class="text-2xl font-bold text-center text-white">{h['name']}</h3>
            <p class="text-center text-yellow-500">Live API Data</p>
        </div>
        '''

    # index.html ကို Update လုပ်ခြင်း
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    start, end = "", ""
    parts = content.split(start)
    res = parts[1].split(end)
    final = parts[0] + start + cards_html + end + res[1]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(final)

if __name__ == "__main__":
    update_web()
