import telebot
import random

# توکن دریافتی از BotFather را دقیقاً بین این دو کوتیشن قرار دهید:
TOKEN = "8971653117:AAHr2x5gibHAT6OZQyY5BiiK5iv-YQpLUJY"

bot = telebot.TeleBot(TOKEN)

# بانک لغات و اصطلاحات انگلیسی برای آموزش
LESSONS = [
    {
        "phrase": "A piece of cake",
        "fa_meaning": "مثل آب خوردن (خیلی ساده و آسان)",
        "example": "The English exam was a piece of cake!"
    },
    {
        "phrase": "Hit the books",
        "fa_meaning": "شروع به درس خواندن سفت و سخت کردن",
        "example": "I have a test tomorrow, so I need to hit the books."
    },
    {
        "phrase": "Under the weather",
        "fa_meaning": "کمی ناخوش بودن، مریض‌احوال بودن",
        "example": "I feel under the weather today, so I won't go to school."
    },
    {
        "phrase": "Once in a blue moon",
        "fa_meaning": "به‌ندرت، هر صد سال یک‌بار",
        "example": "He only visits us once in a blue moon."
    }
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = (
        "سلام! به ربات آموزش انگلیسی خوش آمدید. 🇬🇧✨\n\n"
        "برای دریافت یک لغت یا اصطلاح جدید به همراه مثال، دستور /learn را بفرستید."
    )
    bot.reply_to(message, text)

@bot.message_handler(commands=['learn'])
def send_lesson(message):
    item = random.choice(LESSONS)
    response = (
        f"📌 **{item['phrase']}**\n\n"
        f"🇮🇷 معنی: {item['fa_meaning']}\n"
        f"📝 مثال: *{item['example']}*"
    )
    bot.reply_to(message, response, parse_mode="Markdown")

print("ربات روشن شد...")
bot.infinity_polling()
