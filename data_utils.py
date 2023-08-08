import json
import logging
from config import MAX_POSTS


def remove_old_post(post_list):
    if len(post_list) > MAX_POSTS:
        sorted_posts = sorted(post_list.items(), key=lambda x: x[1]['timestamp'])
        oldest_post_id = sorted_posts[1][0]
        del post_list[oldest_post_id]
        logging.info(f"Удален пост: {oldest_post_id}")

        save_data_to_file(post_list)


def save_data_to_file(data):
    with open("data_posts.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
