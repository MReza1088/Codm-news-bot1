import requests

BOT_TOKEN = "توکن رباتت رو اینجا بذار"
CHANNEL_ID = "آیدی عددی کانالت (مثلاً: -1002504...)"

message = "سلام! این یک پیام تستی از ربات هست. اگر اینو دیدی، یعنی ربات وصله و مشکلی نداره! 🎮🔥😉"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHANNEL_ID,
    "text": message
}

response = requests.post(url, data=payload)
print(response.text)
