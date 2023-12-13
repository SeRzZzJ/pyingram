from abc import ABC, abstractmethod

from pyongram.utils.update_parser import UpdateParser


class BaseSession(ABC):
    def __init__(self, update):
        update_parser = UpdateParser(update)
        self._user_id = update_parser.update_from_id()

    @property
    def user_id(self):
        return self._user_id

    @abstractmethod
    def is_session(self):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def update(self, key, value):
        pass

    @abstractmethod
    def clear(self, key=None):
        pass


class MemorySession(BaseSession, ABC):
    def __init__(self, update):
        super().__init__(update)
        self._data = {}
        self._form = ""

    @property
    def data(self):
        return self._data

    def link_to_form(self, name):
        self._form = name

    @property
    def form(self):
        return self._form

    @form.setter
    def form(self, name):
        self._form = name

    def check_the_session_form(self, router_name):
        return self._form == router_name and self.user_id

    def is_session(self):
        return self._form and self.user_id

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        if key not in self.data:
            return 0
        return self.data[key]

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            raise ValueError

    def clear(self, key=None):
        if key is not None:
            del self._data[key]
        self._data = {}


# class FileSessionJSONModel:
#     def __init__(self, user_id, path):
#         self._user_id = user_id
#         self._path = path
#         self._json_model = {}
#
#     def model_init(self):
#         self._json_model = {"users": []}
#         # with open(self._path, mode="w") as file:
#         #     file.write(dumps({"users": []}))
#         return self
#
#     def load_model(self):
#         with open(self._path, mode="r") as file:
#             self._json_model = load(file)
#         return self
#
#     def get_all_users(self):
#         return self._json_model["users"]
#
#     def get_user(self):
#         try:
#             # print(self._json_model)
#             return next(filter(lambda u: u["user_id"] == self._user_id, self._json_model["users"]))
#         except StopIteration:
#             self.add_new_user()
#
#     def get_user_all_sessions(self):
#         user = self.get_user()
#         return user["sessions"]
#
#     def get_user_last_session(self):
#         user = self.get_user()
#         if not user:
#             return {}
#         sessions = user["sessions"]
#         return sessions[-1]
#
#     def is_active_sessions(self):
#         user = self.get_user()
#         return user["is_active"]
#
#     def add_new_user(self):
#         self._json_model["users"].append({
#             "user_id": self._user_id,
#             "sessions": [],
#             "is_active": True
#         })
#         return self
#
#     def add_for_new_session_user(self, key, value):
#         user = self.get_user()
#         user["sessions"].append({key: value})
#         return self
#
#     def add_for_last_session_user(self, key, value):
#         user = self.get_user()
#         user["sessions"][-1][key] = value
#         return self
#
#     def del_user_last_session(self, key):
#         user = self.get_user()
#         session = user["sessions"][-1]
#         session.pop(key)
#         return self
#
#     def save(self):
#         with open(self._path, mode="w") as file:
#             # file.write(dumps({"users": self.get_all_users()}))
#             file.write(dumps(self._json_model))
#         return self
#
#
# class FileMemorySession(BaseSession, ABC):
#     def __init__(self, name, user_id, path="memory/data_sessions.json"):
#         super().__init__(name, user_id)
#         self._path = path
#         self._model = FileSessionJSONModel(user_id, path)
#
#     def session_init(self):
#         # self._data = self._model.model_init().save().load_model().get_user()
#         self._model.model_init().add_new_user().save().load_model()
#         return self
#
#     def set(self, key, value):
#         # super().set(key, value)
#         self._model.load_model().add_for_new_session_user(key, value).save()
#         print(self._model.get_user())
#
#     def get(self, key):
#         # return self.data[key]
#         return self._model.load_model().get_user_last_session()[key]
#
#     def update(self, key, value):
#         # super().update(key, value)
#         self._model.load_model().add_for_last_session_user(key, value).save()
#
#     def clear(self, key=None):
#         # super().clear(key)
#         if key is not None:
#             return self._model.load_model().del_user_last_session(key).save()
#         self._model.model_init().save().load_model()
#

# m = FileMemorySession(8558)
# m.session_init()
# print(m._model)
# m.download_data_from_file()
# print(m)
# m.update("msg", "msg text!!! HELLO WORLD!!!")
# print(m.get("msg"))
# m.clear("msg")


class RedisSession:
    pass
