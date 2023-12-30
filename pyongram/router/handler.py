from types import FunctionType


class Handler:
    def __init__(self, update_type, field, out_data, handler_fn, is_next_handler=False):
        self._update_type = update_type
        self._field = field
        self._out_data = out_data
        self._handler_fn = handler_fn
        self._is_next_handler = is_next_handler

    def __repr__(self):
        return (f"{self.__class__.__name__}(self._update_type={self._update_type}, "
                f"self._field={self._field}, "
                f"self._out_data={self._out_data}"
                f"self._handler_fn={self._handler_fn}"
                f"self._is_next_handler={self._is_next_handler})")

    @property
    def update_type(self):
        return self._update_type

    @property
    def field(self):
        return self._field

    @property
    def out_data(self):
        if isinstance(self._out_data, FunctionType):
            return self._out_data
        else:
            raise TypeError()

    @property
    def is_next_handler(self):
        return self._is_next_handler

    async def handle(self, context):
        await self._handler_fn(context)
