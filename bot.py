import asyncio
import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram import F

load_dotenv()

BOT_TOKEN = os.getenv("MAX_RENT_BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден!")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer("💎 MAX RENT BOT запущен на Render\n\nБот работает.")

@dp.message()
async def any_message(message: Message):
    await message.answer("✅ Получено")

async def main():
    print("🚀 Бот запущен на Render")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())