import requests
import time
from datetime import datetime

# ====== ΒΑΛΕ ΤΑ ΔΙΚΑ ΣΟΥ ======
BOT_TOKEN = "8695935379:AAG378T7orJ5lVAOhDc68fSHtXNht78T7pA"
CHAT_ID = "8627175123"
CITY = "Thessaloniki"
# ==============================

SPIKE_THRESHOLD = 160  # όριο για alert


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)


def get_fake_wolt_demand():
    # Προσωρινό demo demand (μέχρι να βάλουμε real API)
    import random
    return random.randint(80, 200)


def run_sniper():
    demand = get_fake_wolt_demand()
    now = datetime.now().strftime("%H:%M")

    print(f"{now} → {demand}")

    if demand >= SPIKE_THRESHOLD:
        message = f"🚨 WOLT SPIKE ALERT 🚨\n\n{now} → {demand}"
        send_telegram_message(message)


if __name__ == "__main__":
    print("Wolt AI Sniper Started...")

    while True:
        run_sniper()
        time.sleep(600)  # κάθε 10 λεπτά
