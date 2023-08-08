import asyncio
from aiogram import executor
from telegram_bot import dp, new_posts
from logging_utils import logger, log_handler


def main():
    logger.addHandler(log_handler)

    loop = asyncio.get_event_loop()
    loop.create_task(new_posts())
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
