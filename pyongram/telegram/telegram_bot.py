import asyncio
from typing import Optional, List, LiteralString

from pyongram import TelegramException
from pyongram.session.sessions import MemorySession
from pyongram.telegram.methods.telegram_bot_api import TelegramBotApi
from pyongram import Context
from pyongram.router.routers import FormRouter
from pyongram.utils.update_parser import UpdateParser


class TelegramBot:
    def __init__(self, token):
        self._bot = TelegramBotApi(token)
        self._routers = []
        self._sessions = []

    def use_router(self, router):
        self._routers.append(router)


class TelegramBotLongPolling(TelegramBot):
    def run_infinity_loop(self,
                          limit: int = 100,
                          timeout: int = 10,
                          allowed_updates: Optional[List[LiteralString]] = None):
        asyncio.run(self._start_long_polling(limit, timeout, allowed_updates))

    async def _start_long_polling(self,
                                  limit: int = 100,
                                  timeout: int = 10,
                                  allowed_updates: Optional[List[LiteralString]] = None):
        offset = -1
        allowed_updates = allowed_updates
        if allowed_updates is None:
            allowed_updates = [
                "message",
                "edited_message",
                "channel_post",
                "edited_channel_post",
                "inline_query",
                "chosen_inline_result",
                "callback_query",
                "shipping_query",
                "pre_checkout_query",
                "poll",
                "poll_answer",
                "my_chat_member",
                "chat_member",
                "chat_join_request"
            ]

        while True:
            for update in await self._bot.get_updates(offset, limit, timeout, allowed_updates):
                update_id = update["update_id"]
                try:
                    await self._handle_state_and_router(update)
                except TelegramException as t:
                    print(t.with_traceback(None))
                    await self._bot.get_updates(max(offset, update_id) + 1, limit, timeout, allowed_updates)
                finally:
                    offset = max(offset, update_id) + 1

    async def _handle_state_and_router(self, update):
        if not self._sessions:
            self._sessions.append(MemorySession(update))

        update_parser = UpdateParser(update)
        session = [session for session in self._sessions if session.user_id == update_parser.update_from_id()][0]

        if session:
            form_router = [form_router for form_router in self._routers if (isinstance(form_router, FormRouter) and
                                                                            session.check_the_session_form(
                                                                                form_router.name))]
            print(form_router)
            if form_router:
                print(type(form_router))
                await self._handle_router(update, form_router[0], session)
            else:
                for router in self._routers:
                    if isinstance(router, FormRouter):
                        print(isinstance(router, FormRouter))
                        continue
                    await self._handle_router(update, router, session)
        else:
            self._sessions.append(MemorySession(update))

    async def _handle_router(self, update, router, session):
        for handler in filter(
                lambda hnd: hnd.update_type == list(update.keys())[-1] and hnd.field in update[hnd.update_type],
                router.handlers):
            if handler.out_data(update[handler.update_type]):
                await handler.handle(Context(update, self._bot, session))
                if handler.is_next_handler:
                    continue
                else:
                    break


class TelegramBotWebHooks(TelegramBot):
    pass
