import json

# ဒါက နမူနာ Data ပါ (နောက်ပိုင်းမှာ ဒါကို MLBB Site ကနေ လှမ်းဆွဲတဲ့ Code နဲ့ အစားထိုးပါမယ်)
new_meta_heroes = [
    {"name": "Tigreal", "tier": "S", "wr": "54.2%", "tip": "Flicker + Ulti ကို Timing ကိုက်ကိုက်သုံးပါ။"},
    {"name": "Nolan", "tier": "S", "wr": "53.8%", "tip": "Energy ထိန်းဖို့ Blue Buff ကို အဓိကထားစားပါ။"},
    {"name": "Vexana", "tier": "A", "wr": "51.5%", "tip": "Passive ပေါက်အောင် Skill တွေကို စုပစ်ပါ။"}
]

def update_web():
    # index.html ကို ဖတ်တယ်
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Hero Card တွေ ထည့်မယ့် ပုံစံကို တည်ဆောက်တယ်
    hero_html = ""
    for hero in new_meta_heroes:
        hero_html += f"""
        <div class="bg-slate-800 p-5 rounded-xl border border-slate-600 hover:border-yellow-500 transition cursor-pointer">
            <div class="flex justify-between items-center mb-3">
                <h3 class="text-xl font-bold">{hero['name']}</h3>
                <span class="bg-red-600 text-xs px-2 py-1 rounded">Tier {hero['tier']}</span>
            </div>
            <p class="text-sm text-slate-300 mb-4">Win Rate: {hero['wr']}</p>
            <p class="text-yellow-400 text-sm italic">"{hero['tip']}"</p>
        </div>
        """

    # HTML ထဲက hero-list div ထဲကို အစားထိုးတယ်
    # (မှတ်ချက်- index.html ထဲမှာ id="hero-list" ပါတဲ့နေရာကို ရှာပြီး ပြင်ပေးမှာပါ)
    print("Web Data Updated!")

update_web()
