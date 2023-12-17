import json


class Markup:
    @staticmethod
    def keyboard(buttons):
        return ReplyKeyboardMarkup(buttons)

    @staticmethod
    def inline_keyboard(buttons):
        return InlineKeyboardReplyMarkup(buttons)

    @staticmethod
    def reply_keyboard_remove():
        return ReplyKeyboardRemove()

    @staticmethod
    def force_reply():
        return ForceReply()


class ReplyMarkup:
    def __init__(self):
        self._markup = None

    @property
    def markup(self):
        return json.dumps(self._markup, ensure_ascii=False)


class InputFieldPlaceholder(ReplyMarkup):
    def __init__(self):
        super().__init__()

    def input_field_placeholder(self, value):
        self._markup.update({"input_field_placeholder": value})
        return self


class Selective(ReplyMarkup):
    def __init__(self):
        super().__init__()

    def selective(self):
        self._markup.update({"selective": True})
        return self


class ReplyKeyboardMarkup(InputFieldPlaceholder, Selective):
    def __init__(self, buttons):
        super().__init__()
        self._markup = {"keyboard": buttons}

    def is_persistent(self):
        self._markup.update({"is_persistent": True})
        return self

    def resize_keyboard(self):
        self._markup.update({"resize_keyboard": True})
        return self

    def one_time_keyboard(self):
        self._markup.update({"one_time_keyboard": True})
        return self


class InlineKeyboardReplyMarkup(ReplyMarkup):
    def __init__(self, buttons):
        super().__init__()
        self._markup = {"inline_keyboard": buttons}


class ReplyKeyboardRemove(Selective):
    def __init__(self):
        super().__init__()
        self._markup = {"remove_keyboard": True}


class ForceReply(InputFieldPlaceholder, Selective):
    def __init__(self):
        super().__init__()
        self._markup = {"force_reply": True}
