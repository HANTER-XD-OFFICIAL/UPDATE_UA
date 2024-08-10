import json
import random
import requests

def load_config(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP ত্রুটি চেক করতে
        if response.headers['Content-Type'].startswith('application/json'):
            return response.json()
        else:
            print("Unexpected content type:", response.headers['Content-Type'])
            return None
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

def Samsung(config):
    Anderson = random.choice(config.get("Anderson", []))
    model = random.choice(config.get("model", []))
    vir = str(random.choice(range(111111111, 999999999)))
    cho = str(random.choice(range(43, 447)))
    fb = random.choice(config.get("fb", []))
    FBAN = fb.split("|")[1]
    platform = fb.split("|")[0]
    ua = (
        f"Dalvik/2.1.0 (Linux; U; Android {Anderson}; {model} Build/LRX22C) "
        f"[FBAN/{FBAN};FBAV/{cho}.0.0.15.89;FBPN/{platform};FBLC/sv_SE;"
        f"FBBV/{vir};FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;"
        f"FBDV/{model};FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;"
        f"FBDM={{density={str(random.choice(range(1, 4)))}.0,"
        f"width={str(random.choice(range(720, 1500)))},"
        f"height={str(random.choice(range(1500, 2000)))}}};FB_FW/1;]"
    )
    return ua

# Example usage
config_url = "https://github.com/HANTER-XD-OFFICIAL/UPDATE_UA/blob/main/user_agent.json"
config = load_config(config_url)
if config:
    user_agent = Samsung(config)
    print(user_agent)