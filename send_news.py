import feedparser
import requests

# Sabitler: Güvenli kullanım için bu değerleri GitHub Secrets'ten almanız önerilir.
RSS_FEED = "https://bianet.org/rss/bianet"
BOT_TOKEN = "7518339219:AAHha9VhJAGlj3H5chtLmwoRJQJQPdUie8U"  # Örnek token, secret olarak ekleyin
CHAT_ID = "-1002218980506"  # Örnek grup/kanal ID'si

TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def fetch_latest_news():
    feed = feedparser.parse(RSS_FEED)
    if feed.entries:
        return feed.entries[0]  # En son haberi alır
    return None

def send_message(message):
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(TELEGRAM_API_URL, data=payload)
    return response.json()

def main():
    latest_news = fetch_latest_news()
    if latest_news:
        # Mesaj içeriğini başlık ve link olacak şekilde oluşturuyoruz.
        message = f"<b>{latest_news.title}</b>\n{latest_news.link}"
        result = send_message(message)
        print("Mesaj gönderildi:", result)
    else:
        print("Yeni haber bulunamadı.")

if __name__ == "__main__":
    main()
