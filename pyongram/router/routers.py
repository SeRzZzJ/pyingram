from abc import ABC
from types import FunctionType

from pyongram.router.handler import Handler


class BaseRouter(ABC):
    def __init__(self):
        self._handlers = []

    def __repr__(self):
        return f"{self.__class__.__name__}(self._handlers={self._handlers})"

    @property
    def handlers(self):
        return self._handlers

    def assign(self, routers):
        for router in routers:
            self._handlers.extend(router.handlers)

    def on(self, *, update_type, field, trigger=None, is_next_handler=False):
        self._check_handler_trigger_and_field_update_type_isinstance(update_type=update_type,
                                                                     field=field,
                                                                     trigger=trigger)
        return self._returned_build_decorator(update_type=update_type,
                                              field=field,
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def on_all(self, *, is_next_handler=False):
        return self.on(update_type="", field="", trigger=lambda _: True, is_next_handler=is_next_handler)

    def on_message(self, *, is_next_handler=False):
        return self.on(update_type="message", field="", trigger=lambda _: True, is_next_handler=is_next_handler)

    def on_edited_message(self, *, is_next_handler=False):
        return self.on(update_type="edited_message", field="", trigger=lambda _: True, is_next_handler=is_next_handler)

    def on_channel_post(self, *, is_next_handler=False):
        return self.on(update_type="channel_post", field="", trigger=lambda _: True, is_next_handler=is_next_handler)

    def on_edited_channel_post(self, *, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="", trigger=lambda _: True,
                       is_next_handler=is_next_handler)

    def on_message_reaction(self, *, is_next_handler=False):
        return self.on(update_type="message_reaction", field="", trigger=lambda _: True,
                       is_next_handler=is_next_handler)

    def on_inline_query(self, *, is_next_handler=False):
        return self.on(update_type="inline_query", field="", trigger=lambda _: True, is_next_handler=is_next_handler)

    def on_chosen_inline_result(self, *, is_next_handler=False):
        return self.on(update_type="chosen_inline_result", field="", trigger=lambda _: True,
                       is_next_handler=is_next_handler)

    def on_callback_query(self, *, is_next_handler=False):
        return self.on(update_type="callback_query", field="", trigger=lambda _: True, is_next_handler=is_next_handler)

    def on_shipping_query(self, *, is_next_handler=False):
        return self.on(update_type="shipping_query", field="", trigger=lambda _: True, is_next_handler=is_next_handler)

    def on_pre_checkout_query(self, *, is_next_handler=False):
        return self.on(update_type="pre_checkout_query", field="", trigger=lambda _: True,
                       is_next_handler=is_next_handler)

    def on_poll(self, *, is_next_handler=False):
        return self.on(update_type="poll", field="", trigger=lambda _: True, is_next_handler=is_next_handler)

    def on_poll_answer(self, *, is_next_handler=False):
        return self.on(update_type="poll_answer", field="", trigger=lambda _: True, is_next_handler=is_next_handler)

    def on_my_chat_member(self, *, is_next_handler=False):
        return self.on(update_type="my_chat_member", field="", trigger=lambda _: True, is_next_handler=is_next_handler)

    def on_chat_member(self, *, is_next_handler=False):
        return self.on(update_type="chat_member", field="", trigger=lambda _: True, is_next_handler=is_next_handler)

    def on_chat_join_request(self, *, is_next_handler=False):
        return self.on(update_type="chat_join_request", field="", trigger=lambda _: True,
                       is_next_handler=is_next_handler)

    def _returned_build_decorator(self, update_type, field, out_data=None, is_next_handler=False):
        def decorator(handler_fn):
            self._handlers.append(
                Handler(update_type=update_type,
                        field=field,
                        out_data=out_data,
                        handler_fn=handler_fn,
                        is_next_handler=is_next_handler))

        return decorator

    @classmethod
    def _check_handler_trigger_isinstance(cls, *, trigger=None):
        if not isinstance(trigger, FunctionType):
            raise TypeError()

    @classmethod
    def _check_handler_trigger_and_field_isinstance(cls, *, field, trigger=None):
        if not isinstance(field, str):
            raise TypeError()
        cls._check_handler_trigger_isinstance(trigger=trigger)

    @classmethod
    def _check_handler_trigger_and_field_update_type_isinstance(cls, *, update_type, field, trigger=None):
        if not isinstance(update_type, str):
            raise TypeError()
        cls._check_handler_trigger_and_field_isinstance(field=field, trigger=trigger)


class Router(BaseRouter):
    def __init__(self):
        super().__init__()

    def command(self, *, trigger, is_next_handler=False):
        return self.on(update_type="message",
                       field="text",
                       trigger=lambda msg: msg["text"] == f"/{trigger}",
                       is_next_handler=is_next_handler)

    def start(self, is_next_handler=False):
        return self.on(update_type="message",
                       field="text",
                       trigger=lambda msg: msg["text"] == "/start",
                       is_next_handler=is_next_handler)

    def help(self, is_next_handler=False):
        return self.on(update_type="message",
                       field="text",
                       trigger=lambda msg: msg["text"] == "/help",
                       is_next_handler=is_next_handler)

    def settings(self, is_next_handler=False):
        return self.on(update_type="message",
                       field="text",
                       trigger=lambda msg: msg["text"] == "/settings",
                       is_next_handler=is_next_handler)

    def admin(self, is_next_handler=False):
        return self.on(update_type="message",
                       field="text",
                       trigger=lambda msg: msg["text"] == "/admin",
                       is_next_handler=is_next_handler)

    def text(self, *, trigger, is_next_handler=False):
        return self.on(update_type="message", field="text", trigger=trigger, is_next_handler=is_next_handler)

    def animation(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="animation", trigger=trigger, is_next_handler=is_next_handler)

    def audio(self, *, trigger, is_next_handler=False):
        return self.on(update_type="message", field="audio", trigger=trigger, is_next_handler=is_next_handler)

    def document(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="document", trigger=trigger, is_next_handler=is_next_handler)

    def photo(self, *, trigger, is_next_handler=False):
        return self.on(update_type="message", field="photo", trigger=trigger, is_next_handler=is_next_handler)

    def sticker(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="sticker", trigger=trigger, is_next_handler=is_next_handler)

    def story(self, *, trigger, is_next_handler=False):
        return self.on(update_type="message", field="story", trigger=trigger, is_next_handler=is_next_handler)

    def video(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="video", trigger=trigger, is_next_handler=is_next_handler)

    def video_note(self, *, trigger, is_next_handler=False):
        return self.on(update_type="message", field="video_note", trigger=trigger, is_next_handler=is_next_handler)

    def voice(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="voice", trigger=trigger, is_next_handler=is_next_handler)

    def contact(self, *, trigger, is_next_handler=False):
        return self.on(update_type="message", field="contact", trigger=trigger, is_next_handler=is_next_handler)

    def dice(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="dice", trigger=trigger, is_next_handler=is_next_handler)

    def game(self, *, trigger, is_next_handler=False):
        return self.on(update_type="message", field="game", trigger=trigger, is_next_handler=is_next_handler)

    def poll(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="poll", trigger=trigger, is_next_handler=is_next_handler)

    def venue(self, *, trigger, is_next_handler=False):
        return self.on(update_type="message", field="venue", trigger=trigger, is_next_handler=is_next_handler)

    def location(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="location", trigger=trigger, is_next_handler=is_next_handler)

    def invoice(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="invoice", trigger=trigger, is_next_handler=is_next_handler)

    def author_signature(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="author_signature", trigger=trigger,
                       is_next_handler=is_next_handler)

    def new_chat_members(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="new_chat_members", trigger=trigger,
                       is_next_handler=is_next_handler)

    def left_chat_member(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="left_chat_member", trigger=trigger,
                       is_next_handler=is_next_handler)

    def new_chat_title(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="new_chat_title", trigger=trigger, is_next_handler=is_next_handler)

    def new_chat_photo(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="new_chat_photo", trigger=trigger, is_next_handler=is_next_handler)

    def delete_chat_photo(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="delete_chat_photo", trigger=trigger,
                       is_next_handler=is_next_handler)

    def group_chat_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="group_chat_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def supergroup_chat_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="supergroup_chat_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_chat_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="channel_chat_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def message_auto_delete_timer_changed(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="message_auto_delete_timer_changed", trigger=trigger,
                       is_next_handler=is_next_handler)

    def migrate_to_chat_id(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="migrate_to_chat_id", trigger=trigger,
                       is_next_handler=is_next_handler)

    def migrate_from_chat_id(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="migrate_from_chat_id", trigger=trigger,
                       is_next_handler=is_next_handler)

    def pinned_message(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="pinned_message", trigger=trigger, is_next_handler=is_next_handler)

    def successful_payment(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="successful_payment", trigger=trigger,
                       is_next_handler=is_next_handler)

    def user_shared(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="user_shared", trigger=trigger, is_next_handler=is_next_handler)

    def chat_shared(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="chat_shared", trigger=trigger, is_next_handler=is_next_handler)

    def connected_website(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="connected_website", trigger=trigger,
                       is_next_handler=is_next_handler)

    def write_access_allowed(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="write_access_allowed", trigger=trigger,
                       is_next_handler=is_next_handler)

    def passport_data(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="passport_data", trigger=trigger, is_next_handler=is_next_handler)

    def proximity_alert_triggered(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="proximity_alert_triggered", trigger=trigger,
                       is_next_handler=is_next_handler)

    def forum_topic_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="forum_topic_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def forum_topic_edited(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="forum_topic_edited", trigger=trigger,
                       is_next_handler=is_next_handler)

    def forum_topic_closed(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="forum_topic_closed", trigger=trigger,
                       is_next_handler=is_next_handler)

    def general_forum_topic_hidden(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="general_forum_topic_hidden", trigger=trigger,
                       is_next_handler=is_next_handler)

    def general_forum_topic_unhidden(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="general_forum_topic_unhidden", trigger=trigger,
                       is_next_handler=is_next_handler)

    def video_chat_scheduled(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="video_chat_scheduled", trigger=trigger,
                       is_next_handler=is_next_handler)

    def video_chat_started(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="video_chat_started", trigger=trigger,
                       is_next_handler=is_next_handler)

    def video_chat_ended(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="video_chat_ended", trigger=trigger,
                       is_next_handler=is_next_handler)

    def video_chat_participants_invited(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="video_chat_participants_invited", trigger=trigger,
                       is_next_handler=is_next_handler)

    def web_app_data(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message", field="web_app_data", trigger=trigger, is_next_handler=is_next_handler)

    def edited_text(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_message", field="text", trigger=trigger, is_next_handler=is_next_handler)

    def edited_animation(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="animation", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_audio(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_message", field="audio", trigger=trigger, is_next_handler=is_next_handler)

    def edited_document(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="document", trigger=trigger, is_next_handler=is_next_handler)

    def edited_photo(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_message", field="photo", trigger=trigger, is_next_handler=is_next_handler)

    def edited_sticker(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="sticker", trigger=trigger, is_next_handler=is_next_handler)

    def edited_story(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_message", field="story", trigger=trigger, is_next_handler=is_next_handler)

    def edited_video(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="video", trigger=trigger, is_next_handler=is_next_handler)

    def edited_video_note(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_message", field="video_note", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_voice(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="voice", trigger=trigger, is_next_handler=is_next_handler)

    def edited_contact(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_message", field="contact", trigger=trigger, is_next_handler=is_next_handler)

    def edited_dice(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="dice", trigger=trigger, is_next_handler=is_next_handler)

    def edited_game(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_message", field="game", trigger=trigger, is_next_handler=is_next_handler)

    def edited_poll(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="poll", trigger=trigger, is_next_handler=is_next_handler)

    def edited_venue(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_message", field="venue", trigger=trigger, is_next_handler=is_next_handler)

    def edited_location(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="location", trigger=trigger, is_next_handler=is_next_handler)

    def edited_invoice(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="invoice", trigger=trigger, is_next_handler=is_next_handler)

    def edited_author_signature(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="author_signature", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_new_chat_members(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="new_chat_members", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_left_chat_member(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="left_chat_member", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_new_chat_title(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="new_chat_title", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_new_chat_photo(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="new_chat_photo", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_delete_chat_photo(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="delete_chat_photo", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_group_chat_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="group_chat_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_supergroup_chat_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="supergroup_chat_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_chat_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="channel_chat_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_message_auto_delete_timer_changed(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="message_auto_delete_timer_changed", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_migrate_to_chat_id(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="migrate_to_chat_id", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_migrate_from_chat_id(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="migrate_from_chat_id", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_pinned_message(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="pinned_message", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_successful_payment(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="successful_payment", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_user_shared(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="user_shared", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_chat_shared(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="chat_shared", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_connected_website(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="connected_website", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_write_access_allowed(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="write_access_allowed", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_passport_data(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="passport_data", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_proximity_alert_triggered(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="proximity_alert_triggered", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_forum_topic_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="forum_topic_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_forum_topic_edited(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="forum_topic_edited", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_forum_topic_closed(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="forum_topic_closed", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_general_forum_topic_hidden(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="general_forum_topic_hidden", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_general_forum_topic_unhidden(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="general_forum_topic_unhidden", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_video_chat_scheduled(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="video_chat_scheduled", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_video_chat_started(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="video_chat_started", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_video_chat_ended(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="video_chat_ended", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_video_chat_participants_invited(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="video_chat_participants_invited", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_web_app_data(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_message", field="web_app_data", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_text(self, *, trigger, is_next_handler=False):
        return self.on(update_type="channel_post", field="text", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_animation(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="animation", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_audio(self, *, trigger, is_next_handler=False):
        return self.on(update_type="channel_post", field="audio", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_document(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="document", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_photo(self, *, trigger, is_next_handler=False):
        return self.on(update_type="channel_post", field="photo", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_sticker(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="sticker", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_story(self, *, trigger, is_next_handler=False):
        return self.on(update_type="channel_post", field="story", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_video(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="video", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_video_note(self, *, trigger, is_next_handler=False):
        return self.on(update_type="channel_post", field="video_note", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_voice(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="voice", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_contact(self, *, trigger, is_next_handler=False):
        return self.on(update_type="channel_post", field="contact", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_dice(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="dice", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_game(self, *, trigger, is_next_handler=False):
        return self.on(update_type="channel_post", field="game", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_poll(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="poll", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_venue(self, *, trigger, is_next_handler=False):
        return self.on(update_type="channel_post", field="venue", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_location(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="location", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_invoice(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="invoice", trigger=trigger, is_next_handler=is_next_handler)

    def channel_post_author_signature(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="author_signature", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_new_chat_members(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="new_chat_members", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_left_chat_member(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="left_chat_member", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_new_chat_title(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="new_chat_title", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_new_chat_photo(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="new_chat_photo", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_delete_chat_photo(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="delete_chat_photo", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_group_chat_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="group_chat_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_supergroup_chat_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="supergroup_chat_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_channel_chat_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="channel_chat_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_message_auto_delete_timer_changed(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="message_auto_delete_timer_changed", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_migrate_to_chat_id(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="migrate_to_chat_id", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_migrate_from_chat_id(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="migrate_from_chat_id", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_pinned_message(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="pinned_message", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_successful_payment(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="successful_payment", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_user_shared(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="user_shared", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_chat_shared(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="chat_shared", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_connected_website(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="connected_website", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_write_access_allowed(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="write_access_allowed", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_passport_data(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="passport_data", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_proximity_alert_triggered(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="proximity_alert_triggered", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_forum_topic_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="forum_topic_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_forum_topic_edited(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="forum_topic_edited", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_forum_topic_closed(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="forum_topic_closed", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_general_forum_topic_hidden(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="general_forum_topic_hidden", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_general_forum_topic_unhidden(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="general_forum_topic_unhidden", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_video_chat_scheduled(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="video_chat_scheduled", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_video_chat_started(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="video_chat_started", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_video_chat_ended(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="video_chat_ended", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_video_chat_participants_invited(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="video_chat_participants_invited", trigger=trigger,
                       is_next_handler=is_next_handler)

    def channel_post_web_app_data(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="channel_post", field="web_app_data", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_text(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="text", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_animation(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="animation", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_audio(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="audio", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_document(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="document", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_photo(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="photo", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_sticker(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="sticker", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_story(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="story", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_video(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="video", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_video_note(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="video_note", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_voice(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="voice", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_contact(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="contact", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_dice(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="dice", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_game(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="game", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_poll(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="poll", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_venue(self, *, trigger, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="venue", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_location(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="location", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_invoice(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="invoice", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_author_signature(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="author_signature", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_new_chat_members(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="new_chat_members", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_left_chat_member(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="left_chat_member", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_new_chat_title(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="new_chat_title", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_new_chat_photo(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="new_chat_photo", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_delete_chat_photo(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="delete_chat_photo", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_group_chat_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="group_chat_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_supergroup_chat_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="supergroup_chat_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_channel_chat_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="channel_chat_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_message_auto_delete_timer_changed(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="message_auto_delete_timer_changed", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_migrate_to_chat_id(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="migrate_to_chat_id", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_migrate_from_chat_id(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="migrate_from_chat_id", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_pinned_message(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="pinned_message", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_successful_payment(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="successful_payment", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_user_shared(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="user_shared", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_chat_shared(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="chat_shared", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_connected_website(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="connected_website", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_write_access_allowed(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="write_access_allowed", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_passport_data(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="passport_data", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_proximity_alert_triggered(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="proximity_alert_triggered", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_forum_topic_created(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="forum_topic_created", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_forum_topic_edited(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="forum_topic_edited", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_forum_topic_closed(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="forum_topic_closed", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_general_forum_topic_hidden(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="general_forum_topic_hidden", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_general_forum_topic_unhidden(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="general_forum_topic_unhidden", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_video_chat_scheduled(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="video_chat_scheduled", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_video_chat_started(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="video_chat_started", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_video_chat_ended(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="video_chat_ended", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_video_chat_participants_invited(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="video_chat_participants_invited", trigger=trigger,
                       is_next_handler=is_next_handler)

    def edited_channel_post_web_app_data(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="edited_channel_post", field="web_app_data", trigger=trigger,
                       is_next_handler=is_next_handler)

    def message_reaction_old_reaction(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message_reaction", field="old_reaction", trigger=trigger,
                       is_next_handler=is_next_handler)

    def message_reaction_new_reaction(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="message_reaction", field="new_reaction", trigger=trigger,
                       is_next_handler=is_next_handler)

    def inline_query(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="inline_query", field="query", trigger=trigger,
                       is_next_handler=is_next_handler)

    def chosen_inline_result(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="chosen_inline_result", field="query", trigger=trigger,
                       is_next_handler=is_next_handler)

    def callback_query(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="callback_query", field="data", trigger=trigger,
                       is_next_handler=is_next_handler)

    def shipping_query_invoice_payload(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="shipping_query", field="invoice_payload", trigger=trigger,
                       is_next_handler=is_next_handler)

    def shipping_query_shipping_address(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="shipping_query", field="shipping_address", trigger=trigger,
                       is_next_handler=is_next_handler)

    def pre_checkout_query_invoice_payload(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="pre_checkout_query", field="invoice_payload", trigger=trigger,
                       is_next_handler=is_next_handler)

    def pre_checkout_query_order_info(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="pre_checkout_query", field="order_info", trigger=trigger,
                       is_next_handler=is_next_handler)

    def poll_question(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="poll", field="question", trigger=trigger,
                       is_next_handler=is_next_handler)

    def poll_type(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="poll", field="type", trigger=trigger,
                       is_next_handler=is_next_handler)

    def poll_answer_voter_chat(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="poll_answer", field="voter_chat", trigger=trigger,
                       is_next_handler=is_next_handler)

    def poll_answer_user(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="poll_answer", field="user", trigger=trigger,
                       is_next_handler=is_next_handler)

    def my_chat_member_old_chat_member(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="my_chat_member", field="old_chat_member", trigger=trigger,
                       is_next_handler=is_next_handler)

    def my_chat_member_new_chat_member(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="my_chat_member", field="new_chat_member", trigger=trigger,
                       is_next_handler=is_next_handler)

    def chat_member_old_chat_member(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="chat_member", field="old_chat_member", trigger=trigger,
                       is_next_handler=is_next_handler)

    def chat_member_new_chat_member(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="chat_member", field="new_chat_member", trigger=trigger,
                       is_next_handler=is_next_handler)

    def chat_join_request_user_chat_id(self, *, trigger=None, is_next_handler=False):
        return self.on(update_type="chat_join_request", field="user_chat_id", trigger=trigger,
                       is_next_handler=is_next_handler)


class LabeledRouter(Router):
    def __init__(self, label):
        super().__init__()
        self._label = label

    @property
    def label(self):
        return self._label
