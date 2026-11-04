import asyncio
import logging
import os
from threading import Thread
from flask import Flask, request, jsonify
from flask_cors import CORS
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# --- НАСТРОЙКИ ---
TOKEN = os.environ.get("BOT_TOKEN", "8541102686:AAFSSiQAMLgdc19LLjAzHQaPwFCYhRQJ21Y")
WEB_APP_URL = "https://essential676767-wq.github.io/durak-game1/"

bot = Bot(token=TOKEN)
dp = Dispatcher()
bot_loop = None

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🃏 НАЧАТЬ ИГРУ",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ])

    welcome_text = (
        f"👋 Привет, <b>{message.from_user.first_name}</b>!\n\n"
        "Добро пожаловать в <b>Дурак на деньги</b>! 💰\n\n"
        "🃏 <b>Правила просты:</b>\n"
        "• Играй против Алексея (ИИ).\n"
        "• Делай ставки и выигрывай деньги.\n"
        "• Используй магазин, чтобы получать бонусы за рекламу.\n\n"
        "Нажми на кнопку ниже, чтобы начать играть прямо сейчас! 👇"
    )

    await message.answer(
        text=welcome_text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )

app = Flask(__name__)
CORS(app)

@app.route('/')
def health_check():
    return "Durak Bot is running!", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

async def main():
    logging.basicConfig(level=logging.INFO)
    Thread(target=run_flask, daemon=True).start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())