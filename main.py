import requests, time, os

BASE_URL = "https://bless.network"
paths = ["airdrop", "claim", "rewards", "distribution", "faucet"]
headers = {"User-Agent": "Mozilla/5.0 (BlessMonitor)"}

# 🔹 Telegram Bot settings
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")   # set in Railway variables
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")        # set in Railway variables

def send_telegram(message: str):
    if TELEGRAM_TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message}
        try:
            r = requests.post(url, data=data, timeout=5)
            print(f"📨 Telegram response: {r.status_code} | {r.text}")
        except Exception as e:
            print(f"⚠️ Failed to send Telegram message: {e}")
    else:
        print("⚠️ TELEGRAM_TOKEN or TELEGRAM_CHAT_ID not set")
        
def check_paths():
    for path in paths:
        url = f"{BASE_URL}/{path}"
        try:
            r = requests.get(url, headers=headers, timeout=5)
            status = r.status_code
            if status == 200:
                msg = f"✅ LIVE: {url} is now OPEN (200 OK)"
                print(msg)
                send_telegram(msg)
            elif status == 403:
                print(f"🔒 BLOCKED: {url} (403 Forbidden)")
            else:
                print(f"❌ {url} -> {status}")
        except Exception as e:
            print(f"⚠️ {url} -> ERROR {e}")

if __name__ == "__main__":
    while True:
        print("\n🔍 Checking endpoints...")
        check_paths()
        print("⏳ Sleeping 10 minutes...\n")
        time.sleep(30)  # 10 minutes
