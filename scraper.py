import os

def update_html():
    # ဒီမှာ ပြချင်တဲ့ Meta Heroes တွေကို ထည့်ပါ (နမူနာ ၃ ကောင်)
    heroes = [
        {
            "name": "Tigreal", 
            "tier": "S", 
            "wr": "54.2%", 
            "tip": "Flicker + Ulti ကို Timing ကိုက်ကိုက်သုံးပါ။ Tank ဆိုတာထက် Game Changer လို့ မှတ်ယူပါ",
            "counters": "Diggie, Akai, Valir"
        },
        {
            "name": "Nolan", 
            "tier": "S", 
            "wr": "53.8%", 
            "tip": "Energy ထိန်းဖို့ Blue Buff ကို အဓိကထားစားပါ။ Dash Skill တွေကို ပညာသားပါပါသုံးပါ",
            "counters": "Khufra, Minsitthar, Saber"
        },
        {
            "name": "Vexana", 
            "tier": "A", 
            "wr": "52.1%", 
            "tip": "Passive ပေါက်အောင် Skill တွေကို စုပစ်ပါ။ Lord ဆိုင်ရင် Ulti ကို အသေအချာ သုံးပါ",
            "counters": "Helcurt, Natalia, Chou"
        }
    ]
    
    # HTML Card များ တည်ဆောက်ခြင်း
    cards_html = ""
    for h in heroes:
        tier_class = "tier-s" if h['tier'] == "S" else "tier-a"
        cards_html += f'''
            <div class="hero-card p-6 rounded-3xl relative overflow-hidden">
                <div class="flex justify-between items-start mb-4">
                    <div>
                        <h3 class="text-2xl font-bold text-white">{h['name']}</h3>
                        <p class="text-sm text-slate-400 font-mono">Win Rate: {h['wr']}</p>
                    </div>
                    <span class="{tier_class} text-white text-xs font-bold px-3 py-1 rounded-full shadow-lg shadow-red-900/20">Tier {h['tier']}</span>
                </div>
                <div class="bg-slate-900/50 p-4 rounded-xl mb-4 border-l-4 border-yellow-500">
                    <p class="text-yellow-400 text-sm leading-relaxed">"{h['tip']}"</p>
                </div>
                <div class="text-xs text-slate-500">
                    <strong>Counters:</strong> {h['counters']}
                </div>
            </div>
        '''

    # index.html ကို ဖတ်ပြီး Update လုပ်ခြင်း
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # id="hero-list" နေရာကို ရှာပြီး အစားထိုးမယ်
    start_tag = '<div id="hero-list" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">'
    end_tag = '</div>\n    </main>'
    
    try:
        parts = content.split(start_tag)
        remaining = parts[1].split(end_tag)
        new_content = parts[0] + start_tag + cards_html + end_tag + remaining[1]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Success: Meta Hub Updated!")
    except Exception as e:
        print(f"Error: HTML structure matching failed. {e}")

if __name__ == "__main__":
    update_html()
