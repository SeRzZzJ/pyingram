import asyncio

import aiohttp

from pyongram.telegram.exceptions.telegram_exceptions import TelegramException


class ApiClient:

    def __init__(self, token: str):
        self._request_uri = f"https://api.telegram.org/bot{token}"

    def __repr__(self):
        return f"{self.__class__.__name__}(self._request_uri={self._request_uri})"

    async def request_to_api(self, tg_method: str, params: dict = None):
        async with aiohttp.ClientSession() as session:
            async with await asyncio.create_task(
                    session.post(self._request_uri + "/" + tg_method, data=params)) as resp:
                return await self._check_response(await resp.json())

    @classmethod
    async def _check_response(cls, res):
        if not res["ok"]:
            raise TelegramException(f"Error code: {res["error_code"]!r}, Description: {res["description"]!r}")
        return res["result"]
