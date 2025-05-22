import requests
import time

BOT_TOKEN = "7617887292:AAG2aHTB4bpO-taacPa5A55LpGZj17aMsXs"
CHANNEL_ID = "-1002504090635"

time.sleep(10)  # 10 ثانیه صبر می‌کنه

message = "سلام! این پیام بعد از ۱۰ ثانیه ارسال شد. ربات فعال است! 🎮🔥😉"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHANNEL_ID,
    "text": message
}

response = requests.post(url, data=payload)
print(response.text)
