from bs4 import BeautifulSoup
from http_utils import fetch
from data_utils import remove_old_post, save_data_to_file
from config import VK_URL, HASHTAG
import json
import time


async def check_new_post():
    with open("data_posts.json", encoding="utf-8") as file:
        post_list = json.load(file)

    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 '
            'Safari/537.36'
    }

    response_text = await fetch(VK_URL, headers)

    if response_text:
        data = BeautifulSoup(response_text, 'lxml')
        wall_posts = data.find_all('div', class_='wall_post_cont')

        fresh_posts = {}

        for post in wall_posts:
            post_id = post.get("id").replace('wpt', '')
            text_post = post.find('div', class_='wall_post_text').text

            if post_id in post_list:
                continue
            else:
                timestamp = int(time.time())
                post_list[post_id] = {
                    "href": f'{VK_URL}?w=wall{post_id}',
                    "text": text_post,
                    "timestamp": timestamp
                }

                fresh_posts[post_id] = {
                    "href": f'{VK_URL}?w=wall{post_id}',
                    "text": text_post,
                    "timestamp": timestamp
                }

                if HASHTAG in post_list[post_id]['text']:
                    save_data_to_file(post_list)
                    remove_old_post(post_list)
                    return fresh_posts
                else:
                    save_data_to_file(post_list)

        remove_old_post(post_list)

    return None
