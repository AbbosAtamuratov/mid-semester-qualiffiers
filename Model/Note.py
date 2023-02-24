from datetime import *
import json
class Note:

    def __init__(self, title, text):
         self.title = title
         self.text = text
         self._id = 0
         self.timestamp = datetime.now()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, num):
        self._id = num

    def __str__(self):
        return f'id: {self.id}\n' \
               f'time stamp: {self.timestamp.strftime("%H:%M:%S %d-%m-%Y")}\n' \
               f'title: {self.title}\n' \
               f'text: {self.text}\n'

class NoteEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)