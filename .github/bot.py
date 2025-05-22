import requests
from bs4 import BeautifulSoup
from translatepy import Translator
import telebot
import time
import json
import os

TOKEN = "7617887292:AAG2aHTB4bpO-taacPa5A55LpGZj17aMsXs"
CHANNEL_ID = "-1002504090635"
bot = telebot.TeleBot(TOKEN)

LAST_NEWS_FILE = "last_news.json"
translator = Translator()

def get_last_news():
    if os.path.exists(LAST_NEWS_FILE):
        with open(LAST_NEWS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_last_news(news):
    with open(LAST_NEWS_FILE, "w") as f:
        json.dump(news, f)

def get_codm_news():
    url = "https://www.callofduty.com/mobile"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    article = soup.find("div", class_="news-feed-card")
    if not article:
        return None

    title = article.find("h3").text.strip()
    link = "https://www.callofduty.com" + article.find("a")["href"]
    img_tag = article.find("img")
    image_url = img_tag["src"] if img_tag else None

    return {"title": title, "link": link, "image": image_url}

def translate_text(text):
    try:
        result = translator.translate(text, "Farsi")
        return result.result
    except:
        return text

def fix_translation(text):
    replacements = {
        "Call of Duty Mobile": "کالاف موبایل",
        "players": "بازیکن‌ها",
        "game": "بازی",
        "update": "آپدیت",
        "new": "جدید",
        "weapon": "سلاح",
        "map": "مپ",
        "season": "فصل",
        "event": "رویداد",
        "challenge": "چالش",
        # هرچی که فکر می‌کنی مناسب‌تره اضافه کن
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

def main():
    last_news = get_last_news()
    news = get_codm_news()

    if news and news["link"] != last_news.get("link"):
        translated_title = translate_text(news["title"])
        translated_title = fix_translation(translated_title)

        message = f"🔥 {translated_title}\n\n{news['link']}\n\n💙😉👻🎮🦁☀️🎃\n@lm10vfx_codm"

        if news["image"]:
            bot.send_photo(CHANNEL_ID, photo=news["image"], caption=message)
        else:
            bot.send_message(CHANNEL_ID, message)

        save_last_news(news)

if __name__ == "__main__":
    main()
