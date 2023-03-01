from FileManager.FileManagerFactory import FileManagerFactory
from FileManager.FileManager import FileManager
from Database.DataBase import Database

class CentralControl:
    def __init__(self):
        self.data_base = Database()
        self.file_manager = FileManager()
        self.is_running = True

    @property
    def file_manager(self):
        return self.file_manager

    @file_manager.setter
    def file_manager(self, chosen):
        self.file_manager = chosen

    def run(self):
        self.data_base.display.greet()

        path = self.data_base.display.format_picker()
        fm_factory = FileManagerFactory()
        is_unchosen = True
        while is_unchosen:
            if 0 < path < 5:
                if path == 1:
                    self.file_manager(fm_factory.get_txt_file_manager())
                elif path == 2:
                    self.file_manager(fm_factory.get_json_file_manager())
                elif path == 3:
                    self.file_manager(fm_factory.get_csv_file_manager())
                else:
                    self.file_manager(fm_factory.get_xml_file_manager())
                self.data_base.display.flash('Nice choice')
                is_unchosen = False
            else:
                self.data_base.display.oopsie()
                self.data_base.display.flash('Try again...')

        while self.is_running:
            self.data_base.notepad = self.file_manager.load()
            self.data_base.display.show_menu()
            user_input = int(self.data_base.promt('Choose a command number: '))
            if 0 < user_input < 8:
                if user_input == 1:
                    # create
                    pass
                elif user_input == 2:
                    # update
                    pass
                elif user_input == 3:
                    # delete
                    pass
                elif user_input == 4:
                    # list
                    pass
                elif user_input == 5:
                    # find by id
                    pass
                elif user_input == 6:
                    # find by date
                    pass
                else:
                    self.data_base.display.say_bye()
                    self.file_manager.save(self.data_base.notepad())
                    self.is_running = False
            else:
                self.data_base.display.oopsie()
                self.data_base.display.flash('Try again...')