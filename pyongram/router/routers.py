from abc import ABC
from types import FunctionType

from pyongram.router.handler import Handler


class BaseRouter(ABC):
    def __init__(self):
        self._handlers = []
        self._update_type = None

    @property
    def handlers(self):
        return self._handlers

    def assign(self, routers):
        self._handlers.extend(routers)

    def on(self, *, field, trigger=None, is_next_handler=False):
        self._check_handler_trigger_and_field_update_type_isinstance(update_type=self._update_type,
                                                                     field=field,
                                                                     trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field=field,
                                              out_data=trigger,
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


class BaseMessageRouter(BaseRouter, ABC):
    def __init__(self):
        super().__init__()

    def text(self, *, trigger, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="text",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def animation(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="animation",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def audio(self, *, trigger, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="audio",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def document(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="document",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def photo(self, *, trigger, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="photo",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def sticker(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="sticker",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def story(self, *, trigger, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="story",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def video(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="video",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def video_note(self, *, trigger, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="video_note",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def voice(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="voice",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def contact(self, *, trigger, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="contact",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def dice(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="dice",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def game(self, *, trigger, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="game",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def poll(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="poll",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def venue(self, *, trigger, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="venue",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def location(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="location",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def invoice(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="invoice",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)


class MessageRouter(BaseMessageRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "message"

    def command(self, *, trigger, is_next_handler=False):
        super()._check_handler_trigger_isinstance(trigger=trigger)
        return super()._returned_build_decorator(update_type="message",
                                                 field="text",
                                                 out_data=lambda msg: msg["text"] == f"/{trigger}",
                                                 is_next_handler=is_next_handler)

    def start(self, is_next_handler=False):
        return super()._returned_build_decorator(update_type="message", field="text",
                                                 out_data=lambda msg: msg["text"] == "/start",
                                                 is_next_handler=is_next_handler)

    def help(self, is_next_handler=False):
        return super()._returned_build_decorator(update_type="message", field="text",
                                                 out_data=lambda msg: msg["text"] == "/help",
                                                 is_next_handler=is_next_handler)

    def settings(self, is_next_handler=False):
        return super()._returned_build_decorator(update_type="message", field="text",
                                                 out_data=lambda msg: msg["text"] == "/settings",
                                                 is_next_handler=is_next_handler)

    def admin(self, is_next_handler=False):
        return super()._returned_build_decorator(update_type="message", field="text",
                                                 out_data=lambda msg: msg["text"] == "/admin",
                                                 is_next_handler=is_next_handler)


class EditedMessageRouter(BaseMessageRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "edited_message"


class ChannelPostRouter(BaseMessageRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "channel_post"


class EditedChannelPostRouter(BaseMessageRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "edited_channel_post"


class BaseQueryRouter(BaseRouter, ABC):
    def __init__(self):
        super().__init__()

    def query(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="query",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)


class InlineQueryRouter(BaseQueryRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "inline_query"


class ChosenInlineResultRouter(BaseQueryRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "chosen_inline_result"


class CallbackQueryRouter(BaseRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "callback_query"

    def data(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="data",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)


class BaseInvoicePayloadRouter(BaseRouter, ABC):
    def __init__(self):
        super().__init__()

    def invoice_payload(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="invoice_payload",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)


class ShippingQueryRouter(BaseInvoicePayloadRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "shipping_query"

    def shipping_address(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="shipping_address",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)


class PreCheckoutQueryRouter(BaseInvoicePayloadRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "pre_checkout_query"

    def order_info(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="order_info",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)


class PollRouter(BaseRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "poll"

    def question(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="question",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def type(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="type",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)


class PollAnswerRouter(BaseRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "poll_answer"

    def voter_chat(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="voter_chat",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def user(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="user",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)


class ChatMemberUpdatedRouter(BaseRouter, ABC):
    def __init__(self):
        super().__init__()

    def old_chat_member(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="old_chat_member",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)

    def new_chat_member(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="new_chat_member",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)


class MyChatMemberRouter(ChatMemberUpdatedRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "my_chat_member"


class ChatMemberRouter(ChatMemberUpdatedRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "chat_member"


class ChatJoinRequestRouter(BaseRouter, ABC):
    def __init__(self):
        super().__init__()
        self._update_type = "chat_join_request"

    def user_chat_id(self, *, trigger=None, is_next_handler=False):
        self._check_handler_trigger_isinstance(trigger=trigger)
        return self._returned_build_decorator(update_type=self._update_type,
                                              field="user_chat_id",
                                              out_data=trigger,
                                              is_next_handler=is_next_handler)


class FormRouter(BaseRouter):
    def __init__(self, name):
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name


class MessageFormRouter(FormRouter, MessageRouter, ABC):
    def __init__(self, name):
        super().__init__(name)


class EditedMessageFormRouter(FormRouter, EditedMessageRouter, ABC):
    def __init__(self, name):
        super().__init__(name)


class ChannelPostFormRouter(FormRouter, ChannelPostRouter, ABC):
    def __init__(self, name):
        super().__init__(name)


class EditedChannelPostFormRouter(FormRouter, EditedChannelPostRouter, ABC):
    def __init__(self, name):
        super().__init__(name)


class InlineQueryFormRouter(FormRouter, InlineQueryRouter, ABC):
    def __init__(self, name):
        super().__init__(name)


class ChosenInlineResultFormRouter(FormRouter, ChosenInlineResultRouter, ABC):
    def __init__(self, name):
        super().__init__(name)


class CallbackQueryFormRouter(FormRouter, CallbackQueryRouter, ABC):
    def __init__(self, name):
        super().__init__(name)


class ShippingQueryFormRouter(FormRouter, ShippingQueryRouter, ABC):
    def __init__(self, name):
        super().__init__(name)


class PreCheckoutQueryFormRouter(FormRouter, PreCheckoutQueryRouter, ABC):
    def __init__(self, name):
        super().__init__(name)


class PollFormRouter(FormRouter, PollRouter, ABC):
    def __init__(self, name):
        super().__init__(name)


class PollAnswerFormRouter(FormRouter, PollAnswerRouter, ABC):
    def __init__(self, name):
        super().__init__(name)


class MyChatMemberFormRouter(FormRouter, MyChatMemberRouter, ABC):
    def __init__(self, name):
        super().__init__(name)


class ChatMemberFormRouter(FormRouter, ChatMemberRouter, ABC):
    def __init__(self, name):
        super().__init__(name)


class ChatJoinRequestFormRouter(FormRouter, ChatJoinRequestRouter, ABC):
    def __init__(self, name):
        super().__init__(name)
