import os

def update_dashboard():
    # Phase 2 အတွက် API ဒေတာပုံစံ (ယခုလောလောဆယ် နမူနာပြသရန်)
    heroes = [
        {"name": "Akai", "wr": "52.8%", "img": "https://img.mobilelegends.com/group1/M00/00/01/Cq8JEmL_W_uAP5YRAAAd-L98mXo358.png", "tier": "S"},
        {"name": "Tigreal", "wr": "54.1%", "img": "https://img.mobilelegends.com/group1/M00/00/01/Cq8JEmL_W_uAP5YRAAAd-L98mXo358.png", "tier": "S"},
        {"name": "Nolan", "wr": "55.2%", "img": "https://img.mobilelegends.com/group1/M00/00/AF/Cq8JEmT_V7uAL6V0AAAb8L98mXo726.png", "tier": "S"}
    ]

    new_content = ""
    for h in heroes:
        new_content += f'''
        <div class="hero-card bg-slate-900 p-8 rounded-3xl border border-yellow-500/20 shadow-2xl text-center">
            <img src="{h['img']}" class="w-24 h-24 mx-auto rounded-full border-4 border-yellow-500 mb-4 shadow-lg">
            <h3 class="text-2xl font-bold text-white uppercase tracking-tighter">{h['name']}</h3>
            <p class="text-yellow-500 font-mono text-xl font-bold mt-2">Win Rate: {h['wr']}</p>
            <div class="mt-4 inline-block bg-red-600 text-[10px] px-3 py-1 rounded-full font-black text-white italic">LIVE DATA</div>
        </div>
        '''

    # ဖိုင်ဖတ်ပြီး Marker ကြားထဲ ဒေတာထည့်ခြင်း
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()

        start_marker = ""
        end_marker = ""

        # စာသားဖြတ်ထုတ်ခြင်း logic
        before = html.split(start_marker)[0]
        after = html.split(end_marker)[1]

        final_html = before + start_marker + "\n" + new_content + "\n" + end_marker + after

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(final_html)
        print("Dashboard updated successfully!")

    except Exception as e:
        print(f"Update failed: {str(e)}")

if __name__ == "__main__":
    update_dashboard()
