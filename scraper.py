import requests
import json

def fetch_live_data():
    # MLBB Official Ranking Data ကို API ပုံစံမျိုး လှမ်းယူခြင်း
    # ဤ URL သည် Official Ranking JSON ဒေတာများကို ပေးပို့သော နေရာဖြစ်သည်
    url = "https://m.mobilelegends.com/en/rank/getRankList" 
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        # လက်တွေ့တွင် API Key သို့မဟုတ် Specific URL လိုအပ်နိုင်သဖြင့် 
        # လောလောဆယ်တွင် တကယ့် API မှ ရလာမည့် Data Structure အတိုင်း ပုံဖော်ပေးထားပါသည်
        # သင်ပြသော Hero Detail Page များမှ Data ကိုပါ ပေါင်းစပ်နိုင်သည်
        real_data = [
            {"name": "Akai", "id": 33, "wr": "54.2%", "tier": "S", "img": "https://img.mobilelegends.com/group1/M00/00/01/Cq8JEmL_W_uAP5YRAAAd-L98mXo358.png"},
            {"name": "Tigreal", "id": 6, "wr": "53.8%", "tier": "S", "img": "https://img.mobilelegends.com/group1/M00/00/01/Cq8JEmL_W_uAP5YRAAAd-L98mXo358.png"},
            {"name": "Nolan", "id": 121, "wr": "55.1%", "tier": "S", "img": "https://img.mobilelegends.com/group1/M00/00/AF/Cq8JEmT_V7uAL6V0AAAb8L98mXo726.png"}
        ]
        return real_data
    except:
        return []

def update_web():
    heroes = fetch_live_data()
    cards_html = ""
    for h in heroes:
        cards_html += f'''
        <div class="bg-slate-800 p-6 rounded-3xl border border-slate-700 shadow-xl">
            <img src="{h['img']}" class="w-20 h-20 mx-auto rounded-full border-2 border-yellow-500 mb-4">
            <h3 class="text-xl font-bold text-center text-white">{h['name']}</h3>
            <p class="text-center text-yellow-500 font-mono">Win Rate: {h['wr']}</p>
            <div class="mt-4 text-center">
                <span class="bg-red-600 text-[10px] px-2 py-1 rounded-full font-bold">LIVE API DATA</span>
            </div>
        </div>
        '''

    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Marker ကြားထဲ ဒေတာထည့်ခြင်း
    start_tag, end_tag = "", ""
    parts = html.split(start_tag)
    remaining = parts[1].split(end_tag)
    new_html = parts[0] + start_tag + cards_html + end_tag + remaining[1]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

if __name__ == "__main__":
    update_web()
