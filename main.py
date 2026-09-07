import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Токен твоего бота
TOKEN = "8227925572:AAF4ytjrUe3Y742DYDnHySCFCx88sPpNYsw"

# ССЫЛКА НА ТВОЕ МИНИ-ПРИЛОЖЕНИЕ (вставь свою ссылку из Шага 2)
WEB_APP_URL = "https://github.com/evulyaa/our-stories.git"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Создаем кнопку, которая открывает Mini App
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💖 Открыть «Наши Истории» 💖",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )
    
    text = (
        "Привет, моя любовь! 🌸\n\n"
        "Я подготовила для тебя кое-что очень особенное...\n"
        "Нажми на кнопку ниже, чтобы открыть наше мини-приложение 💕"
    )
    
    await message.answer(text=text, reply_markup=keyboard)

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот с Мини-приложением запущен! 💕")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
