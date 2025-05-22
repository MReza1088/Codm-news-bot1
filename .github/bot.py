import requests
import time
from bs4 import BeautifulSoup

BOT_TOKEN = "7617887292:AAG2aHTB4bpO-taacPa5A55LpGZj17aMsXs"
CHANNEL_ID = "-1002504090635"
NEWS_URL = "https://www.callofduty.com/blog/mobile"

def get_latest_codm_news():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(NEWS_URL, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        article = soup.find("article")
        if not article:
            return None

        title_tag = article.find("h3")
        link_tag = article.find("a", href=True)
        image_tag = article.find("img")

        if not title_tag or not link_tag:
            return None

        title = title_tag.text.strip()
        link = "https://www.callofduty.com" + link_tag["href"]
        image_url = image_tag["src"] if image_tag else ""

        return {
            "title": title,
            "link": link,
            "image_url": image_url
        }
    except Exception as e:
        print(f"خطا در دریافت اخبار: {e}")
        return None

def send_news(news):
    if not news:
        print("خبر معتبر نیست.")
        return

    message = (
        f"🔥 <b>خبر داغ از کالاف دیوتی موبایل</b>\n\n"
        f"📰 <b>{news['title']}</b>\n"
        f"🔗 <a href='{news['link']}'>مطالعه کامل خبر</a>\n\n"
        f"📢 برای دریافت فوری‌ترین اخبار COD Mobile:\n"
        f"👉 <b>@lm10vfx_codm</b>"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHANNEL_ID,
        "photo": news["image_url"],
        "caption": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=payload)
    print(f"ارسال خبر: {response.text}")

def main():
    last_title = ""

    while True:
        news = get_latest_codm_news()
        if news and news["title"] != last_title:
            send_news(news)
            last_title = news["title"]
        else:
            print("خبر جدیدی نیست یا خطا در دریافت خبر.")

        time.sleep(7200)  # هر ۲ ساعت یک‌بار بررسی

if __name__ == "__main__":
    main()
