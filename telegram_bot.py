from aiogram import Bot, types, Dispatcher
import os
import json
from vk_parser import check_new_post
import logging
from config import SLEEP_INTERVAL, USER_ID
import asyncio

bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler(commands="all")
async def all_posts(message: types.Message):
    with open("data_posts.json", encoding="utf-8") as file:
        all_post = json.load(file)

    for k, v in all_post.items():
        href = v["href"]
        text = v["text"]
        if href != all_post["-64474568_1204527"]["href"]:
            await message.answer(f"{href}\n{text}")


async def send_message(user_id, message):
    await bot.send_message(user_id, message)


async def new_posts():
    while True:
        fresh_posts = await check_new_post()
        user_id = USER_ID

        if fresh_posts:
            for k, v in fresh_posts.items():
                href = v["href"]
                text = v["text"]
                logging.info(f'Новый пост: {href}\n{text}')
                await send_message(user_id, f'{href}\n{text}')
        else:
            logging.debug('Нет новых постов')

        await asyncio.sleep(SLEEP_INTERVAL)
