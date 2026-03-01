import requests
import time
from datetime import datetime

# ====== ΒΑΛΕ ΤΑ ΔΙΚΑ ΣΟΥ ======
BOT_TOKEN = "ΒΑΛΕ_ΕΔΩ_ΤΟ_BOT_TOKEN"
CHAT_ID = "ΒΑΛΕ_ΕΔΩ_ΤΟ_CHAT_ID"
CITY = "Thessaloniki"
# ==============================

SPIKE_THRESHOLD = 160  # όριο για alert


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
