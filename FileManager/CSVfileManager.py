from FileManager.FileManager import FileManager
import pandas as pd
from Model.Note import Note


class CSVfileManager(FileManager):

    def __init__(self):
        super().__init__('notes.csv')

    def save(self, notepad):
        data = pd.DataFrame([note.__dict__ for note in notepad])
        data.to_csv(self.file_name, index=False)

    def load(self):
        notepad = []
        df = pd.read_csv(self.file_name)
        for index, row in df.iterrows():
            title = row['title']
            text = row['text']
            _id = int(row['_id'])
            timestamp = row['timestamp']
            note = Note(title, text)
            note._id = _id
            note.timestamp = timestamp
            notepad.append(note)
        return notepad