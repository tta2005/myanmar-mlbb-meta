import requests
from bs4 import BeautifulSoup

def get_real_meta():
    # MLBB Ranking Page ကနေ Data ဆွဲမယ်
    url = "https://m.mobilelegends.com/en/rank"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # ဤနေရာတွင် နမူနာအားဖြင့် Data ပုံစံကို တည်ဆောက်ပြထားပါသည်
    # တကယ့် Site ကနေ HTML ဖတ်ပြီး Update လုပ်မည့် Logic
    top_heroes = [
        {"name": "Tigreal", "tier": "S", "wr": "54.8%", "tip": "Flicker + Ulti Timing ကို အထူးဂရုစိုက်ပါ။"},
        {"name": "Nolan", "tier": "S", "wr": "53.2%", "tip": "Blue Buff မပါရင် Nolan က ဘာမှလုပ်လို့မရတာ သတိပြုပါ။"},
        {"name": "Vexana", "tier": "S", "wr": "52.5%", "tip": "Lord ဆိုင်တဲ့အချိန်မှာ Ulti ကို အမှန်ကန်ဆုံးသုံးပါ။"},
        {"name": "Mathilda", "tier": "A", "wr": "51.9%", "tip": "အသင်းသားတွေ လိုက်နိုင်မယ့် အနေအထားမှ ဝင်ပါ။"}
    ]
    return top_heroes

def update_html():
    heroes = get_real_meta()
    
    # HTML Card များ တည်ဆောက်ခြင်း
    cards_html = ""
    for h in heroes:
        cards_html += f'''
        <div class="bg-slate-800 p-5 rounded-xl border border-slate-600 hover:border-yellow-500 transition shadow-lg">
            <div class="flex justify-between items-center mb-3">
                <h3 class="text-xl font-bold">{h['name']}</h3>
                <span class="bg-red-600 text-xs px-2 py-1 rounded text-white font-bold">Tier {h['tier']}</span>
            </div>
            <p class="text-sm text-slate-400 mb-4 font-mono">Win Rate: {h['wr']}</p>
            <p class="text-yellow-400 text-sm leading-relaxed">"{h['tip']}"</p>
        </div>
        '''

    # index.html ကို အလိုအလျောက် Update လုပ်ခြင်း
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # id="hero-list" ရှိတဲ့ နေရာကြားထဲကို Data အသစ် ထိုးထည့်မယ်
    start_tag = '<div id="hero-list" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'
    end_tag = '</div>\n    </div>\n\n    <footer'
    
    split_content = content.split(start_tag)
    remaining_content = split_content[1].split(end_tag)
    
    new_html = split_content[0] + start_tag + cards_html + end_tag + remaining_content[1]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Website updated successfully!")

if __name__ == "__main__":
    update_html()
