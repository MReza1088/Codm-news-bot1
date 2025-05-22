import requests
import hashlib
import os

BOT_TOKEN = '7617887292:AAG2aHTB4bpO-taacPa5A55LpGZj17aMsXs'
CHANNEL_ID = '-1002504090635'
PAGE_URL = 'https://www.callofduty.com/mobile'

# محل ذخیره آخرین خبر
LAST_HASH_FILE = 'last_news_hash.txt'

# دریافت خبر از سایت رسمی (به‌صورت ساده)
def fetch_latest_news():
    try:
        response = requests.get(PAGE_URL, timeout=10)
        if response.status_code == 200:
            content = response.text

            # استخراج عکس اولی سایت (نمونه ساده)
            start = content.find('<img')
            src_index = content.find('src="', start) + 5
            end_index = content.find('"', src_index)
            image_url = content[src_index:end_index] if src_index > 4 else None

            # ساخت هش از محتوای خبر برای جلوگیری از تکراری بودن
            news_hash = hashlib.md5(content.encode()).hexdigest()

            return {
                'text': "🔥 خبر جدید از سایت رسمی Call of Duty Mobile!\n\n"
                        "💙😉🔥👻🎮🦁☀️🎃\n"
                        "آخرین اخبار را در لینک زیر بخوان:\n"
                        f"{PAGE_URL}\n\n"
                        "🆔 @lm10vfx_codm",
                'image_url': image_url,
                'hash': news_hash
            }
        else:
            return None
    except Exception as e:
        return None

# چک تکراری نبودن خبر
def is_new_news(news_hash):
    if os.path.exists(LAST_HASH_FILE):
        with open(LAST_HASH_FILE, 'r') as f:
            last_hash = f.read().strip()
        return last_hash != news_hash
    return True

# ذخیره هش جدید
def save_news_hash(news_hash):
    with open(LAST_HASH_FILE, 'w') as f:
        f.write(news_hash)

# ارسال به تلگرام
def send_to_telegram(news):
    if news['image_url']:
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto'
        data = {
            'chat_id': CHANNEL_ID,
            'photo': news['image_url'],
            'caption': news['text']
        }
    else:
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        data = {
            'chat_id': CHANNEL_ID,
            'text': news['text']
        }

    response = requests.post(url, data=data)
    return response.ok

# اجرای اصلی
if __name__ == '__main__':
    news = fetch_latest_news()
    if news and is_new_news(news['hash']):
        if send_to_telegram(news):
            save_news_hash(news['hash'])
