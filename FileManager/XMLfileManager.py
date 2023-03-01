import xmltodict as xD
from FileManager.FileManager import FileManager
from Model.Note import Note

class XMLfileManager(FileManager):
    def __init__(self):
        super().__init__('notes.xml')

    def save(self, notepad):
        dict_notes = [note.__dict__ for note in notepad]
        xml_string = xD.unparse({"notes": {"note": dict_notes}}, pretty=True)

        with open(self.file_name, 'w') as x_file:
            x_file.write(xml_string)

    def load(self):
        notepad = []
        with open(self.file_name, 'r') as x_file:
            source_str = x_file.read()

        dict_notes = xD.parse(source_str)
        for n in dict_notes['notes']['note']:
            note = Note(n['title'], n['text'])
            note._id = n['_id']
            note.timestamp = n['timestamp']
            notepad.append(note)
        return notepad