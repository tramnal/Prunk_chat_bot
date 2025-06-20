from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import logging

from config import BOT_TOKEN
from handlers import (
    greeting, bad_words, morning, inactivity, wisdom,
    word_triggers, activity_tracker, random_beer,
    wiki_google, voice_response, weekly_stats
)

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        greeting.router,
        bad_words.router,
        morning.router,
        inactivity.router,
        wisdom.router,
        word_triggers.router,
        activity_tracker.router,
        random_beer.router,
        wiki_google.router,
        voice_response.router,
        weekly_stats.router,
    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
