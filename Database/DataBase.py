from datetime import datetime
from Model.Note import Note
from View.Display import Display


class Database:
    def __init__(self):
        self._display = Display()
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
            new_index = max([int(note.id) for note in self._notepad]) + 1
        else:
            new_index = 1
        new_note.id = new_index
        self.notepad.append(new_note)

    def update(self, id):
        for note in self._notepad:
            if int(note.id) == int(id):
                note.title = self.display.promt('Input new title: ')
                note.text = self.display.promt('Input new text: ')
                note.timestamp = datetime.now().strftime("%H:%M:%S %d-%m-%Y")

    def delete(self, id):
        index = 0
        target = 0
        for note in self._notepad:
            if int(note.id) == int(id):
                target = index
            index += 1
        self._notepad.pop(target)


    def find_by_id(self, id):
        index = 0
        target = 0
        for note in self.notepad:
            if int(note.id) == int(id):
                target = index
            index += 1
        self._display.flash(str(self.notepad[target]))

    def find_by_date(self, date):
        comparable_date = datetime.strptime(str(date),"%d-%m-%Y").date()
        target = 0
        index = 0
        for note in self.notepad:
            note_date = note.timestamp.split(' ')[1]
            if datetime.strptime(note_date, "%d-%m-%Y").date() == comparable_date:
                target = index
            index += 1
        self.display.flash(self.notepad[target])

    def list(self):
        self._display.show_all(self._notepad)