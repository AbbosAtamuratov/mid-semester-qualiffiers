from View.Display import Display
from Database.DataBase import Database
from FileManager.XMLfileManager import XMLfileManager

d1 = Display()
db = Database(d1)

print('ok, testing loading xml...\n')
# print('ok, testing saving xml...\n')

# for i in range(4):
#     db.create()

xfm = XMLfileManager()

# xfm.save(db.notepad)

db.notepad=xfm.load()
db.list()