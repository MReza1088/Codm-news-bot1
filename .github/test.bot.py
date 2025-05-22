import time
import requests

BOT_TOKEN = "7617887292:AAG2aHTB4bpO-taacPa5A55LpGZj17aMsXs"
CHANNEL_ID = "-1002504090635"

time.sleep(5)

message = "سلام! این یک پیام تستیه که بعد از ۵ ثانیه ارسال شده."

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHANNEL_ID,
    "text": message
}

response = requests.post(url, data=payload)
print(response.text)
