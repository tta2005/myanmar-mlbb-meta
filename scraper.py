import os

def update_html():
    # Hero ပုံ URL များအပါအဝင် အချက်အလက်များ
    heroes = [
        {
            "name": "Tigreal", 
            "tier": "S", 
            "wr": "54.2%", 
            "img": "https://p16-va.lemon8cdn.com/obj/tos-alisg-v-a3e477-sg/ocA07IByA7mAnfAALMCHjB8AA1IA?x-expires=1716307200&x-signature=2S0%2B0rX8I%2FcH%2BKWqL6o9y%2B7j%2Fjg%3D",
            "tip": "Flicker + Ulti ကို Timing ကိုက်ကိုက်သုံးပါ။ Tank ဆိုတာထက် Game Changer လို့ မှတ်ယူပါ။",
            "counters": "Diggie, Akai, Valir"
        },
        {
            "name": "Nolan", 
            "tier": "S", 
            "wr": "53.8%", 
            "img": "https://img.mobilelegends.com/group1/M00/00/AF/Cq8JEmT_V7uAL6V0AAAb8L98mXo726.png",
            "tip": "Energy ထိန်းဖို့ Blue Buff ကို အဓိကထားစားပါ။ Dash Skill တွေကို ပညာသားပါပါသုံးပါ။",
            "counters": "Khufra, Minsitthar, Saber"
        },
        {
            "name": "Vexana", 
            "tier": "A", 
            "wr": "52.1%", 
            "img": "https://img.mobilelegends.com/group1/M00/00/91/Cq8JE2L_W_uAP5YRAAAd-L98mXo358.png",
            "tip": "Passive ပေါက်အောင် Skill တွေကို စုပစ်ပါ။ Lord ဆိုင်ရင် Ulti ကို အသေအချာ သုံးပါ။",
            "counters": "Helcurt, Natalia, Chou"
        }
    ]
    
    cards_html = ""
    for h in heroes:
        tier_class = "tier-s" if h['tier'] == "S" else "tier-a"
        cards_html += f'''
            <div class="hero-card p-6 rounded-3xl relative overflow-hidden bg-slate-800/40">
                <div class="flex justify-between items-start mb-4">
                    <div class="flex items-center gap-4">
                        <img src="{h['img']}" alt="{h['name']}" class="w-16 h-16 rounded-full border-2 border-yellow-500 object-cover shadow-lg">
                        <div>
                            <h3 class="text-2xl font-bold text-white">{h['name']}</h3>
                            <p class="text-sm text-slate-400 font-mono italic">Win Rate: {h['wr']}</p>
                        </div>
                    </div>
                    <span class="{tier_class} text-white text-xs font-bold px-3 py-1 rounded-full shadow-lg">Tier {h['tier']}</span>
                </div>
                <div class="bg-slate-900/60 p-4 rounded-xl mb-4 border-l-4 border-yellow-600">
                    <p class="text-yellow-400 text-sm leading-relaxed">"{h['tip']}"</p>
                </div>
                <div class="text-[10px] text-slate-500 uppercase tracking-widest font-bold">
                    Counters: <span class="text-slate-400 font-normal">{h['counters']}</span>
                </div>
            </div>
        '''

    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # ပိုပြီး တိကျတဲ့ matching အတွက် comment tag တွေကို သုံးပါမယ်
    start_marker = ""
    end_marker = ""
    
    try:
        parts = content.split(start_marker)
        remaining = parts[1].split(end_marker)
        new_content = parts[0] + start_marker + cards_html + end_marker + remaining[1]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Success: Meta Hub Updated with Images!")
    except:
        print("Error: Marker not found in HTML")

if __name__ == "__main__":
    update_html()
