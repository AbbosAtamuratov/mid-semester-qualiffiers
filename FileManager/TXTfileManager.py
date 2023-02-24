from FileManager.FileManager import FileManager
from Model.Note import Note
from datetime import datetime

class TXTfileManager(FileManager):

    def __init__(self):
        super().__init__('notes.txt')

    def save(self, notepad):
        with open(self.file_name, 'w') as txt_file:
            for note in notepad:
                line = f'{note.id} :: {note.timestamp.strftime("%H:%M:%S %d-%m-%Y")} ' \
                       f':: {note.title} :: {note.text}'
                txt_file.write(line+'\n')

    def load(self):
        notes = []
        with open(self.file_name, 'r') as txt_file:
           for line in txt_file:
               contents = line.split('::')
               contents = [c.strip() for c in contents]
               note_element = Note(contents[2], contents[3])
               note_element.id = contents[0]
               note_element.timestamp = datetime.strptime(contents[1], "%H:%M:%S %d-%m-%Y")
               notes.append(note_element)
        return notes