import aiohttp
import logging


async def fetch(url, headers):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                response.raise_for_status()
                return await response.text()
    except aiohttp.ClientError as e:
        error_message = f"Произошла ошибка во время запроса: {e}"
        if isinstance(e, aiohttp.ClientResponseError):
            status_code = e.status
            response_text = await e.response.text()
            error_message += f"\nКод статуса: {status_code}\nОтвет сервера: {response_text}"
        logging.error(error_message)
        return None
