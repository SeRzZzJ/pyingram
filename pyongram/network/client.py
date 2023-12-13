import asyncio

import aiohttp
from pyongram.telegram.exceptions.telegram_exceptions import TelegramException
from typing import AnyStr, Dict


class ApiClient:

    def __init__(self, request_uri: str):
        self._request_uri: str = request_uri

    async def request_to_api(self, tg_method: AnyStr, params: Dict = None):
        async with aiohttp.ClientSession() as session:
            async with session.post(self._request_uri + "/" + tg_method, data=params) as resp:
                return await self._check_response(await asyncio.create_task(resp.json()))

    @classmethod
    async def _check_response(cls, res):
        if not res["ok"]:
            raise TelegramException(f"Error code: {res["error_code"]!r}, Description: {res["description"]!r}")
        return res["result"]
