import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command

# TOKEN (Render Environment Variables dan olinadi)
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start_handler(message: types.Message):
    await message.answer("👋 Salom! Men ishlayapman ✅")

async
