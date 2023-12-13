from pyongram.network.client import ApiClient


class TelegramTypeConstructor:
    def __init__(self, token: str):
        self._client = ApiClient(f"https://api.telegram.org/bot{token}")
