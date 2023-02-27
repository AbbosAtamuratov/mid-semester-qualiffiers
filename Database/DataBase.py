from datetime import datetime
from Model.Note import Note
from View.Display import Display


class Database:
    def __init__(self, display):
        self._display = display
        self._notepad = []

    @property
    def display(self):
        return self._display

    @property
    def notepad(self):
        return self._notepad

    @notepad.setter
    def notepad(self, notes):
        self._notepad = notes

    def create(self):
        inp_title = self.display.promt('Input your title: ')
        inp_text = self.display.promt('Input your text: ')
        new_note = Note(inp_title, inp_text)
        if len(self._notepad) != 0:
            new_index = max([note.id for note in self._notepad]) + 1
        else:
            new_index = 1
        new_note.id = new_index
        self.notepad.append(new_note)

    def update(self, id):
        id_list = [note.id for note in self._notepad]
        if int(id) in id_list:
            for note in self._notepad:
                if note.id == id:
                    note.title = self.display.promt('Input new title: ')
                    note.text = self.display.promt('Input new text: ')
                    note.timestamp = datetime.now()
        else:
            self.display.flash('Sorry! id is not found')

    def delete(self, id):
        id_list = [note.id for note in self._notepad]
        if int(id) in id_list:
            index = 0
            for note in self._notepad:
                if note.id == id:
                    target = index
                index += 1
            self._notepad.pop(target)
        else:
            self.display.flash('Sorry! id is not found')

    def find_by_id(self, id):
        id_list = [note.id for note in self._notepad]
        if int(id) in id_list:
            index = 0
            for note in self._notepad:
                if note.id == id:
                    target = index
                index += 1
            self._display.flash(str(self._notepad[target]))
        else:
            self.display.flash('Sorry! id is not found')

    # def find_by_date(self, date):


    def list(self):
        self._display.show_all(self._notepad)