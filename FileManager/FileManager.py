from abc import ABC, abstractclassmethod

class FileManager(ABC):

    def __init__(self, file_name):
        self.file_name = file_name

    @abstractclassmethod
    def save(self, notepad):
        pass

    @abstractclassmethod
    def load(self):
        pass