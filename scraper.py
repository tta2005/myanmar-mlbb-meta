import os

def update_web():
    # ဤနေရာတွင် နောက်အဆင့်တွင် တကယ့် Live API Link ကို ချိတ်ပါမည်
    # လောလောဆယ် Data Flow အလုပ်လုပ်ကြောင်း အတည်ပြုရန် Akai ကို နမူနာသုံးပါမည်
    live_data = [
        {
            "name": "Akai", 
            "wr": "52.8%", 
            "img": "https://img.mobilelegends.com/group1/M00/00/01/Cq8JEmL_W_uAP5YRAAAd-L98mXo358.png",
            "tier": "S"
        },
        {
            "name": "Minsitthar", 
            "wr": "51.4%", 
            "img": "https://img.mobilelegends.com/group1/M00/00/01/Cq8JEmL_W_uAP5YRAAAd-L98mXo358.png",
            "tier": "A"
        }
    ]

    cards_html = ""
    for h in live_data:
        cards_html += f'''
        <div class="bg-slate-900 p-6 rounded-3xl border border-yellow-500/20 text-center">
            <img src="{h['img']}" class="w-20 h-20 mx-auto rounded-full border-2 border-yellow-500 mb-4 shadow-lg shadow-yellow-500/20">
            <h3 class="text-xl font-bold text-white uppercase tracking-wider">{h['name']}</h3>
            <p class="text-yellow-500 font-mono text-lg font-bold mt-2">Win Rate: {h['wr']}</p>
            <div class="mt-4 inline-block bg-yellow-600 text-[10px] px-3 py-1 rounded-full font-black text-black">TIER {h['tier']}</div>
        </div>
        '''

    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    start, end = "", ""
    parts = content.split(start)
    res = parts[1].split(end)
    final_html = parts[0] + start + cards_html + end + res[1]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

if __name__ == "__main__":
    update_web()
