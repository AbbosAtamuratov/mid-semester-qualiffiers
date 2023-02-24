from View.Display import Display
from Database.DataBase import Database
from FileManager.CSVfileManager import CSVfileManager

d1 = Display()
db = Database(d1)

print('ok, testing loading csv...\n')
# print('ok, testing saving csv...\n')

# for i in range(3):
#     db.create()

cfm = CSVfileManager()

# cfm.save(db.notepad)

db.notepad=cfm.load()
db.list()