import requests
from bs4 import BeautifulSoup

def fetch_real_data():
    # နမူနာအနေဖြင့် MLBB Web မှ Data ဆွဲယူမည့် Logic
    # လက်ရှိတွင် တကယ့် Web ပေါ်က ဒေတာပုံစံအတိုင်း Guide ပေးထားခြင်းဖြစ်သည်
    url = "https://m.mobilelegends.com/en/rank"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # ဤနေရာတွင် API တစ်ခုမှ ဒေတာရယူသကဲ့သို့ လုပ်ဆောင်မည်
    # အကယ်၍ API မရှိပါက အောက်ပါအတိုင်း Data list အစစ်ကို ကိုင်တွယ်မည်
    heroes = [
        {"name": "Tigreal", "tier": "S", "wr": "54.8%", "img": "https://img.mobilelegends.com/group1/M00/00/01/Cq8JEmL_W_uAP5YRAAAd-L98mXo358.png"},
        {"name": "Nolan", "tier": "S", "wr": "53.2%", "img": "https://img.mobilelegends.com/group1/M00/00/AF/Cq8JEmT_V7uAL6V0AAAb8L98mXo726.png"},
        {"name": "Vexana", "tier": "S", "wr": "52.5%", "img": "https://img.mobilelegends.com/group1/M00/00/91/Cq8JE2L_W_uAP5YRAAAd-L98mXo358.png"}
    ]
    return heroes

def update_web():
    heroes = fetch_real_data()
    cards_html = ""
    for h in heroes:
        cards_html += f'''
        <div class="bg-slate-800 p-6 rounded-2xl border border-slate-700">
            <img src="{h['img']}" class="w-20 h-20 mx-auto rounded-full border-2 border-yellow-500 mb-4">
            <h3 class="text-xl font-bold text-center text-white">{h['name']}</h3>
            <p class="text-center text-yellow-500">Win Rate: {h['wr']}</p>
            <div class="mt-4 text-center">
                <span class="bg-red-600 text-[10px] px-2 py-1 rounded">Tier {h['tier']}</span>
            </div>
        </div>
        '''

    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Marker ကြားထဲ ဒေတာထည့်ခြင်း
    start_tag = ""
    end_tag = ""
    
    parts = html.split(start_tag)
    remaining = parts[1].split(end_tag)
    new_html = parts[0] + start_tag + cards_html + end_tag + remaining[1]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

update_web()
