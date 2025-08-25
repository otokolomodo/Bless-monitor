import requests, time

BASE_URL = "https://bless.network"
paths = ["airdrop", "claim", "rewards", "distribution", "faucet"]
headers = {"User-Agent": "Mozilla/5.0 (AirdropMonitor)"}

def check_paths():
    for path in paths:
        url = f"{BASE_URL}/{path}"
        try:
            r = requests.get(url, headers=headers, timeout=5)
            status = r.status_code
            if status == 200:
                print(f"✅ [FOUND LIVE] {url} (200 OK)")
            elif status == 403:
                print(f"🔒 [BLOCKED] {url} (403 Forbidden, but exists)")
            else:
                print(f"❌ {url} -> {status}")
        except Exception as e:
            print(f"⚠️ {url} -> ERROR {e}")

# Loop every 10 minutes
if __name__ == "__main__":
    while True:
        print("\n🔍 Checking endpoints...")
        check_paths()
        print("⏳ Sleeping 10 minutes...\n")
        time.sleep(600)  # 600s = 10 minutes
