from typing_extensions import deprecated

from aiohttp import web_app

from pyongram.utils.useful_functions import remove_none_value


class Buttons:
    @staticmethod
    def keyboard():
        return ReplyKeyboardButtons()

    @staticmethod
    def inline_keyboard():
        return InlineKeyboardButtons()


class ReplyKeyboardButtons:
    @staticmethod
    def text(text):
        return {"text": text}

    @staticmethod
    def request_user(text, request_id, user_is_bot=None, user_is_premium=None):
        return {"text": text, "request_user": remove_none_value({"request_id": request_id,
                                                                 "user_is_bot": user_is_bot,
                                                                 "user_is_premium": user_is_premium})}

    @staticmethod
    def request_chat(text,
                     request_id,
                     chat_is_channel,
                     chat_is_forum=None,
                     chat_has_username=None,
                     chat_is_created=None,
                     user_administrator_rights=None,
                     bot_administrator_rights=None,
                     bot_is_member=None):
        return {"text": text, "request_chat": remove_none_value({"request_id": request_id,
                                                                 "chat_is_channel": chat_is_channel,
                                                                 "chat_is_forum": chat_is_forum,
                                                                 "chat_has_username": chat_has_username,
                                                                 "chat_is_created": chat_is_created,
                                                                 "user_administrator_rights": remove_none_value(
                                                                     user_administrator_rights),
                                                                 "bot_administrator_rights": remove_none_value(
                                                                     bot_administrator_rights),
                                                                 "bot_is_member": bot_is_member})}

    @staticmethod
    def request_contact(text):
        return {"text": text, "request_contact": True}

    @staticmethod
    def request_location(text):
        return {"text": text, "request_location": True}

    @staticmethod
    def request_poll(text, poll_type):
        return {"text": text, "request_poll": poll_type}

    @staticmethod
    def web_app(text, url):
        return {"text": text, web_app: {"url": url}}

    @staticmethod
    def request_users(text, request_id, user_is_bot=None, user_is_premium=None, max_quantity=None):
        return {"text": text, "request_users": remove_none_value({"request_id": request_id,
                                                                  "user_is_bot": user_is_bot,
                                                                  "user_is_premium": user_is_premium,
                                                                  "max_quantity": max_quantity})}


class InlineKeyboardButtons:
    @staticmethod
    def url(text, url):
        return {"text": text, "url": url}

    @staticmethod
    def callback_data(text, data):
        return {"text": text, "callback_data": data}

    @staticmethod
    def web_app(text, url):
        return {"text": text, web_app: {"url": url}}

    @staticmethod
    def login_url(text, url, forward_text=None, bot_username=None, request_write_access=None):
        return {"text": text, "request_user": remove_none_value({"url": url,
                                                                 "forward_text": forward_text,
                                                                 "bot_username": bot_username,
                                                                 "request_write_access": request_write_access})}

    @staticmethod
    def switch_inline_query(text, query):
        return {"text": text, "switch_inline_query": query}

    @staticmethod
    def switch_inline_query_current_chat(text, query):
        return {"text": text, "switch_inline_query_current_chat": query}

    @staticmethod
    def switch_inline_query_chosen_chat(text,
                                        query,
                                        allow_user_chats,
                                        allow_bot_chats=None,
                                        allow_group_chats=None,
                                        allow_channel_chats=None):
        return {"text": text, "request_chat": remove_none_value({"query": query,
                                                                 "allow_user_chats": allow_user_chats,
                                                                 "allow_bot_chats": allow_bot_chats,
                                                                 "allow_group_chats": allow_group_chats,
                                                                 "allow_channel_chats": allow_channel_chats})}

    @staticmethod
    def callback_game(text):
        return {"text": text, "callback_game": {}}

    @staticmethod
    def pay(text):
        return {"text": text, "pay": True}
