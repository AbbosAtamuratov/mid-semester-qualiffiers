from FileManager.FileManagerFactory import FileManagerFactory
from FileManager.FileManager import FileManager
from Database.DataBase import Database

class CentralControl:
    def __init__(self):
        self.data_base = Database()
        self.is_running = True

    def run(self):
        self.data_base.display.greet()

        path = self.data_base.display.format_picker()
        fm_factory = FileManagerFactory()
        is_unchosen = True
        while is_unchosen:
            if 0 < path < 5:
                if path == 1:
                    file_manager=fm_factory.get_txt_file_manager()
                elif path == 2:
                    file_manager=fm_factory.get_json_file_manager()
                elif path == 3:
                    file_manager=fm_factory.get_csv_file_manager()
                else:
                    file_manager=fm_factory.get_xml_file_manager()
                self.data_base.display.flash('Nice choice')
                is_unchosen = False
            else:
                self.data_base.display.oopsie()
                self.data_base.display.flash('Try again...')

        self.data_base.notepad = file_manager.load()
        while self.is_running:
            self.data_base.display.show_menu()
            user_input = int(self.data_base.display.promt('Choose a command number: '))
            if 0 < user_input < 8:
                if user_input == 1:
                    # create
                   self.data_base.create()
                elif user_input == 2:
                    # update
                    user_input = self.validate_id()
                    self.data_base.update(user_input)
                elif user_input == 3:
                    # delete
                    user_input = self.validate_id()
                    self.data_base.delete(user_input)
                elif user_input == 4:
                    # list
                    self.data_base.list()
                elif user_input == 5:
                    # find by id
                    user_input = self.validate_id()
                    self.data_base.find_by_id(user_input)
                elif user_input == 6:
                    # find by date
                    user_input = self.validate_date()
                    self.data_base.find_by_date(user_input)
                else:
                    self.data_base.display.say_bye()
                    file_manager.save(self.data_base.notepad)
                    self.is_running = False
            else:
                self.data_base.display.oopsie()
                self.data_base.display.flash('Try again...')

    def validate_id(self):
        id_is_not_valid = True
        while id_is_not_valid:
            user_id = self.data_base.display.promt('Insert id: ')
            if int(user_id) in [int(note.id) for note in self.data_base.notepad]:
                id_is_not_valid = False
                self.data_base.display.flash('id validation status: success...')
            else:
                self.data_base.display.flash('id validation status: fail...')
                self.data_base.display.oopsie()
                self.data_base.display.flash('Please try again')
        return user_id
    def validate_date(self):
        date_is_not_valid = True
        while date_is_not_valid:
            user_date = self.data_base.display.promt('Insert date in dd-mm-yyyy format: ')
            if user_date in [note.timestamp.split(' ')[1] for note in self.data_base.notepad]:
                date_is_not_valid = False
                self.data_base.display.flash('date validation status: success...')
            else:
                self.data_base.display.flash('date validation status: fail...')
                self.data_base.display.oopsie()
                self.data_base.display.flash('Please try again')
        return user_date