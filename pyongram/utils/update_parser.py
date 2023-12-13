class UpdateParser:
    def __init__(self, update):
        self._update = update

    def update_type(self):
        return list(self._update.keys())[1]

    def update_from(self):
        update_from_index = list(self._update[self.update_type()].keys()).index("from")
        return list(self._update[self.update_type()].keys())[update_from_index]

    def update_from_id(self):
        return self._update[self.update_type()][self.update_from()]["id"]

    def update_data_field(self, field):
        return self._update[self.update_type()][field]

    def check_update_data_field(self, field):
        return field in self._update[self.update_type()]
