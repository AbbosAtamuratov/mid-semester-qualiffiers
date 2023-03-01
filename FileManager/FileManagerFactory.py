from FileManager.TXTfileManager import TXTfileManager
from FileManager.XMLfileManager import XMLfileManager
from FileManager.JSONfileManager import JSONfileManager
from FileManager.CSVfileManager import CSVfileManager

class FileManagerFactory:
    def get_txt_file_manager(self):
        return TXTfileManager()

    def get_json_file_manager(self):
        return JSONfileManager()

    def get_csv_file_manager(self):
        return CSVfileManager()

    def get_xml_file_manager(self):
        return XMLfileManager()