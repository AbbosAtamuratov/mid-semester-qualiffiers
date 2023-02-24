from View.Display import Display
from Database.DataBase import Database
from FileManager.JSONfileManager import JSONfileManager

d1 = Display()
db = Database(d1)

print('ok, testing loading json...\n')

# for i in range(3):
#     db.create()

jfm = JSONfileManager()

# jfm.save(db.notepad)

db.notepad=jfm.load()
db.list()