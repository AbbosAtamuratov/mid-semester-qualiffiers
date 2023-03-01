from FileManager.FileManager import FileManager
from Model.Note import *
import json

class JSONfileManager(FileManager):

    def __init__(self):
        super().__init__('notes.json')

    def save(self, notepad):
        json_string = json.dumps([note.__dict__ for note in notepad], indent=4)
        with open(self.file_name, 'w') as json_file:
            json_file.write(json_string)

    def load(self):
        notepad=[]
        with open(self.file_name, 'r') as json_file:
            source_str = json_file.read()
        json_dicts = json.loads(source_str)
        for dict_note in json_dicts:
            note = Note(dict_note['title'], dict_note['text'])
            note._id = int(dict_note['_id'])
            note.timestamp = dict_note['timestamp']
            notepad.append(note)
        return notepad